"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
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

def preOrder1(root):
    s=Stack()
    if root == None: return None
    s.push(root)
    while s.size()>0:
        curr=s.Top()
        if curr.left and curr.right:
            print s.Top().data,
            s.pop()
            s.push(curr.right)
            s.push(curr.left)



        elif curr.left and not curr.right:
            print s.Top().data,
            s.pop()
            s.push(curr.left)
        elif curr.right and not curr.left:
            print s.Top().data,
            s.pop()
            s.push(curr.right)
        else:
            print curr.data,
            s.pop()







"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def preOrder2(root):
    s=[]
    if root == None: return None
    s.append(root)
    while len(s)>0:
        curr=s[-1]
        if curr.left and curr.right:
            print curr.data,
            s.pop()
            s.append(curr.right)
            s.append(curr.left)

        elif curr.left and not curr.right:
            print curr.data,
            s.pop()
            s.append(curr.left)
        elif curr.right and not curr.left:
            print curr.data,
            s.pop()
            s.append(curr.right)
        else:
            print curr.data,
            s.pop()

def preOrder(root):
    if root == None: return
    print root.data,
    preOrder(root.left)
    preOrder(root.right)
