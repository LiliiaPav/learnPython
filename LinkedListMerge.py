"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def MergeLists(headA, headB):
    head=Node()
    nextN=Node()
    if headA==None and headB==None:
        return None
    if headA==None and headB!=None:
        head=headB
        head.next=headB.next
        return head
    elif headB==None and headA!=None:
        head=headA
        head.next=headA.next
        return head
    elif headA.data>headB.data:
        head=headB
        head.next=nextN
    elif headA.data<headB.data:
        head=headA
        head.next=nextN

    return head