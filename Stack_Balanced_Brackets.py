#!/bin/python

import sys

class Stack(object):
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.items==[]: return None
        return self.items.pop()
    def Top(self):
        if self.items==[]: return None
        return self.items[-1]
    def size(self):
        return len(self.items)
    def clean(self):
        self.items=[]

def balance(data, s):
    N=len(data)
    i=0
    o=0
    cl=0
    while i<N:
        #print s.Top(), data[i]
        if data[i]=='(' or data[i]=='{' or data[i]=='[':
            o+=1
            s.push(data[i])
        elif data[i]==')' or data[i]=='}' or data[i]==']':
            cl+=1
            if data[i]==')' and s.Top()=='(' :
                s.pop()
            elif data[i]==')' and s.Top()!='(' :
                return "NO"
            elif data[i]=='}' and s.Top()=='{' :
                s.pop()
            elif data[i]=='}' and s.Top()!='{' :
                return "NO"
            elif data[i]==']' and s.Top()=='[' :
                s.pop()
            elif data[i]==']' and s.Top()!='[' :
                return "NO"


        i+=1
    if o!=cl:
        return "NO"
    return 'YES'



t = int(raw_input().strip())
for a0 in xrange(t):
    data = raw_input().strip()
    s=Stack()
    print balance(data, s)



