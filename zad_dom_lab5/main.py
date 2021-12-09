from typing import *
from collections import deque


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'
    parent: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        if self.right_child is None and self.left_child is None:
            return True
        return False

    def add_left_child(self, child):
        self.left_child = child
        self.left_child.parent = self

    def add_right_child(self, child):
        self.right_child = child
        self.right_child.parent = self

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        print(self.value)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)
        print(self.value)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        print(self.value)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def get_level(self) -> int:
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


class BinaryTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode):
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)


def all_paths(tree: BinaryTree) -> List[List[BinaryNode]]:
    root = tree.root
    lista = []
    path = []
    stack = deque()

    stack.append((root, path))
    if root is None:
        raise ValueError("root can't be None")
    while stack:
        node, path = stack.pop()
        path.append(node.value)
        if node.is_leaf():
            lista.append(list(path))
        if node.right_child:
            stack.append((node.right_child, list(path)))
        if node.left_child:
            stack.append((node.left_child, list(path)))
    return lista


n1 = BinaryNode(1)
n2 = BinaryNode(2)
n3 = BinaryNode(3)
n4 = BinaryNode(4)
n5 = BinaryNode(5)
n7 = BinaryNode(7)
n8 = BinaryNode(8)
n9 = BinaryNode(9)

n1.add_left_child(n2)
n1.add_right_child(n3)
n3.add_right_child(n7)
n2.add_right_child(n5)
n2.add_left_child(n4)
n4.add_right_child(n9)
n4.add_left_child(n8)

drzewo = BinaryTree(n1)
print(all_paths(drzewo))
