"""
栈是限定仅在表尾进行插入和删除操作的线性表，栈又称为先进后出
（Last In First Out）的线性表，简称LIFO结构。
（栈就像一个杯子，我们只能在杯口（栈顶）向这个杯子里倒入水（进栈）或使其倒出水（出栈），
而不能在杯底（栈底）进行这些操作，而且我们喝水的时候不能直接喝底下的水，
只能先喝上面的水（出栈），才能去喝下面的水）
栈顶：允许插入和删除的一端称为栈顶。
栈底：不可以进行插入和删除操作。
空栈：不含任何数据元素的栈称为空栈。
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        return self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_pop(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None


# 栈---深度优先搜索(回溯法)
# 思路: 从一个节点开始, 任意找下一个能走的点, 当找不到能走的点时,退回上一个点寻找是否有其他方向的点。
# 使用栈存储当前的路径
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


def maze_path(x1, y1, x2, y2):
    global nextNode
    stack = []
    stack.append((x1, y1))
    while len(stack) > 0:
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[0]] = 2
                break
        else:
            maze[nextNode[0]][nextNode[0]] = 2
            stack.pop()
    else:
        return False