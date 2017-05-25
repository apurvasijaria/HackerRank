#https://www.hackerrank.com/challenges/apple-and-orange/
#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
count=0
for i in range(m):
    d=apple[i]+a
    if(d<=t and d>=s):
        count=count+1
print count
count=0
for i in range(n):
    d=orange[i]+b
    if(d<=t and d>=s):
        count=count+1
print count
