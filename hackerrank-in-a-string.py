#https://www.hackerrank.com/challenges/hackerrank-in-a-string

#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    c=['h','a','c','k','e','r','r','a','n','k']
    i=0
    for a in s:
        if(a==c[i]):
            i=i+1
    if(i==len(c)):
        print 'YES'
    else:
        print 'NO'
        
