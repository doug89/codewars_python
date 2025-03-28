"""
Build Tower
6 kyu
https://www.codewars.com/kata/576757b1df89ecf5bd00073b/python
Description:
Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
"""


def tower_builder(n):
    return [("*" * (1 + 2 * i)).center(1 + 2 * (n - 1)) for i in range(n)]


# def tower_builder(n):
#     floors = ["*" * (1 + 2 * (i-1)) for i in range(1, n+1)]
#     return [floor.center(1 + 2 * (n-1)) for i, floor in enumerate(floors)]


# def tower_builder(n_floors):
#     building = []
#     for i in range(0, n_floors):
#         floor = "*" * (1 + (2 * (i)))
#         building.append(floor.center(1 + (2 * (n_floors - 1))))
#     return building


# def tower_builder(n_floors):
#     building = []
#     for i in range(1, n_floors+1):
#         whitespace = " " * (n_floors - i)
#         floor = "*" * (1 + 2 * (i-1))
#         building.append(whitespace + floor + whitespace)
#     return building


# def tower_builder(n_floors):
#     building = []
#     building.append("*" * (1 + 2 * (n_floors-1)))
#     for i in range(1, n_floors):
#         floor = list(building[-1])
#         floor[floor.index("*")] = " "
#         floor.reverse()
#         floor[floor.index("*")] = " "
#         building.append("".join(floor))
#     building.reverse()
#     return building


print(tower_builder(6))