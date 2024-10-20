class PrioriyQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data, priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index, (data, priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty Priority Queue")
        return self.items.pop(0)[0]

    def size(self):
        return len(self.items)


# driver code
pq1 = PrioriyQueue()
pq1.push(23, 4)
pq1.push(12, 7)
pq1.push(42, 1)
pq1.push(62, 9)
pq1.push(70, 6)
print("size before pop() ->", pq1.size())

print("Printing all elements of priority queue...")
while not pq1.is_empty():
    print(pq1.pop(), end=" ")
print()

print("size after pop() ->", pq1.size())
