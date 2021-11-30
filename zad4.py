from typing import *

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        child.parent = self
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

    def get_level(self) -> int:
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        if self.parent:
            prefix = '-'
        else:
            prefix = ''
        print(spaces + prefix + self.value)
        if self.children:
            for child in self.children:
                child.print_tree()

    def printing(self):
        print(self.value)

    def printing_branch(self):
        print(self.value)
        for x in self.children:
            print(x.value)

    # def search(self, value:any) -> Union['TreeNode', None]:
    #     if self.value == value:
    #         return self
    #
    #     for child in self.children:
    #         x = child.search(value)
    #         if x =


food = TreeNode("food")
fruits = TreeNode("fruits")
vegetables = TreeNode("vegetables")
dairy = TreeNode("dairy")
citrus = TreeNode("citrus")
food.add(vegetables)
food.add(fruits)
food.add(dairy)
fruits.add(citrus)

# food.printing()
# print(" ")
# food.printing_branch()
# print(" ")
# fruits.printing_branch()
# print(" ")
#
#
# print(food.is_leaf())
# print(citrus.is_leaf())

food.print_tree()
