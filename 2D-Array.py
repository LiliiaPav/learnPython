#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

#print amaunt
res=[]
i=0
j=0
while j<4:
    temp=arr[j][i]+arr[j][i+1]+arr[j][i+2]+arr[j+1][i+1]+arr[j+2][i]+arr[j+2][i+1]+arr[j+2][i+2]
    res.append(temp)
    i+=1
    if i==4:
        j+=1
        i=0
#print res
print max(res)
