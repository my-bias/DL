# 二叉树查找
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BTS:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    # 递归写法 传入根节点root
    def insert(self, node, val):
        if not node:  # node为空 代表找到要插入的节点
            node = BinaryTreeNode(val)
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BinaryTreeNode(val)
            return
        while True:
            if val > p.data:
                if p.rchild:
                    p = p.rchild
                # 循环到没有右孩子代表插入成功
                else:  # 没有右孩子
                    p.rchild = BinaryTreeNode(val)
                    p.rchild.parent = p
                    return
            elif val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BinaryTreeNode(val)
                    p.lchild.parent = p
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if val < node.data:
            return self.query(node.lchild, val)
        elif val > node.data:
            return self.query(node.rchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if val < p.data:
                p = p.lchild
            elif val > p.data:
                p = p.rchild
            else:
                return p

    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

    def __remove_node1(self, node):
        # 情况1:要删除的是叶子节点
        if not node.parent: # 是根节点
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
            node.parent = None
        elif node == node.parent.rchild:
            node.parent.rchild = None
            node.parent = None



    def __remove_node21(self, node):
        # 情况2.1:node只有一个左孩子
        if not node.parent: # 节点是根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.lchild.parent:  # 节点是左孩子
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:  # 节点是右孩子
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent




    def __remove_node22(self, node):
        # 情况2.2: node只有右节点
        if not node.parent: # 节点是根节点
            self.root = node.rchild
            node.rchild.parent = None
        elif node == node.lchild.parent:  # 节点是左孩子
            node.rchild.parent = node.parent
            node.parent.lchild = node.rchild
        else:   # 节点是右孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent



    def delete(self, val):
        # 先查找值为val的节点
        if self.root:
            node = self.query_no_rec(val)
        if not node:
            return False
        if not node.lchild and not node.rchild:
            self.__remove_node1(node)
        elif not node.rchild:
            self.__remove_node22(node)
        elif not node.lchild:
            self.__remove_node21(node)
        else:
            min_node = node.rchild
            while min_node:
                min_node = min_node.lchild
            node.data = min_node.data
            # 删除min_node
            if min_node.rchild:
                self.__remove_node22(min_node)
            else:
                self.__remove_node1(min_node)




li = [5, 1, 2, 7, 8, 6, 3, 4, 9, 0]
tree = BTS(li)
tree.in_order(tree.root)
print()
tree.delete(6)
tree.in_order(tree.root)
print()
tree.delete(9)
tree.in_order(tree.root)
print()