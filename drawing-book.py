#!/bin/python
#https://www.hackerrank.com/challenges/drawing-book
import sys

def solve(n, p):
    if(p<=(n-p)):
        return int(p/2)
    elif(int(n/2)==int(p/2)):
        return int((n-p)/2)
    elif(p!=1):
        return int(n/2)-int(p/2)
    else:
        return 0
n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print(result)
