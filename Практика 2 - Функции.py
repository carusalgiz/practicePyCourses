"""
Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
и возвращающую True, если оно простое, и False - иначе.
"""


def is_prime(x):
    check = False
    if x == 2:
        check = True
    elif x % 2 != 0:
        for i in range(3, x):
            if x % i != 0:
                check = True
            else:
                check = False
                break
    return check


q = int(input())
print(is_prime(q))
