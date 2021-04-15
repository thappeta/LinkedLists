from DoublyLinkedlist.Node import Node


class Linkedlist:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.prev = None
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node.prev = node
            node.next = new_node
            new_node.next=None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev=None

    def insertion_at_anypoint_after(self, pos, data):
        count = 0
        new_node=Node(data)
        node=self.head
        while count<pos-1:
            node=node.next
            count+=1
        next=node.next
        node.next=new_node
        new_node.next=next
        new_node.prev=node
        next.prev=new_node

    def insertion_at_anypoint_before(self,pos,data):
        count=0
        new_node=Node(data)
        node=self.head
        while count<pos-1:
            node=node.next
            count +=1
        prev=node.prev
        prev.next=new_node
        node.prev=new_node
        new_node.next=node
        new_node.prev=prev


    def traverse(self):
        node = self.head
        while node:
            print(node.data,"-->",end="")
            node = node.next


if __name__ == "__main__":
    ll = Linkedlist()
    for i in range(5, 11):
        ll.prepend(i)
    ll.insertion_at_anypoint_after(2, 22)
    ll.insertion_at_anypoint_before(2,22)
    ll.traverse()
