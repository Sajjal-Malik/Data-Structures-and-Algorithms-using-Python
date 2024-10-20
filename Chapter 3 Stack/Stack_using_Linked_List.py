from Singly_Linked_List import *


class Stack:
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.mylist.is_empty()

    def push(self, data):
        self.mylist.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count -= 1

    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item

    def size(self):
        return self.item_count

    def printStack(self):
        for item in self.mylist:
            print(mylist.start.item, end=" ")
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
