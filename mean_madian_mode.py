'''
Given an array, L, of N integers, calculate and print the the respective
mean, median, and mode on separate lines.
If your array contains more than one modal value, choose the numerically smallest one.
'''

N=int(input())
L=input()
L=L.split()
L=list(map(int, L))

mean=sum(L)/N

L.sort()
s=int(N/2)
if N%2==0:
    median=(L[s-1]+L[s])/2
else:
    median=L[s-1]

temp={}
big=1
num=0
for elem in L:
    if elem in temp:
        temp[elem]=temp[elem]+1
        if temp[elem]>big:
            big=temp[elem]
            num=elem
    else:
        temp[elem]=1
if num==0:
    mode=L[0]
else:
    mode=num

print (mean)
print(median)
print(mode)
