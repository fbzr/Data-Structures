"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create new node
        new_node = ListNode(value)

        if self.length:
            # point new node's next to current head
            new_node.next = self.head
            # current head prev node points to new_node
            self.head.prev = new_node
        else:
            # if list was tail and head will point to same node
            self.tail = new_node

        # update head
        self.head = new_node
        # update length
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = None

        if self.length:
            # save value to be returned
            value = self.head.value
            
            if not self.head.next:
                self.tail = None

            # update head
            self.head = self.head.next
            
            if self.head:
                # point head prev to None
                self.head.prev = None

            self.length -= 1

        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create new node and point its prev node to current tail
        new_node = ListNode(value)

        if self.length:
            new_node.prev = self.tail
            self.tail.next = new_node
        else:
            # if list was tail and head will point to same node
            self.head = new_node
        
        self.tail = new_node
        # update length
        self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = None

        if self.length:
            # save value to be returned
            value = self.tail.value

            # check if there is only one element
            if not self.tail.prev:
                self.head = None

            # update tail
            self.tail = self.tail.prev

            if self.head:
                # point tail next to None
                self.head.next = None

            self.length -= 1

        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if not node is self.head:
            if node.prev:
                node.prev.next = node.next

            if node.next:
                node.next.prev = node.prev

            if node is self.tail:
                self.tail = node.prev

            node.prev = None
            node.next = self.head
            self.head.prev = node

            self.head = node

        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if not node is self.tail:
            if node.prev:
                node.prev.next = node.next

            if node.next:
                node.next.prev = node.prev

            if node is self.head:
                self.head = node.next

            node.next = None
            
            node.prev = self.tail
            self.tail.next = node

            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            if node is self.head:
                self.head = node.next
            if node is self.tail:
                self.tail = node.prev

            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        max_value = current.value if current else None

        while(current):
            if current.value > max_value:
                max_value = current.value

            current = current.next

        return max_value