"""
Get the Middle Character
7 kyu
https://www.codewars.com/kata/56747fd5cb988479af000028/python

Description:

You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

    If the string's length is odd, return the middle character.
    If the string's length is even, return the middle 2 characters.
"""

# def get_middle(s: str) -> str:
#     if len(s) % 2 == 0:
#         return s[int(len(s)/2-1):int(len(s)/2+1)]
#     return s[int(len(s)/2)]

# def get_middle(s: str) -> str:
#     index = int(len(s)/2)
#     if len(s) % 2 == 0:
#         return s[index-1:index+1]
#     return s[index]

def get_middle(string: str) -> str:
    index = int(len(string)/2)
    return string[index-1:index+1] if len(string) % 2 == 0 else string[index]



print(get_middle("ABCD"))
print(get_middle("ABCDE"))
