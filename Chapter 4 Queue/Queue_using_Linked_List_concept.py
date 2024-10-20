class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front == None or self.rear == None

    def enqueue(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:

            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        else:
            return self.front.item

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        else:
            return self.rear.item

    def size(self):
        return self.item_count


# driver code
q1 = Queue()
# try:
#     q1.get_front()
# except IndexError as e:
#     print(e.args[0])

q1.enqueue(2)
q1.enqueue(22)
q1.enqueue(9)
q1.enqueue(25)
q1.enqueue(7)
print("Front value is ->", q1.get_front())
print("Rear value is ->", q1.get_rear())
print("Size of the queue is ->", q1.size())
