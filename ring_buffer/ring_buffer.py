

from doubly_linked_list import DoublyLinkedList


#looking back on this i may have been able to do this with just a singly linked list? I've not needed to work with prev props. 
class RingBuffer:

    def __init__(self, capacity):
        self.capacity = capacity
        self.currentNode = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity: 
            # ^ checking that new entry will not push storage to grow larger than the set limit. This code block determines what will happen if new node is within the predetermined limit.
            self.storage.add_to_tail(item) # item is added to the tail and then set as the currentNode on next line
            self.currentNode = self.storage.tail
        
        elif self.storage.length == self.capacity:
            # elif is telling python whay to do if the storage is currently at it's limit. 
            
            if not self.currentNode.next: 
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.currentNode = self.storage.head

            else:
                self.currentNode.next.delete()
                self.currentNode.insert_after(item)
                self.currentNode = self.currentNode.next

    def get(self):
        list_contents = []
        
        currentNode = self.storage.head
        
        while currentNode:
            list_contents.append(currentNode.value)
            currentNode = currentNode.next
        
        return list_contents

        
