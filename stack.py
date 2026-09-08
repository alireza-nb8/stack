
class Stack:
    def __init__(self,input):
        self.name  = input
        self.list = []

    def push(self,x):
        self.list.append(x)

    def pop(self):
        last_index = self.list[-1]
        del self.list[-1]
        return last_index