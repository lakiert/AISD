from typing import *


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.right_child is None and self.left_child is None:
            return True
        return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    # def traverse_in_order(self):
    #     if self.left_child is not None:
    #         type(self).traverse_in_order(self.left_child)
    #     print(self.value)
    #     if self.right_child is not None:
    #         type(self).traverse_in_order(self.right_child)

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


class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        pass


# tree = BinaryTree(10)
# tree.root.add_right_child(2)
# tree.root.add_left_child(5)
# tree.root.left_child.add_left_child(1)
# assert tree.root.value == 10
#
# assert tree.root.right_child.value == 2
# tree.root.right_child.add_left_child(10)
# assert tree.root.right_child.is_leaf() is False
#
# assert tree.root.left_child.left_child.value == 1
# assert tree.root.left_child.left_child.is_leaf() is True


n10 = BinaryNode(10)
n9 = BinaryNode(9)
n2 = BinaryNode(2)
n1 = BinaryNode(1)
n3 = BinaryNode(3)
n4 = BinaryNode(4)
n6 = BinaryNode(6)

n10.left_child = n9
n10.right_child = n2
n9.left_child = n1
n9.right_child = n3
n2.left_child = n4
n2.right_child = n6

n10.traverse_in_order(BinaryNode)
print(" ")
n10.traverse_post_order(BinaryNode)
print(" ")
n10.traverse_pre_order(BinaryNode)