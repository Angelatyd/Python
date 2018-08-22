import requests
import bs4
import re

res = requests.get('https://doc.morningstar.com/Document/51246e60bfc35f0f6a9341dfa5ef3ecb.msdoc/original?clientid=globaldocuments&key=52dbc583e1012395')
uSoup = bs4.BeautifulSoup(res.text)
e = uSoup.select('body')
html = e[0].getText()
# 多行匹配～
# s1 = 'INVESTMENT OBJECTIVE'
# s2 = 'The trust seeks to'
# pattern = re.compile(s1+'.*?'+s2, flags=re.DOTALL+re.MULTILINE)
# result = pattern.findall(html)
# print(result)
# print(len(result))

with open('uit.txt','w') as f:
    f.write(html)
# print(html)