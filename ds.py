class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        return None

    def push_list(self, list):
        for i in list:
            self.push(i)
        return None

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[self.size() - 1]

    def stackToList(self):
        """
        返回栈底到栈顶的所有元素
        """
        return self.stack
