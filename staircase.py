#https://www.hackerrank.com/challenges/staircase
#!/bin/python

import sys


n = int(raw_input().strip())
for i in range(n):
    a=[]
    for k in range(n-i-1):
        a.append(' ')
    for k in range(i+1):
        a.append('#')
    print ''.join(a)
