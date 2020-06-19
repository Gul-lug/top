import requests
from collections import Counter
import re, sys, os
print(len(sys.argv))
if len(sys.argv)==1:
    st="in.txt"
else:
    st=sys.argv[1]

try:
    with open(st) as f:
        link = f.readline().strip()
        while link:
            html = requests.get(link, verify=False)
            if html.status_code == 200:
                print('Connecting.. ОК')
            #print(html.text)
                cnt = Counter(x for x in re.findall(r'[a-zA-Zа-яА-ЯёЁ\']{2,}', html.text))
                print(cnt.most_common(10))
            else:
                print('Connecting.. Error')
            link = f.readline().strip()
except Exception as err:
    print(err)

