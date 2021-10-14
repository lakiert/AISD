# class House:
#     doors: int
#     color: str
#
#     def __init__(self, doors: int, color: str) -> None:
#         self.doors = doors
#         self.color = color
#
#     def change_color(self, new_color: str) -> None:
#         if new_color == self.color:
#             raise ValueError('new color should differ from the old one')
#
#         self.color = new_color
#
#     def __str__(self) -> str:
#         return f' liczba drzwi wynosi: {self.doors} ,' \
#             f' color elewacji: {self.color} '
#
#     def __len__(self) -> int:
#         return 100
#
# green_house: House = House(doors=15, color='green')
# blue_house: House = House(doors=10, color='blue')
# print(green_house.doors)
# print(green_house.color)
# print(green_house)
# print(blue_house)
# print(len(blue_house))





# from typing import List
#
# l: List[int] = [1,0,2,3,7,4]
#
# print(l)
# print(len(l))





# def sum_(x: int, y: int) -> int:
#     return x+y
#
# assert sum_(2,2) == 4
























