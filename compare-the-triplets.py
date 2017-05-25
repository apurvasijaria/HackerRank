#https://www.hackerrank.com/challenges/compare-the-triplets

#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    a=0
    b=0
    c=[]
    if(a0>b0):
        a=a+1
    elif(b0>a0):
        b=b+1
    if(a1>b1):
        a=a+1
    elif(b1>a1):
        b=b+1
    if(a2>b2):
        a=a+1
    elif(b2>a2):
        b=b+1
    c.append(a)
    c.append(b)
    return c
    

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))


