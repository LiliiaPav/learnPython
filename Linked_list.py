class Node(object):
    def __init__(self, d, n=None):
        self.data=d
        self.next_node=n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node=n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data=d
    def __str__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self, r=None):
        self.root=r
        self.size=0
    def get_size(self):
        return self.size
    def add(self, d):
        new_node=Node(d, self.root)
        self.root=new_node
        self.size+=1
    def remove(self, d):
        curr_node=self.root
        prev_node=None
        while curr_node:
            if curr_node.get_data()== d:
                if prev_node:
                    prev_node.set_next(curr_node.get_next)
                else:
                    self.root=curr_node
                self.size-=1
                return True #date removed
            else:
                prev_node=curr_node
                curr_node=curr_node.get_next()
        return False
    def find(self, d):
        curr_node=self.root
        while curr_node:
            if curr_node.get_data()== d:
                return d
            else:
                curr_node=curr_node.get_next()
        return None



myList=LinkedList()
myList.add(5)
myList.add(7)
myList.add(9)
myList.add(8)

print(myList.find(8))
print(myList.remove(9))