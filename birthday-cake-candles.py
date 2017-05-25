#!/bin/python
#APurva Sijaria
#https://www.hackerrank.com/challenges/birthday-cake-candles
import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))
t=height[0]
count=0
for i in range(len(height)):
    if(t<=height[i]):
        t=height[i]
for i in range(len(height)):
    if(height[i]==t):
        count=count+1
print count
