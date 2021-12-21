from typing import *


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child: BinaryNode = None
        self.right_child: BinaryNode = None

    def is_leaf(self):
        if self.right_child is None and self.left_child is None:
            return True
        return False

    def min(self):
        while self.left_child:
            self = self.left_child
        return self.value


class BinarySearchTree:
    root: BinaryNode = None

    def __init__(self):
        self.root: BinaryNode

    def insert(self, value):
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left_child is None:
                node.left_child = BinaryNode(value)
            else:
                self._insert(value, node.left_child)
        elif value > node.value:
            if node.right_child is None:
                node.right_child = BinaryNode(value)
            else:
                self._insert(value, node.right_child)
        else:
            print("already exists!")

    def show(self):
        if self.root:
            self._show(self.root)

    def _show(self, node):
        if node:
            self._show(node.left_child)
            print(str(node.value))
            self._show(node.right_child)

    def contains(self, value) -> bool:
        if self.root:
            return self._contains(value, self.root)
        else:
            return None

    def _contains(self, value, node):
        if value == node.value:
            return True
        elif value < node.value and node.left_child:
            return self._contains(value, node.left_child)
        elif value > node.value and node.right_child:
            return self._contains(value, node.right_child)
        else:
            return False


tree = BinarySearchTree()
tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(10)
tree.insert(14)
tree.insert(13)

tree.show()

print(" ")

print(tree.contains(8))
print(tree.contains(3))
print(tree.contains(99))
print(tree.contains(999))

print(tree.root.min())
print(tree.root.left_child.right_child.min())

