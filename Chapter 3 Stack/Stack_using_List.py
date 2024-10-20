class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        return self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Empty Stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Empty Stack")

    def size(self):
        return len(self.items)

    def printStack(self):
        for item in self.items:
            print(item, end=" ")
        print()


# driver code
s1 = Stack()
s1.push(10)
s1.push(40)
s1.push(78)
s1.push(56)
s1.push(90)
s1.push(99)
s1.printStack()

s1.pop()
s1.printStack()

print("The top element of the stack is:", s1.peek())
print("The size of the stack is:", s1.size())
print("Is stack empty?", s1.is_empty())
