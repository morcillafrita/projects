"""
Following the stack implementation from
*    Title: Problem Solving with Algorithms and Data Structures Using Python
*    Author: Miller, Bradley and Ranum, David
*    Date: 2011
"""

class Stack:
    # Creates a new stack object with an empty list
    # The list will hold the contents of the stack with the first element being the "bottom"
    def __init__(self):
        self.items = []

    def isEmpty(self):
        # Returns true if stack is empty, false otherwise
        return self.items == []

    def push(self, item):
        # Adds a new item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Returns item from the top of the stack and removes it from the stack
        return self.items.pop()

    def peek(self):
        # Returns the item at the top of the stack, but does not remove it
        return self.items[len(self.items) - 1]
    
    def size(self):
        # Returns the number of items in the stack
        return len(self.items)