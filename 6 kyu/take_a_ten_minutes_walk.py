"""
Take a Ten Minutes Walk
6 kyu
https://www.codewars.com/kata/54da539698b8a2ad76000228/python

Description:

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early
to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens
with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter
strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each
letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will
return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!)
and will, of course, return you to your starting point. Return false otherwise.

    Note: you will always receive a valid array containing a random assortment of direction
    letters ('n', 's', 'e', or 'w' only). It will never give you an empty array
    (that's not a walk, that's standing still!).
"""


def is_valid_walk(walk):
    starting_point = walk.count("w") == walk.count("e") and walk.count("n") == walk.count("s")
    return starting_point and len(walk) == 10

# def is_valid_walk(walk):
#     starting_point = walk.count("w") == walk.count("e") and walk.count("n") == walk.count("s")
#     return True if starting_point and len(walk) == 10 else False


#
# def is_valid_walk(walk):
#     x = 0
#     y = 0
#     for direction in walk:
#         if direction == "w":
#             x -= 1
#         if direction == "e":
#             x += 1
#         if direction == "s":
#             y -= 1
#         if direction == "n":
#             y += 1
#     if x == y == 0 and len(walk) == 10:
#         return True
#     return False


# def is_valid_walk(walk):
#     x = 0
#     y = 0
#     for direction in walk:
#         if direction == "w":
#             x -= 1
#         if direction == "e":
#             x += 1
#         if direction == "s":
#             y -= 1
#         if direction == "n":
#             y += 1
#     distance = abs(x-0) + abs(y-0)
#     round_trip = len(walk) - distance
#     return round_trip <= 10
