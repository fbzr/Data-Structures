"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import queue
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                #insert to left
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        else:
            if self.right:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)
        
        fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        
        print(node.value)

        if node.right:
            self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal


    def bft_print(self, node):
        nodes = queue.Queue(0)
        nodes.put(node)
        
        while not nodes.empty():
            current = nodes.get()
            print(current.value)
            if current.left:
                nodes.put(current.left)
            if current.right:
                nodes.put(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        nodes = queue.LifoQueue()
        
        nodes.put(node)

        while not nodes.empty():
            current = nodes.get()
            print(current.value)
            if current.right:
                nodes.put(current.right)
            if current.left:
                nodes.put(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left:
            self.in_order_print(node.left)

        if node.right:
            self.in_order_print(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.in_order_print(node.left)

        if node.right:
            self.in_order_print(node.right)
        
        print(node.value)
