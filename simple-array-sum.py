#https://www.hackerrank.com/challenges/simple-array-sum

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
sum=0
for i in range(len(arr)):
    sum=sum+arr[i]
print sum
