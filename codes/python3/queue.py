# Queue implementation in Python 3

class Queue():
    def __init__(self):
        self.items = []

    def Enqueue(self, item):
        self.items.append(item)

    def Dequeue(self):
        return self.items.pop(0) if len(self.items) > 0 else None
