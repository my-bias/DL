"""
队尾（rear）：只能从队尾添加元素，一般叫作enQueue，入队
队头（front）：只能从队头移除元素，一般叫作deQueue，出队
先进先出的原则、First In Fist Out（跟栈是反的，栈是后进先出）
"""


# 环形队列
# 队空: rear = front
# 队满: rear + 1 = front
class myQueue:
    def __init__(self, size=100):
        self.size = size
        self.myqueue = [0 for _ in range(size)]
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def __len__(self):
        return (self.rear - self.front + self.size) % self.size

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return self.rear + 1 == self.front

    def append(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.myqueue[self.rear] = element
        else:
            raise IndexError("Queue is filled")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.myqueue[self.front]
        else:
            raise IndexError("Queue is empty")


# 广度优先搜索
# 思路:从一个节点开始,寻找所有接下来能继续走的点,继续不断寻找,直到找到出口。
# 使用队列存储当前正在考虑的节点

from collections import deque
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x - 1, y),
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1),
]


def print_r(path):
    curNode = path[-1]
    real_path = []
    while curNode[2] != -1:
        real_path.append(curNode[0:2])
        curNode = path[curNode[2]]
    real_path.append(curNode[0:2])
    real_path.reverse()
    print(real_path)


def maze_path(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:
        curNode = queue.pop()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            break
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))
                maze[nextNode[0]][nextNode[1]] = 2
    else:
        print("no way to destination")
        return False


maze_path(1, 1, 8, 8)
