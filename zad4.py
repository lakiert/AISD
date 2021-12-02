from typing import *

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def __str__(self):
        return self.value

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        child.parent = self
        self.children.append(child)

    def for_each_deep_first(self) -> None:
        
        for child in self.children:
            type(self).for_each_deep_first(child)

    def for_each_level_order(self) -> None:
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

    # def search(self, value:any) -> Union['TreeNode', None]:
    #     if self.value == value:
    #         return self
    #
    #     for child in self.children:
    #         x = child.search(value)
    #         if x =

    def printing(self):
        print(self.value)

    def printing_children(self):
        print(self.value)
        for x in self.children:
            print(x.value)



class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    def add(self, value:Any, parent:Any):
        parent.children.append(TreeNode(value))

    def show(self):
        spaces = ' '
        prefix = '-'

        if type(self) is Tree:
            print(self.root.value)
            for child in self.root.children:
                print(spaces * child.get_level()*3 + prefix + child.value)
                Tree.show(child)
        if type(self) is TreeNode:
            for child in self.children:
                print(spaces * child.get_level()*3 + prefix + child.value)
                Tree.show(child)


food = TreeNode("food")
fruits = TreeNode("fruits")
vegetables = TreeNode("vegetables")
dairy = TreeNode("dairy")
citrus = TreeNode("citrus")
berries = TreeNode("berries")
leafy = TreeNode("leafy")
roots = TreeNode("roots")
milk = TreeNode("milk")
cheese = TreeNode("cheese")
cheese_white = TreeNode("cheese_white")
cheese_yellow = TreeNode("cheese_yellow")

food.add(vegetables)
food.add(fruits)
food.add(dairy)
fruits.add(citrus)
fruits.add(berries)
vegetables.add(leafy)
vegetables.add(roots)
dairy.add(milk)
dairy.add(cheese)
cheese.add(cheese_white)
cheese.add(cheese_yellow)

# food.printing()
# print(" ")
# food.printing_children()
# print(" ")
# fruits.printing_children()
# print(" ")
#
# print(food.is_leaf())
# print(citrus.is_leaf())
#
food.print_tree()
#
# food.for_each_deep_first()

tree = Tree(food)
tree.show()

