class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        prev = None # initial state of prev is none.
        node = self.head 
        
        #if we are reversing a ll that means the add to head function has already been called. and if that is the case self.head has the attributes of the Node class. that includes next_node and value. 

        while node: 
            next_node = node.next_node
            node.next_node = prev
            prev = node
            node = next_node
        self.head = prev
