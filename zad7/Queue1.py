from typing import *


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def node(self, at: int) -> Node:
        node = self.head
        if self.head is None:
            print("empty")
            return
        for x in range(at):
            node = node.next
        return node

    def __len__(self):
        node = self.head
        if self.head is None:
            return 0
        licznik = 0
        while node.next:
            node = node.next
            licznik += 1
        return licznik + 1

    def insert(self, value: Any, after: Node) -> None:
        node = Node(value)
        node.next = after.next
        after.next = node

    def remove_last(self) -> Any:
        if self.head is None:
            print("empty")
            return
        node = self.head
        node2 = self.head
        if self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        while node.next is None:
            node = node.next
        while node2.next != node:
            node2 = node2.next
        temp = node
        node2.next = None
        return temp

    def pop(self) -> Any:
        if self.head is None:
            print("empty")
            return
        current = self.head
        self.head = current.next
        return current.value

    def remove(self, after: Node) -> Any:
        if self.head is None:
            print("empty")
            return
        node = after.next
        node2 = node.next
        after.next = node2

    def __str__(self):
        node = self.head
        text = ""
        while node is not None:
            text += str(node.value)
            if node.next is not None:
                text += " -> "
            node = node.next
        return text


class Queue():
    _storage: LinkedList

    def __init__(self):
        self.head = None

    def peek(self) -> Any:
        node = self.head
        if node is None:
            print("empty")
            return
        return node.value

    def enqueue(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def dequeue(self) -> Any:
        if self.head is None:
            print("empty")
            return
        current = self.head
        self.head = current.next
        return current.value

    def __len__(self):
        print(" ")
        node = self.head
        if self.head is None:
            return 0
        licznik = 0
        while node.next:
            node = node.next
            licznik += 1
        return licznik + 1

    def __str__(self):
        node = self.head
        text = ""
        while node is not None:
            text += str(node.value)
            if node.next is not None:
                text += ", "
            node = node.next
        return text
