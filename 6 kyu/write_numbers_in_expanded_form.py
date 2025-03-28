"""
Write Number in Expanded Form
6 kyu
https://www.codewars.com/kata/5842df8ccbd22792a4000245

Description:
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"

NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2 https://www.codewars.com/kata/write-number-in-expanded-form-part-2!!
"""

# def expanded_form(num):
#     i = 1
#     sections = []
#     number = num
#     while num != 0:
#         remainder = num % 10**i
#         num -= remainder
#         if remainder != 0:
#             sections.append(str(remainder))
#         i += 1
#     return " + ".join(reversed(sections))


# def expanded_form(number):
#     n = str(number)
#     segments = []
#     for i, char in enumerate(n):
#         if char != "0":
#             segments.append(char + "0" * (len(n) - i - 1))
#     return " + ".join(segments)


def expanded_form(n):
    return [char + "0" * (len(str(n)) - i - 1) for i, char in enumerate(str(n)) if char != "0"]

print(expanded_form(70304))
