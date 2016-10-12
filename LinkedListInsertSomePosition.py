"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    currNode= Node(data, None)
    temp=head
    if head == None:
        head = currNode
        return head
    if position == 0:
        currNode.next=head
        head = currNode
        return head
    i=0
    while i < position:
        if i == position-1:
            currNode.next=temp.next
            temp.next=currNode
            return head
        if temp.next == None:
            return False
        temp=temp.next
        i+=1
