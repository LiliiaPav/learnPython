class Queue(object):
    """  Queues are a fundamental computer science data structure.
    A queue is basically like a line at Disneyland - you can add elements to a queue, and they maintain a specific order.
    When you want to get something off the end of a queue, you get the item that has been in there the longest
    (this is known as 'first-in-first-out', or FIFO)."""

    def __init__(self):
        """ initialize Queue """
        self.values = []

    def insert(self, elem):
        """inserts one element in your Queue"""
        self.values.append(elem)


    def remove(self):
        """removes (or 'pops') one element from your Queue and returns it. If the queue is empty, raises a ValueError."""
        try:
            return self.values.pop(0)
        except:
            raise ValueError('Queue is empty')

    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.values]) + '}'

queue = Queue()
queue.insert(5)
queue.insert(6)
print queue
queue.remove()
print queue





