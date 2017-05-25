#!/bin/python
#https://www.hackerrank.com/challenges/sock-merchant
import sys


n = int(raw_input().strip())
pair=0
use=[]
c = map(int,raw_input().strip().split(' '))
def see(a,use):
    #print a
    for i in range(len(use)):
        if(a==use[i]):
            #print use
            return False
    use.append(a)

    return True
for i in range(n):
    count=0
    if(see(c[i],use)):
        for j in range(n):
            if(c[j]==c[i]):
                count=count+1
    pair=pair+int(count/2)
    
print pair
