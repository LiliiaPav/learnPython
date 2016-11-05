# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def Top(self):
        if self.items==[]: return None
        return self.items[-1]
    def size(self):
        return len(self.items)
    def clean(self):
        self.items=[]

import sys
S=Stack()
mx=Stack()
N=raw_input()
N= int (N)
for line in sys.stdin:
    line=map(int, line.strip().split())
    #print line
    if line[0]==1:
        S.push(line[1])
        if mx.size()==0:
            mx.push(line[1])
            #print mx.Top()
        elif mx.Top()<=line[1]:
            mx.push(line[1])

    elif line[0]==2:
        if S.Top()==mx.Top():
            mx.pop()
        S.pop()
        if S.isEmpty():
            mx.clean()
    elif line[0]==3:
        print mx.Top()