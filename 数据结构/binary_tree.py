class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BinaryTreeNode('A')
b = BinaryTreeNode('B')
c = BinaryTreeNode('C')
d = BinaryTreeNode('D')
e = BinaryTreeNode('E')
f = BinaryTreeNode('F')
g = BinaryTreeNode('G')

e.lchild = a
a.rchild = c
c.lchild = b
c.rchild = d
e.rchild = g
g.rchild = f

root = e

def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)


def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)


def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')

post_order(root)