#!python

from linkedlist import LinkedList

class ArrayDeque(object):

    def __init__(self, iterable=None):
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push_front(item)

    def is_empty(self):
        return len(self.list) == 0
    
    def length(self):
        return len(self.list)
    
    def push_front(self):
        return self.list.insert(0, item)
    
    def push_back(self):
        return self.list.append(item)

    def pop_front(self):
        if self.list.is_empty():
            raise ValueError("The list is empty, cant remove item")
        return self.list.pop(0)
    
    def pop_back(self):
        if self.list.is_empty():
            raise ValueError("The list is empty, cant remove item")
        return self.list.pop()