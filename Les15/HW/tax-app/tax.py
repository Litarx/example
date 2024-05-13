def inputCalculateTax(dic, sum, tax):
    money = sum #начальная сумму
    tax *= sum / 100  #значение вычисленного налога + процент
    total = money - tax #сумма денег
    '''выбрал вариант словаря так как можно подробно описать какая строчка за что отвечет.
    по крайней мере я знаю как показать это на данном этапе своего развития)'''

    dic ["Amount"] = money
    dic ["Tax"] = tax
    dic ["Sum"] = total
    return dic
