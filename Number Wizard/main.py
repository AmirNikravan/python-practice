import random
import os

first = 1
last = 99
print("welcom to number guesser programm")
flag = True
while flag:
    stat = ""
    comp_guess = random.randint(first, last)
    str = input("aya adad shoma {} ast ? yes/no ".format(comp_guess))
    os.system("clear")
    if str == "yes":
        print("i won")
        break
    else:
        stat = input("""ok let me guess again :)\nbigger or smaller ? """)
    if stat == "bigger":
        first = comp_guess + 1
    else:
        last = comp_guess - 1
