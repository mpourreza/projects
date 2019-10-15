# Stack implementation in Python 3

class Stack():
    def __init__(self):
        self.items = []

    # Add to the stack
    def Push(self, item):
        self.items.append(item)

    # Remove the last element from the stack
    def Pop(self):
        return self.items.pop() if len(self.items) > 0 else None

    # Return the last element
    def Top(self):
        return self.items[-1] if len(self.items) > 0 else None

    def IsEmpty(self):
        return True if len(self.items) == 0 else False
