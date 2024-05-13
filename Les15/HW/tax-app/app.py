from os import system
from tax import inputCalculateTax
system ("cls")

payment = {}
# money = 10000
money = int(input("Amount is: "))
tax = 10

inputCalculateTax(payment,money,tax)

for row in payment:
    le = 6 - len(row)
    print(row, " " * le, end=":")
    print(f"{payment[row]:9}")
