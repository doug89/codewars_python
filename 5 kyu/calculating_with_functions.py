"""
Calculating with Functions
5 kyu
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

"""

def zero(n=''): return eval("0"+n)
def one(n=''): return eval("1"+n)
def two(n=''): return eval("2"+n)
def three(n=''): return eval("3"+n)
def four(n=''): return eval("4"+n)
def five(n=''): return eval("5"+n)
def six(n=''): return eval("6"+n)
def seven(n=''): return eval("7"+n)
def eight(n=''): return eval("8"+n)
def nine(n=''): return eval("9"+n)

def plus(n): return " + " + str(n)
def minus(n): return f" - {n}"
def times(n): return f" * {n}"
def divided_by(n): return f" // {n}"



# def zero(n=0):
#     return 0 if n == 0 else eval(str(0) + n)
# def one(n=1):
#     return 1 if n == 1 else eval(str(1) + n)
# def two(n=2):
#     return 2 if n == 2 else eval(str(2) + n)
# def three(n=3):
#     return 3 if n == 3 else eval(str(3) + n)
# def four(n=4):
#     return 4 if n == 4 else eval(str(4) + n)
# def five(n=5):
#     return 5 if n == 5 else eval(str(5) + n)
# def six(n=6):
#     return 6 if n == 6 else eval(str(6) + n)
# def seven(n=7):
#     return 7 if n == 7 else eval(str(7) + n)
# def eight(n=8):
#     return 8 if n == 8 else eval(str(8) + n)
# def nine(n=9):
#     return 9 if n == 9 else eval(str(9) + n)
#
# def plus(n): return " + " + str(n)
# def minus(n): return f" - {n}"
# def times(n): return f" * {n}"
# def divided_by(n): return f" // {n}"



# def zero(n=0):
#     if n == 0:
#         return 0
#     else:
#         return eval(str(0) + n)
# def one(n=1):
#     if n == 1:
#         return 1
#     else:
#         return eval(str(1) + n)
# def two(n=2):
#     if n == 2:
#         return 2
#     else:
#         return eval(str(2) + n)
# def three(n=3):
#     if n == 3:
#         return 3
#     else:
#         return eval(str(3) + n)
# def four(n=4):
#     if n == 4:
#         return 4
#     else:
#         return eval(str(4) + n)
# def five(n=5):
#     if n == 5:
#         return 5
#     else:
#         return eval(str(5) + n)
# def six(n=6):
#     if n == 6:
#         return 6
#     else:
#         return eval(str(6) + n)
# def seven(n=7):
#     if n == 7:
#         return 7
#     else:
#         return eval(str(7) + n)
# def eight(n=8):
#     if n == 8:
#         return 8
#     else:
#         return eval(str(8) + n)
# def nine(n=9):
#     if n == 9:
#         return 9
#     else:
#         return eval(str(9) + n)
#
# def plus(n): return " + " + str(n)
# def minus(n): return f" - {n}"
# def times(n): return f" * {n}"
# def divided_by(n): return f" // {n}"

print(four(divided_by(two())))