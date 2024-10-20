class Stack(list):
    def is_empty(self):
        return len(self) == 0

    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Empty Stack")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Empty Stack")

    def size(self):
        return len(self)

    def printStack(self):
        for item in self:
            print(item, end=" ")
        print()

    def insert(self, index, data):  # method overridden
        raise AttributeError("No Attribute 'insert()' in Stack")


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
# s1.insert(0,10)  // throws the exception
