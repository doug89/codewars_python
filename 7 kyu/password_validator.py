"""
Password validator
7 kyu
https://www.codewars.com/kata/56a921fa8c5167d8e7000053

Description

Your job is to create a simple password validation function, as seen on many websites.

The rules for a valid password are as follows:

    There needs to be at least 1 uppercase letter.
    There needs to be at least 1 lowercase letter.
    There needs to be at least 1 number.
    The password needs to be at least 8 characters long.

You are permitted to use any methods to validate the password.

Examples:
password("Abcd1234"); ===> true
password("Abcd123"); ===> false
password("abcd1234"); ===> false
password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"); ===> true
password("ABCD1234"); ===> false
password("Ab1!@#$%^&*()-_+={}[]|]\\:;?/>.<,"); ===> true;
password("!@#$%^&*()-_+={}[]|]\\:;?/>.<,"); ===> false;
"""

# def is_valid(password: str) -> bool:
#     has_uppercase = bool(list(filter(str.isupper, password)))
#     has_lowercase = bool(list(filter(str.islower, password)))
#     has_digit = bool(list(filter(str.isdigit, password)))
#     has_length = len(password) >= 8
#     if has_uppercase and has_lowercase and has_digit and has_length:
#         return True
#     else:
#         return False

def is_valid(password: str) -> bool:
    results = []
    results.append(any(char.isupper() for char in password))
    results.append(any(char.islower() for char in password))
    results.append(any(char.isdigit() for char in password))
    results.append(len(password) >= 8)
    return all(results)

passwords = ["Abcd1234",
             "Abcd123",
             "abcd1234",
             "AbcdefGhijKlmnopQRsTuvwxyZ1234567890",
             "ABCD1234",
             "Ab1!@#$%^&*()-_+={}[]|]\\:;?/>.<,",
             "!@#$%^&*()-_+={}[]|\\]:;?/>.<,"]

for password in passwords:
    print(f"{is_valid(password)}\t{password}")