"""
Detect Pangram
6 kyu
https://www.codewars.com/kata/545cedaa9943f7fe7b000048/python

Description:

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""


def is_pangram(string: str) -> bool:
    letters = set([i for i in string.upper() if i.isalpha()])
    return len(letters) == 26


# def is_pangram(string):
#     unique_chars = set()
#     for char in string.upper():
#         if char.isalpha():
#             unique_chars.add(char)
#     return len(unique_chars) == 26