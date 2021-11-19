# zad1

# def numbers(n: int):
#
#     if (n < 0):
#         return
#
#     print(n)
#     numbers(n-1)
#
#
# numbers(10)



# zad2

# def fib(n: int):
#
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# print(fib(0))
# print(fib(1))
# print(fib(2))
# print(fib(3))
# print(fib(4))
# print(fib(5))
# print(fib(6))
# print(fib(7))
# print(fib(8))



# zad3

# def power(number: int, n: int) -> int:
#
#     if (n==0):
#         return 1
#     elif (n==1):
#         return number
#     else:
#         return number*(power(number, n-1))
#
#
# print(power(10, 3))
# print(power(2, 3))



# zad4
#
# def reverse(txt: str) -> str:
#     if len(txt) == 0:
#         return txt
#     else:
#         return reverse(txt[1:]) + txt[0]
#
#
# print("Ala ma kota")
# print(reverse("Ala ma kota"))



# zad5

# def factorial(n: int) -> int:
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
#
#
# print(factorial(4))
# print(factorial(3))
# print(factorial(2))
# print(factorial(1))
# print(factorial(0))
# print(factorial(7))



# zad6

# def prime(n: int, i=2) -> bool:
#     if n < 2:
#         return False
#     if n % i == 0:
#         return False
#     if i * i > n:
#         return True
#
#
#     return prime(n, i + 1)
#
#
# print(prime(7))
# print(prime(10))


