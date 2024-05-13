from os import system
system ("cls")

def intCount (n):
    print (n)
    n += 1
    if n != 7:
        return intCount (n)
    else:
        print (n)
        return n

var = 1
intCount(var)
