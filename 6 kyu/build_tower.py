"""
Build Tower
6 kyu
https://www.codewars.com/kata/576757b1df89ecf5bd00073b/python

Description:
Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
"""

def tower_builder(n_floors):
    building = []
    for i in range(1, n_floors+1):
        whitespace = " " * (n_floors - i)
        floor = "*" * (1 + 2 * (i-1))
        building.append(whitespace + floor + whitespace)
    return building


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