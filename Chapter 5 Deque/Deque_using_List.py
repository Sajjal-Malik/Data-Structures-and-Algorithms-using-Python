class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert_front(self, data):
        self.items.insert(0, data)

    def insert_rear(self, data):
        self.items.append(data)

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        else:
            self.items.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        else:
            self.items.pop()

    def get_front(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        else:
            return self.items[0]

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Empty Deque")
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

    def printDeque(self):
        for item in self.items:
            print(item, end=" ")
        print()


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
