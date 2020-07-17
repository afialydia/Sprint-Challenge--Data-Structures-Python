#looking back on this i may have been able to do this with just a singly linked list? I've not needed to work with prev props. 

class RingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        list_contents = []
        
        currentNode = self.storage.head
        
        while currentNode:
            list_contents.append(currentNode.value)
            currentNode = currentNode.next
        
        return list_contents

