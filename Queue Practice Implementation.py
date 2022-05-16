"""
Following the queue implementation from
*    Title: Problem Solving with Algorithms and Data Structures Using Python
*    Author: Miller, Bradley and Ranum, David
*    Date: 2011
"""

class Queue:
    def __init__(self):
        # Creates an empty list representing the contents of the queue
        # Index 0 will be the back of the queue and the last index will be the front
        self.items = []

    def isEmpty(self):
        # Returns true if the queue has no items and false otherwise
        return self.items == []

    def enqueue(self, item):
        # Adds the new item to the back of the queue (index 0)
        self.items.insert(0, item)

    def dequeue(self):
        # Returns the item at the front of the queue and removes it 
        return self.items.pop()

    def size(self):
        return len(self.items)