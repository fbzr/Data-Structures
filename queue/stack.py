"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

    # With array you have to pass the index of the item (its length - 1) to pop/remove and with LinkedList you remove its tail
    #Linked list avoids contiguous memory
"""

from singly_linked_list import LinkedList
class Stack:
    # def __init__(self):
    #     self.size = 0
    #     self.storage = []

    # def __len__(self):
    #     return len(self.storage)

    # def push(self, value):
    #     self.storage.append(value)
    #     self.size = len(self.storage)

    # def pop(self):
    #     if self.storage:
    #         self.size = len(self.storage) - 1
    #         return self.storage.pop(self.size)

    #     return None

    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.storage.head:
            self.size -= 1
            return self.storage.remove_tail()

        return None