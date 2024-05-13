"""https://github.com/dorinesinenco/EDUQATION/blob/master/programming/python/functional/wrappers.ru.md"""

from os import system
system ("cls")


def wrap_brackets1(text):
    return "[" + text + "]"

def wrap_brackets2(text):
    return "<" + text + ">"

def wrap_brackets3(text):
    return "<<<[[[(" + text + "]]]>>>"


print(wrap_brackets1("12345"))

print(wrap_brackets2("12345"))

print(wrap_brackets3("12345"))
