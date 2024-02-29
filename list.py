# Insert 10 random letters in the range ‘a’ through ‘z’ into a list. Perform the following tasks and display your results

import random

abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

workList=[]
for i in range(10):
    num=random.randrange(0, 26)
    workList.append(abc[num])
print("Random Letters")
print(workList)
print("Sort the list in ascending order.")
workList.sort()
print(workList)
print("Sort the list in descending order.")
workList.sort(reverse=True)
print(workList)
print("Unique values sorted in as ascending order.")
workSet=set(workList)
workList=list(workSet)
workList.sort()
print(workList)