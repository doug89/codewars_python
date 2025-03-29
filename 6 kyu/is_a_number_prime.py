"""
Is a number prime?
6 kyu
https://www.codewars.com/kata/5262119038c0985a5b00029f/python

Description:

Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Requirements

    You can assume you will be given an integer input.
    You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
    NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.

Example

is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */

"""


def is_prime(n):
    if n <= 3: return n > 1
    if n % 2 == 0 or (n > 5 and n % 10 == 5): return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

# def is_prime(n):
#     # This is dirty and I am ashamed.
#     if (n<=3): return n > 1
#     if n % 10 in [2, 4, 6, 8, 0, 5] and n not in [2, 5]:
#         return False
#     if n < 10000:
#         for i in range(3, n//2+1, 2):
#             if n % i == 0:
#                 return False
#     else:
#         for i in range(3, n//900+1, 2):
#             if n % i == 0:
#                 return False
#     return True


# def is_prime(n):
#     if n % 10 in [2,4,6,8,0,5] and n not in [2, 5]:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return False if n < 2 else True

for i in range(12):
    print(f"{i}: {is_prime(i)}")
