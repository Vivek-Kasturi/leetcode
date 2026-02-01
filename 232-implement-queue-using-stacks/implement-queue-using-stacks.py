class MyQueue:

    def __init__(self):
        self.stack = []      # just one stack for brute force

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        # brute force: rebuild queue order every time
        temp = []
        while self.stack:
            temp.append(self.stack.pop())

        front = temp.pop()   # this is the queue front

        # rebuild original order
        while temp:
            self.stack.append(temp.pop())

        return front

    def peek(self) -> int:
        temp = []
        while self.stack:
            temp.append(self.stack.pop())

        front = temp[-1]     # peek without removing

        while temp:
            self.stack.append(temp.pop())

        return front

    def empty(self) -> bool:
        return len(self.stack) == 0
