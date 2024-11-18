class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# 使用示例
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)  # 输出: [1, 2, 3]
    print(stack.pop())  # 输出: 3
    print(stack.peek())  # 输出: 2
    print(stack.size())  # 输出: 2
    print(stack.is_empty())  # 输出: False
