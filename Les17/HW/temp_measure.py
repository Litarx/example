from os import system

system("cls")


class TempNow:
    value = None
    gradein = None
    output = None

    def index():
        TempNow.value = float(input("Grade:"))
        TempNow.gradein = str.upper(input("In:"))
        TempNow.output = str.upper(input("Show In:"))
        return TempNow.value

    def convert():
        if TempNow.gradein == "C":
            if TempNow.output == "K":
                TempNow.value += 273.15
            if TempNow.output == "F":
                TempNow.value = (TempNow.value * 9/5) + 32
            else:
                pass

        if TempNow.gradein == "K":
            if TempNow.output == "F":
                TempNow.value = TempNow.value * 9 / 5 - 459.67
            if TempNow.output == "C":
                TempNow.value -= 273.15
            else:
                pass

        if TempNow.gradein == "F":
            if TempNow.output == "K":
                TempNow.value = TempNow.value * 5 / 9 + 459.67
            if TempNow.output == "C":
                TempNow.value = (TempNow.value - 32) * 5 / 9
            else:
                pass

        return TempNow.value

    def print():
        out_value = (TempNow.convert())  # Ensure convert is called and the value is updated
        print(out_value, "* ", TempNow.output, sep="")


TempNow.index()
TempNow.print()
