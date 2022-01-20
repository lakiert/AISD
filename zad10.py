from array import array
from ctypes import Array
from typing import Tuple


def binary_search(numbers: Array, value: int) -> Tuple[bool, int]:
    start, end = 0, len(numbers) - 1

    while start <= end:
        middle = (start + end) // 2
        if numbers[middle] == value:
            return True, middle
        elif numbers[middle] < value:
            start += 1
        elif numbers[middle] > value:
            end -= 1

    return False, -1


ints = array('I', [1, 5, 6, 7, 10, 26, 29, 40])

result = binary_search(ints, 40)
result = binary_search(ints, 10)

print(result)
