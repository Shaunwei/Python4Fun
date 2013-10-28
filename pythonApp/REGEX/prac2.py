# coding: utf-8
import re
m = re.match('foo','foo')
if m is not None:
    m.group()
    
m = re.match('foo','food on the table')
m.group()
#Section1.3.6 (|)
bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print m.group()
    
m = re.match(bt, 'blt')
if m is not None:
    print m.group()
    
m
if m is not None:
    print m.group()
    
m = re.match(bt, 'He bit me!')
if m is not None:
    print m.group()
    
m = re.search(bt, 'He bit me!')
if m is not None:
    print m.group()

#Section 1.3.7 matching any single character (.)
anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None: print m.group()
m = re.match(anyend, 'end')
if m is not None: print m.group()
m = re.match(anyend, '\end')
if m is not None: print m.group()
m = re.match(anyend, '\nend')
if m is not None: print m.group()
m = re.search('.end', 'The end.')
if m is not None: print m.group()

#Section1.3.8 creating character classes ([])
m = re.match('[cr][23][dp][o2]','c3po') #mathes 'c3po'
#Section 1.3.9 Repetition, Special Characters, and Grouping
patt = '\w+@(\w+\.)?\w+\.com'
re.match(patt, 'nobody@xxx.com').group()
re.match(patt, 'nobody@www.xxx.com').group()
#Section 1.3.12 Searching and Replacing with sub() and subn()
s = 'attn: X\n\nDear X,\n'
re.sub('X','Mr. Smith',s)
re.subn('X','Mr. Smith',s)
print re.sub('X','Mr. Smith',s)
re.sub('[ae]','X','abcdef')
re.subn('[ae]','X','abcdef')
#Section
n ="""This line is the first,
another line,
that line, it's the best
"""
re.findall(r'(?im)(^th[\w]+)',n)
re.findall(r'(?im)(^th[\w ]+)',n)
re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
'(800) 555-1212').groupdict()
