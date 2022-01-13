from typing import *


def bubble_ascending(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]


def bubble_descending(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]


def selection_ascending(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
            l[i], l[min_index] = l[min_index], l[i]


def selection_descending(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] > l[min_index]:
                min_index = j
            l[i], l[min_index] = l[min_index], l[i]


def insertion_ascending(l):
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i-1
        while j >= 0 and l[j] > key:
            l[j+1] = l[j]
            j = j-1
            l[j+1] = key


def insertion_descending(l):
    n = len(l)
    for i in range(1, n):
        key = l[i]
        j = i-1
        while j >= 0 and key > l[j]:
            l[j+1] = l[j]
            j = j-1
            l[j+1] = key




list1 = [6, 1, 7, 3, 4, 9, 2, 5, 8, 0]
print(list1)
bubble_ascending(list1)
print(list1)
bubble_descending(list1)
print(list1)


print("\n")
list1 = [6, 1, 7, 3, 4, 9, 2, 5, 8, 0]
print(list1)
selection_ascending(list1)
print(list1)
selection_descending(list1)
print(list1)

print("\n")
list1 = [6, 1, 7, 3, 4, 9, 2, 5, 8, 0]
print(list1)
insertion_ascending(list1)
print(list1)
insertion_descending(list1)
print(list1)

