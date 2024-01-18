class Cqueue:
    def __init__(self , size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def insqueue(self , item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def delqueue(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = self.raer = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return item
        
    def display(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.rear >= self.front:
            for i in range (self.front , self.rear +1):
                print(self.queue[i] , end=" ")
        else:
            for i in range (self.front , self.size):
                print(self.queue[i] , end=" ")
            for i in range (0 , self.rear + 1):
                print(self.queue[i] , end=" ")
        print()

    def sort_and_store_in_doubly_linked_list(self):
        sorted_list = list(sorted(self.queue, reverse=True))

        linked_list = Dlinkedlist()

        for item in sorted_list:
            linked_list.addinstart(item)

        return linked_list

class Dnode:

    def __init__(self , data):
        self.data = data
        self.next = None
        self.prev = None

class Dlinkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        while (t):
            print(t.data , end="<-->")
            t = t.next
        print()

    def addinstart(self , data):
        n = Dnode(data)
        if self.head == None:
            self.head = n
            return 
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n

    def addinend(self , data):
        n = Dnode(data)
        if self.head != None :
            t = self.head
            while (t.next != None):
                t = t.next
            t.next = n
            n.prev = t
        else:
            self.head = n

    def addafter(self , m , data):
        n = Dnode(data)
        t = self.head
        while (t.data != m):
            t = t.next
        n.next = t.next
        n.prev = t
        t.next = n
        n.next.prev = n


    def delfirst(self):
        if (self.head == None):
            return False
        self.head = self.head.next
        self.head.prev = None

    def dellast(self):
        if (self.head == None):
            return -1
        t = self.head
        while (t.next != None):
            t = t.next
        t.prev.next = None
        t.prev = None

    def delafter(self , d):
        t = self.head
        while (t.data != d):
            t = t.next
        t.next.prev = t.prev
        t.prev.next = t.next
        t.next = None
        t.prev = None


my_queue = Cqueue(5)

my_queue.insqueue(1)
my_queue.insqueue(12)
my_queue.insqueue(0)
my_queue.insqueue(-1)
my_queue.insqueue(8)

my_queue.display()
my_queue.delqueue()
my_queue.insqueue(9)
my_queue.display()

linked_list1 = Dlinkedlist()
linked_list1.addinstart(18)
linked_list1.addinend(20)
linked_list1.addafter(18 , 70)
linked_list1.display()


linked_list = my_queue.sort_and_store_in_doubly_linked_list()

linked_list.display()

