from typing import *

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        for child in self.children:
            self.for_each_deep_first(visit(child))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        fifo = self.children
        while len(fifo):
            visit(fifo[0])
            print(fifo[0])
            fifo += fifo[0].children
            del fifo[0]

    def printing(self):
        print(self.value)

    def printing_branch(self):
        print(self.value)
        for x in self.children:
            print(x.value)


a = TreeNode("A")
b = TreeNode("B")
b2 = TreeNode("B2")
b3 = TreeNode("B3")
c = TreeNode("C")
a.add(b)
a.add(b2)
a.add(b3)
b.add(c)

# a.printing()
# a.printing_branch()
# b.printing_branch()
#
# print(a.is_leaf())
# print(c.is_leaf())
