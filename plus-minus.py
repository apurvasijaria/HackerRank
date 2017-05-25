#https://www.hackerrank.com/challenges/plus-minus
#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
p=0
z=0
neg=0
for i in range(len(arr)):
    if(arr[i]<0):
        neg=neg+1
    if(arr[i]>0):
        p=p+1  
    if(arr[i]==0):
        z=z+1
print float(p)/float(n)
print float(neg)/float(n)
print float(z)/float(n)
