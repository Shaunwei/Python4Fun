import re

f = open('whodata.txt', 'r')

for eachLine in f:
    print re.split(r'\s\s+', eachLine.rstrip())

f.close()
