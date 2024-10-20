class Queue:
    def __init__(self):
        self.items = []
        self.front = None
        self.rear = None

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue Underflow")

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")

    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow")

    def size(self):
        return len(self.items)

    def printQueue(self):
        for item in self.items:
            print(item, end=" ")
        print()


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
q1.printQueue()
print("Size of the queue is ->", q1.size())


q1.dequeue()
q1.dequeue()
print("Front value is ->", q1.get_front())
print("Rear value is ->", q1.get_rear())
q1.printQueue()
print("Size of the queue is ->", q1.size())
