import requests
from collections import Counter
import re, sys
print(sys.argv[1])
try:
    with open(sys.argv[1]) as f:
        link = f.readline().strip()
        while link:
            html = requests.get(link, verify=False)
            if html.status_code == 200:
                print('Connecting.. ОК')
            #print(html.text)
                cnt = Counter(x for x in re.findall(r'[A-z\']{2,}', html.text))
                print(cnt.most_common(10))
            else:
                print('Connecting.. Error')
            link = f.readline().strip()
except Exception as err:
    print(err)



#cnt = Counter(x for x in re.findall(r'[A-z\']{2,}', txt))
#print(cnt.most_common(10))