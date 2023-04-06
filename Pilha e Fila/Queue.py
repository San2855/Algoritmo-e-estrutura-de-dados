class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
      
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.size())
