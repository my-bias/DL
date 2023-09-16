class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prior = None


def create_link_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head.prior = node
        head = node
    return head


def create_link_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        node.prior = tail
        tail = node
    return head


def print_link(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


def findNode(head, key):
    p = head
    while p != None:
        if p.item == key:
            return p
        p = p.next
    return None


def insert_link(lk, lift_key, element):
    node = Node(element)
    curNode = findNode(lk, lift_key)
    node.next = curNode.next
    curNode.next.prior = node
    curNode.next = node
    node.prior = curNode
    curNode.next = node
    return lk


def remove_link(lk, element):
    p = findNode(lk, element)
    p.prior.next = p.next
    p.next.prior = p.prior
    del p
    return lk


lk = create_link_tail([1, 2, 3, 4, 5, 6])
new_lk = remove_link(lk, 5)
print_link(new_lk)
