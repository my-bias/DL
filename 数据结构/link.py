"""
链表是由一系列节点组成的元素集合。
每个节点包含两部分，数据域item和指向下一个节点的指针next。
通过节点之间的相互连接最终串联成一个链表。
"""


class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


def create_link_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


def create_link_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_link(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next





# 链表返回的是heat, 所以这里的heat代表链表
def findNode(head, key):
    p = head
    while p != None:
        if p.item == key:
            return p
        p = p.next
    return None
# curNode = findNode(lk, 4)
# print(curNode.item)

def insert_link(lk,key,element):
    node = Node(element)
    curNode = findNode(lk,key)
    node.next = curNode.next
    curNode.next = node
    return lk


# new_lk = insert_link(lk,5, 7)
# print_link(new_lk)

# 单链表实现困难
def remove_link(lk, key):
    curNode = findNode(lk,key)


lk = create_link_tail([1, 2, 3, 4, 5, 6])
# new_lk = insert_link(lk,5, 7)
# print_link(new_lk)