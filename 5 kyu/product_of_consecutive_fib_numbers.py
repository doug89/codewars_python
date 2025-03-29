"""
Product of consecutive Fib numbers
5 kyu
https://www.codewars.com/kata/5541f58a944b85ce6d00006a/python

Description:

The Fibonacci numbers are the numbers in the following integer sequence (Fn): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such that:
F(0)=0F(1)=1F(n)=F(n−1)+F(n−2)F(0) = 0\\F(1) = 1\\F(n) = F(n-1) + F(n-2)F(0)=0F(1)=1F(n)=F(n−1)+F(n−2)

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying:
F(n)∗F(n+1)=prodF(n) * F(n+1) = prodF(n)∗F(n+1)=prod
"""

def product_fib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    return [a, b, a * b == prod]


def product_fib(prod):
    seq = [0, 1]
    while seq[-1] * seq[-2] < prod:
        seq.append(seq[-1] + seq[-2])
    return [seq[-2],seq[-1], seq[-2] * seq[-1] == prod]

print(product_fib(100000))
