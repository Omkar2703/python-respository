#Craeting LinkedList with three nodes
class Node: #Here we create a node structure
    def __init__(self, data):
        self.data = data
        self.next = None
class LL: #This class contains linkedlist Functions
    def __init__(self):
        self.head = None
    def display(self):
        temp = list.head
        while(temp):
            print(temp.data)
            temp = temp.next
list = LL()
list.head = Node(1)
second = Node(2)
third = Node(3)

#linking

list.head.next = second
second.next = third
third.next = None

list.display()