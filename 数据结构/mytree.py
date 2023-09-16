class Node:
    def __init__(self, name, type="dir"):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree:
    def __init__(self):
        self.root = Node('/')
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != '/':
            name += '/'
        for child in self.now.children:
            if child == name:
                self.now = child


dir = FileSystemTree()
dir.mkdir('bin/')
dir.mkdir('root/')
dir.mkdir('user/')
print(dir.ls())
