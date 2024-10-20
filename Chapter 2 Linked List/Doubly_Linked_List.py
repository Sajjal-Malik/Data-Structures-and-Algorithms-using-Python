""" Doubly Linked List """


class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        temp = self.start
        if temp != None:
            while temp.next != None:
                temp = temp.next
        n = Node(temp, data, None)
        if temp == None:
            self.start = n
        else:
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n
        else:
            self.start = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" -> ")
            temp = temp.next
        print("None")

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.prev = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next

    # must define method if making the class iterable
    def __iter__(self):
        return SLLIterator(self.start)


# This class will allow us to run for loop over our SLL class
class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# driver code
mylist = DLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_start(15)
mylist.insert_at_last(79)
mylist.insert_at_last(69)
mylist.insert_after(mylist.search(10), 30)
mylist.insert_after(mylist.search(15), 45)
mylist.insert_after(mylist.search(79), 55)
mylist.insert_after(mylist.search(10), 87)
mylist.insert_at_last(99)
mylist.print_list()

print("Start Node ->", mylist.start.item)

mylist.delete_first()
mylist.print_list()
print("Start Node ->", mylist.start.item)

mylist.delete_last()
mylist.print_list()

mylist.delete_item(30)
mylist.print_list()

print("Start Node ->", mylist.start.item)

# for loop is runnin successfully becasue we have made our SLL class iterable by defining iterator
print("The remaining value of the Linked List printed using Iterator: ")
for value in mylist:
    print(value, end=" -> ")
print("None")
