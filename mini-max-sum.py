#!/bin/python
#https://www.hackerrank.com/challenges/mini-max-sum

import sys
arr = map(int, raw_input().strip().split(' '))
sum=0
sum_arr=[]
a=[]
for i in range(len(arr)):
    sum=0
    for j in range(len(arr)):
        if(j!=i):
            sum=sum+arr[j]  
    sum_arr.append(sum)

min_sum=sum_arr[0]
max_sum=sum_arr[0]

for i in range(len(sum_arr)):
    if(sum_arr[i]<=min_sum):
        min_sum=sum_arr[i]
    if(sum_arr[i]>=max_sum):
        max_sum=sum_arr[i]
print str(min_sum)+' '+str(max_sum)
