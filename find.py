import requests
import re

url = 'http://b8e0235a-f240-455d-a375-9f4fb9b27e4c.node3.buuoj.cn/shop?page='

for i in range(0, 500):
    url_t = url + str(i)
    res = requests.get(url_t)
    print(i)
    if '/static/img/lv/lv6.png' in res.text:
        print("ans:%d" % i)
        break