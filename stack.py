#stack class
class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, n):
        self.items.append(n)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

s = Stack()
s.push(10)
s.push('Rohan')
s.push(20)
print(s.items)

s.pop()
print(s.items)
