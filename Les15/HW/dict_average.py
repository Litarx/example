from os import system
system ("cls")


def calculate_total(dic,totalname):
    # Сумма всех оценок
    total_notes = sum(dic.values()) / len(dic)
    # Добавляем в словарь
    dic[totalname] = total_notes
    return dic

# --------------------------------------------------#

dic = {
    "sem 1": 9.25,
    "sem 2": 7.50,
    "exam": 8.56,
}

calculate_total(dic,"Total")

for row in dic:
    le = 6 - len(row)
    print(row," " * le, end = "|")
    print(f"{dic[row]:6}")
