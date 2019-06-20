class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class Doubly_LinkedList(object):

    def append(item):
        new_node = Node(item)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        
    def prepend():
        new_node = Node(item)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def find():
        pass

    def delete():
        pass