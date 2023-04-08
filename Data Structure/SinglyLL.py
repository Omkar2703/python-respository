class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None
    def insert(self, ele):
        newrec = Node(ele)
        if(self.head):
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newrec
        else:
            self.head = newrec
    def delete(self, ele):
        temp = self.head
        if (temp != None):
            if (temp.data == ele):
                self.head = temp.next
                temp = None
                return
        while(temp != None):
            if temp.data == ele:
                break
            prev = temp
            temp = temp.next
        if(temp == None):
            return
        prev.next = temp.next
        temp = None
    def display(self):
        temp = self.head
        while(temp):
            print (" %d" %(temp.data)),
            temp = temp.next

list = LL()
while(True):
    print("\nMenu\n1. Insertion\n2. Deletion\n3. Display\n4. Exit\n")
    c = int(input("\nEnter the choice: "))
    if(c==4):
        print("\nExit satisfied")
    elif(c==1):
        n = int(input("\nNo. of Elements: "))            
        for i in range(0, n):
            ele = int(input("\nEnter the element: "))
        list.insert(ele)
    elif(c==2):
        ele = int(input("\nEnter the element to be deleted: "))
        list.delete(ele)
        print("%d is the element deleted", ele)
    elif(c==3):
        list.display()