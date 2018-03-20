from mycolor import show

class Vector:
    def size(self):
        print('size func')

    def is_empty(self):
        print('is_empty func')


class OldStack(Vector):
    def push(self):
        print('OldStack push')

    def pop(self):
        print('OldStack pop')

old_stack = OldStack()
print(old_stack.size(), old_stack.is_empty(),
      old_stack.push(), old_stack.pop())

print('-------------改造开始-----------------')

class Stack:
    def __init__(self):
        self.vector = Vector()

    def size(self):
        self.vector.size()

    def is_empty(self):
        self.vector.is_empty()

    def push(self):
        print('Stack push')

    def pop(self):
        print('Stack pop')

stack = Stack()
print(stack.size(), stack.is_empty(),
      stack.push(), stack.pop())