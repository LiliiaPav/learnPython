class Node(object):
    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n # pointer to next node
        self.prev = p # previous node
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_prev(self):
        return self.prev
    def set_prev(self, p):
        self.prev = p
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d

class LinkedList(object):
    def __init__(self, r=None):
        self.root=r
        self.size=0
    def get_size(self):
        return self.size
    def add(self, d):
        new_node=Node(d, self.root)
        if self.root:
            self.root.set_prev(new_node)
        self.root=new_node
        self.size+=1
    def remove(self, d):
        curr_node=self.root

        while curr_node:
            if curr_node.get_data()== d:
                next = curr_node.get_next()
                prev= curr_node.get_prev()
                if next:
                    next.set_prev(prev)
                if prev:
                    prev.set_next(next)
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