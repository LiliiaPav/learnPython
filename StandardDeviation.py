'''
Given an array, X, of N integers, calculate and print the standard deviation.
Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format).
An error margin of  will be tolerated for the standard deviation.
'''
import math
N=int(input())
X=input()
X=X.split()
X=list(map(int, X))
mean=sum(X)/N
temp=0
for elem in X:
    temp+=(elem-mean)**2

result= math.sqrt(temp/N)

print (round(result,1))
