class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def insert_front(self, data):
        n = Node(None, data, self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1

    def insert_rear(self, data):
        n = Node(self.rear, data, None)
        if self.is_empty():
            self.rear = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count += 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        else:
            return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        else:
            return self.rear.item

    def size(self):
        return self.item_count
    
    def printDeque(self):
        temp = self.front
        while temp != self.rear:
            print(temp.item, end=" ")
            temp = temp.next
        print(temp.item)


# driver code
d1 = Deque()
d1.insert_front(10)
d1.insert_front(140)
d1.insert_front(1000)
d1.insert_rear(50)
d1.insert_rear(90)
d1.insert_rear(909)
d1.printDeque()
print("front ->", d1.get_front())
print("rear ->", d1.get_rear())
print("size ->", d1.size())
