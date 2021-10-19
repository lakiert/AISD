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



    def print(self):
        print_ = self.head
        prints_ = []
        while print_ != None:
            prints_.append(print_.value)
            print_ = print_.next
        prints_.append("None")
        return " -> ".join(prints_)


lista1 = LinkedList()
lista1.head = Node('monday')
lista1.push_('tuesday')
lista1.push_('apple')
lista1.push_('first')
lista1.append('last')
print(lista1.print())


