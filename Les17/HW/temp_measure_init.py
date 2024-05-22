from os import system

system("cls")


class TempNow:
    def __init__(self):
        self.value = None
        self.gradein = None
        self.output = None

    def index(self):
        self.value = float(input("Grade:"))
        self.gradein = str.upper(input("In:"))
        self.output = str.upper(input("Show In:"))
        return self.value

    def convert(self):
        if self.gradein == "C":
            if self.output == "K":
                self.value += 273.15
            if self.output == "F":
                self.value = (self.value * 9 / 5) + 32
            else:
                pass

        if self.gradein == "K":
            if self.output == "F":
                self.value = self.value * 9 / 5 - 459.67
            if self.output == "C":
                self.value -= 273.15
            else:
                pass

        if self.gradein == "F":
            if self.output == "K":
                self.value = self.value * 5 / 9 + 459.67
            if self.output == "C":
                self.value = (self.value - 32) * 5 / 9
            else:
                pass

        return self.value

    def print(self):
        out_value = self.convert()  # Ensure convert is called and the value is updated
        print(out_value, "* ", self.output, sep="")


temp = TempNow()
temp.index()
temp.print()
