class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[len(self.queue)-1]

    def size(self):
        return len(self.queue)
    
    def rotate(self, count):
        for _ in range(count):
            item = self.dequeue()
            self.enqueue(item)
        return self.queue
