from typing import Any

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value:Any) -> None:
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
        if (self.head == None):
            print("empty")
            return
        for x in range(at):
            node = node.next
        return node

    def __len__(self):
        node = self.head
        if (self.head == None):
            return 0
        licznik = 0
        while (node.next):
            node = node.next
            licznik += 1
        return licznik + 1

    def print(self):
        element = self.head
        data = element.value
        text = str(data)
        while (element.next != None):
            element = element.next
            data = element.value
            text += " -> " + str(data)
        print(text)

    def insert(self, value: Any, after: Node) -> None:
        node = Node(value)
        node.next = after.next
        after.next = node

    def remove_last(self) -> Any:
        current = self.head
        current2 = self.head
        if (self.head == None):
            print("empty")
            return
        while (current.next != self.tail):
            current = current.next
        while (current2.next != current):
            current2 = current2.next
        temp = current
        current2.next = None
        return temp

    def pop(self) -> Any:
        current = self.head
        if (self.head == None):
            print("empty")
            return
        temp = current
        current2 = current.next
        self.head = current2
        return temp

    def remove(self, after: Node) -> Any:
        if (self.head == None):
            print("empty")
            return
        node = after.next
        node2 = node.next
        after.next = node2




lista = LinkedList()
# print("lista: ")
# lista.append(1)
# lista.append(2)
# lista.append(3)
# lista.append(4)
# lista.append(5)
# lista.append(6)
# lista.append(7)
# lista.print()
# print("\n0 na poczatku: ")
# lista.push(0)
# lista.print()
# print("\nusuniecie ostatniego: ")
# lista.remove_last()
# lista.print()
# print("\nusuniecie pierwszego: ")
# lista.pop()
# lista.print()
# print("\nusuniecie wezla nr 3: ")
# lista.remove(after=lista.node(2))
# lista.print()
# print("\ndlugosc listy: ")
# print(lista.__len__())



class Stack():
    _storage: LinkedList()

    def __init__(self):
        self.head = None

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __len__(self):
        print(" ")
        node = self.head
        if self.head == None:
            return 0
        licznik = 0
        while (node.next != None):
            node = node.next
            licznik += 1
        return licznik + 1

    def print(self):
        element = self.head
        data = element.value
        text = str(data)
        while (element.next != None):
            element = element.next
            data = element.value
            text += "\n ^ \n" + str(data)
        print(" ")
        print(text)

    def pop(self) -> Any:
        current = self.head
        if (self.head == None):
            print("empty")
            return
        temp = current
        current2 = current.next
        self.head = current2
        return temp


stack = Stack()

# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.print()
# print(stack.pop())
# stack.print()

# print(stack.__len__())














