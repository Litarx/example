"""https://github.com/dorinesinenco/EDUQATION/blob/master/programming/python/functional/input.helpers.ru.md"""

from os import system
system ("cls")


def inputInt(message):
    val = int(input(message))
    return val

def inputFloat(message):
    val = float(input(message))
    return val

def inputBoolean(message):
    val = bool(input(message))
    return val


i1 = inputInt("put int:")
i2 = inputInt("put int:")
print("Sum of integers =", i1 + i2)

f1 = inputFloat("put float:")
f2 = inputFloat("put float:")
print("Sum of float =", f1 + f2)

b1 = inputBoolean("put boolean:")
b2 = inputBoolean("put boolean:")
print("Boolean =", b1 >= b2)
