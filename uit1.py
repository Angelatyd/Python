import re

# 寻找Name集中页
f = open('uit.txt','r')
f1 = f.read()
pattern1 = re.compile('PROSPECTUS')
m1 = pattern1.search(f1)
f2 = f1[0:m1.end()]
list = f2.split('\n-------------------------------------------------------------')

pattern2 = re.compile('\w+(.*)\w+')
for c in list:
    print(pattern2.search(c).group())