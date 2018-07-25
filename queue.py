#Queue class 

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, n):
        self.items.insert(0, n)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue('ram')
q.enqueue(10)
q.enqueue(4.5)
print(q.items)
q.dequeue()
print(q.items)
print(q.size())
print(q.isEmpty())
