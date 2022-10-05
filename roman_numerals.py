import pyinputplus as pyip
import re

I = 1
II=2
III=3

IV=4
V=5

IX=9
X=10

L=50

XC=90
C=100

CD=400
D=500

CM=900
M=1000

MV=4000
V=5000

def convert():
    value = pyip.inputInt(prompt='Enter a number or Roman Numeral',allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'],min=0, max=5000)
    roman_regex = re.compile(r'(I|V|X|L|C|D|M)')
    mo = roman_regex.search(value)
    if mo == None:
        num = True
    else:
        num = False
    if num==True: # converting a number to roman numeral
        value = int(value)
        answer=[]
        # split number into units and add the corresponding letters to a list
        if value >=1000:
            thousands=value//1000
            if thousands <4:
                for i in range(thousands):
                    answer.append("M")
            elif thousands == 4:
                answer.append("MV")
            else:
                answer.append("V")
        if value >= 100:
            hundreds=(value%1000)//100
            if hundreds >0:
                if hundreds < 4:
                    for i in range(hundreds):
                        answer.append("C")
                elif hundreds == 4:
                    answer.append("CD")
                elif hundreds == 5:
                    answer.append("D")
                elif hundreds <9:
                    answer.append("D")
                    for i in range(hundreds-5):
                        answer.append("C")
                elif hundreds ==9:
                    answer.append("CM")
        if value >= 10:
            tens=(value%100)//10
            if tens >0:
                if tens < 4:
                    for i in range(tens):
                        answer.append("X")
                elif tens == 4:
                    answer.append("XL")
                elif tens == 5:
                    answer.append("L")
                elif tens <9:
                    answer.append("L")
                    for i in range(tens-5):
                        answer.append("X")
                elif tens ==9:
                    answer.append("XC")
        units=(value%10)
        if units > 0:
            if units < 4:
                for i in range(units):
                    answer.append("I")
            elif units == 4:
                answer.append("IV")
            elif units == 5:
                answer.append("V")
            elif units <9:
                answer.append("V")
                for i in range(units-5):
                    answer.append("I")
            elif units ==9:
                answer.append("IX")
        print("".join(answer))
    
    #if converting a roman numeral to a number
    if num == False:
        list = []
        answer = []
        for i in range(len(value)):
            list.append(value[i])
        print(list)

        for i in range(len(list)):
            if list[i] == "I":
                if i < len(list)-1 and (list[i+1] == "V" or list[i+1] == "X"):
                    answer.append(-1)
                else:
                    answer.append(1)
            elif list[i] == "V":
                answer.append(5)
            elif list[i] == "X":
                if i < len(list)-1 and list[i+1] == "C":
                    answer.append(-10)
                else:
                    answer.append(10)
            elif list[i]=="C":
                if i < len(list)-1 and list[i+1] == "D":
                    answer.append(-100)
                else:
                    answer.append(100)
            elif list[i]=="D":
                answer.append(500)
            elif list[i]=="M":
                answer.append(1000)
        print(sum(answer))

if __name__ == "__main__":
    convert()
