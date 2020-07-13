"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   # With array you have to pass the index of the item (0) to dequeue/remove and with LinkedList you remove its head
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import LinkedList
from stack import Stack
class Queue:
    # def __init__(self):
    #     self.size = 0
    #     self.storage = []
    
    # def __len__(self):
    #     return self.size

    # def enqueue(self, value):
    #     self.storage.append(value)
    #     self.size += 1

    # def dequeue(self):
    #     if self.storage:
    #         self.size -= 1
    #         return self.storage.pop(0)
        
    #     return None

# --------------------------------------

    # def __init__(self):
    #     self.size = 0
    #     self.storage = LinkedList()
    
    # def __len__(self):
    #     return self.size

    # def enqueue(self, value):
    #     self.storage.add_to_tail(value)
    #     self.size += 1

    # def dequeue(self):
    #     if self.storage.head:
    #         self.size -= 1
    #         return self.storage.remove_head()
        
    #     return None

# --------------------------------------
# STRETCH
    def __init__(self):
        self.size = 0
        self.stack_in = Stack()
        self.stack_out = Stack()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        for _ in range(self.stack_out.size):
            self.stack_in.push(self.stack_out.pop())

        self.stack_in.push(value)
        self.size += 1

    def dequeue(self):
        if self.size:
            for _ in range(self.stack_out.size):
                self.stack_in.push(self.stack_out.pop())

            while (self.stack_in.size > 0):
                self.stack_out.push(self.stack_in.pop())
            
            self.size -= 1
            return self.stack_out.pop()

        return None
        
        