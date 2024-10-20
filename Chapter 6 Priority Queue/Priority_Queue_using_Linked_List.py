class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next


class PrioriyQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def push(self, data, priority):
        n = Node(data, priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty Priority Queue")
        data = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return data

    def size(self):
        return self.item_count


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
