from SingleLinkedList.Node import Node


class singlylinkedlist:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def length(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

        """Insertion after the point"""

    def insertion_at_any_point(self, data, pos):
        if pos > self.length():
            return "length out of index"
        else:
            count = 0
            new_node = Node(data)
            node = self.head
            while count < pos - 1:
                count += 1
                node = node.next
        new_node.next = node.next
        node.next = new_node

        """Insertion before the point"""

    def insertion_before_point(self, pos, data):
        if pos > self.length():
            return "length out of index"
        else:
            count = 0
            node = self.head
            new_node = Node(data)
            while count < pos - 1:
                count += 1
                prev = node
                node = node.next
            prev.next = new_node
            new_node.next = node

    ''' Deletion after the point'''

    def deletion_at_anypoint_after(self, pos):
        if pos > self.length():
            return "please enter a proper location"
        else:
            node = self.head
            count = 0
            while count < pos - 1:
                count += 1
                prev = node
                node = node.next
            node.next = node.next.next

    ''' Deletion before the point'''

    def deletion_at_anypoint_before(self, pos):
        if pos > self.length():
            return "please enter a proper location"
        else:
            node = self.head
            count = 0
            while count < pos - 1:
                count += 1
                prev = node
                node = node.next
            prev.next = node.next

    '''Head node deletion'''

    def head_node_deletion(self):
        self.head=self.head.next

    '''Tail node deletion'''

    def tail_node_deletion(self):
        node=self.head
        while node.next:
            prev=node
            node=node.next
        prev.next=None
    '''Entire linkedlist deletion '''

    def entire_deletion(self):
        self.head = None

    def traverse(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


if __name__ == '__main__':
    sl = singlylinkedlist()
    for i in range(5):
        sl.append(i)
    sl.insertion_at_any_point(44, 2)
    sl.insertion_before_point(2, 33)
    sl.deletion_at_anypoint_after(2)
    sl.deletion_at_anypoint_before(2)
    sl.tail_node_deletion()
    sl.head_node_deletion()
    sl.traverse()

