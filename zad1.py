# zad1

# x='J'
# y='Kowalski'
#
# def funkcja(x,y):
#     return x + '.' + y
#
# print (funkcja(x,y))
# print (funkcja('A' , 'Nowak'))


# zad2

# imie = 'andrzej'
# nazwisko = 'kowalski'
#
# def funkcja(x,y):
#     return x[0].capitalize() + '.' + y.capitalize()
#
# print(funkcja(imie,nazwisko))
# print(funkcja('janina','nowak'))


# zad3

# pierwsze=20
# drugie=21
# wiek=21
#
# def funkcja(x,y,z):
#     rok = (x*100)+y
#     wynik = rok - z
#     return wynik
#
# print(funkcja(pierwsze,drugie,wiek))
# print(funkcja(20,21,45))


# zad4

# imie = 'andrzej'
# nazwisko = 'kowalski'
#
# def funkcja1(x,y):
#     return x[0].capitalize() + '.' + y.capitalize()
#
# def funkcja2(x,y,foo):
#     return foo(x,y)
#
# print(funkcja2(imie,nazwisko,funkcja1))
# print(funkcja2('jan','nowak',funkcja1))


# zad5

# def funkcja(x,y):
#     if x>0 & (y>0 & y!=0):
#         return x/y
#
# print(funkcja(10,5))
# print(funkcja(-20,10))
# print(funkcja(10,0))


# zad6

# wynik=0
# limit=100
#
# while wynik < limit:
#     i= int(input("podaj liczbe:"))
#     wynik += i
#
# print("wynik=", wynik)


# zad7
#
# lista1 = [1,2,3,4,5]
# lista2 = ['ola','ala','ela','ula']
#
# def funkcja7(lista):
#     return tuple(lista)
#
# print(funkcja7(lista1))
# print(funkcja7(lista2))


# zad8
# lista=[]
# print('podaj trzy imiona')
# def funkcja8(lista):
#     for i in range(3):
#         lista.append(input('podaj imie:'))
#
#     return tuple(lista)
#
# print(funkcja8(lista))


# zad9

# tydzien=['poniedzialek','wtorek','sroda','czwartek','piatek','sobota','niedziela']
# liczba=1
# def funkcja9(liczba):
#     liczba = int(input('podaj numer dznia tygodnia:'))
#     return tydzien[liczba-1]
#
# print(funkcja9(liczba))


# zad10

# # text2=''.join(reversed(text))
# # text3=text[::-1]

# napis=input('podaj slowo:')
# def funkcja10(napis):
#     if napis == napis[::-1]:
#         return True
#     else:
#         return False
#
# print(funkcja10(napis))


