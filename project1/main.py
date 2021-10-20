from typing import Any

class Node:
    def __init__(self, value=None): #przy tworzeniu node powstaje to:
        self.value = value      #dane zawarte w wezle
        self.next = None      #next wskazujace na nastepny wezel

class LinkedList():
    def __init__(self):       #podczas tworzenia listy: (lista sklada sie z wezlow)
        self.head = None    #tworzy obiekt node i nazwie go head

    def push_(self, value:Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value:Any) -> None:
        new_node = Node(value)
        if (self.head == None):
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node


    def node(self, at: int) -> Node:
        node = self.head
        for x in range(at):
            node = node.next
        return node.value


    # def insert(self, value: Any, after: Node) -> None:
    #     node = Node(value)
    #     node.next = after.next
    #     after.next = node

    # def pop(self) -> None:
    #     current = self.head
    #     while(current.next):
    #         current = current.next
    #     current.next = None




    def print(self):
        print_ = self.head
        prints_ = []
        while print_ != None:
            prints_.append(print_.value)
            print_ = print_.next
        prints_.append("None")
        return " -> ".join(prints_)


    def __len__(self):
        node = self.head
        licznik = 0
        while(node.next):
            node = node.next
            licznik += 1
        return licznik+1



lista1 = LinkedList()
lista1.head = Node('jeden')
lista1.push_('zero')
lista1.append('dwa')
lista1.append('trzy')
lista1.append('cztery')
# lista1.insert('tak', lista1.node(1))
print("dlugosc listy = ", lista1.__len__())
print(lista1.print())

print(lista1.node(3))
print(lista1.node(0))




