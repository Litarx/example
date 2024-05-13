from os import system
system ("cls")


"""

Interactive version VVV
"""

# def drawLine():
#     length = int(input("L>"))
#     direction = input("H/V>")
#     data = []
#     data.append(length)
#     data.append(direction)
#     if data [1] == "h":
#         print("-" * length)
#     if data [1] == "v":
#         print("|\n" * length)
#     return data

# drawLine()


"""

Constant version VVV
"""
def drawLine(length, direction):
    if direction == "h":
        print("-" * length)
    if direction == "v":
        print("|\n" * length)
    return

drawLine(5,"v")
