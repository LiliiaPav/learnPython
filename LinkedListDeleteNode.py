"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Delete(head, position):
    if position==0:
        head=head.next
        return head
    else:
        prev=head
        currN=head.next
        nextNode=currN.next
        i=1
        while i<= position:
            if i==position:
                prev.next=nextNode
                return head
            i+=1
            prev=currN
            currN=currN.next
            nextNode=currN.next
            nextNode=currN.next