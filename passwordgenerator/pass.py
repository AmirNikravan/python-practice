import random
from lists import *
import os
import time


def rand():
    os.system('cls')
    print("*******************RAMZ TASADOFI***************")
    print("dar hal tolid ramz")
    time.sleep(3)
    passw = []
    for j in range(0, 5):
        passw.append(random.choice(nlist))
    for j in range(0, 9):
        passw.append(random.choice(alist))
    for j in range(0, 5):
        passw.append(random.choice(mlist))
    random.shuffle(passw)
    real = ''.join(passw)
    print(f"ramz shoma = {real}")


def custom():
    passw = []
    os.system('cls')
    print("*******************RAMZ TASADOFI***************")
    number = int(input("tedad adad be kar rafte dar ramz chand ta bashad ?\n"))
    while number <= 5:
        os.system('cls')
        print("tedad adad bayad bishtar az 5 ta bashad!")
        number = int(
            input("tedad adad be kar rafte dar ramz chand ta bashad ?\n"))
    for i in range(0, number):
        passw.append(random.choice(nlist))
    alpha = int(input("tedad harf be kar rafte dar ramz chand ta bashad ?\n"))
    while alpha <= 5:
        os.system('cls')
        print("tedad harf bayad bishtar az 5 ta bashad!")
        alpha = int(
            input("tedad harf be kar rafte dar ramz chand ta bashad ?\n"))
    for i in range(0, alpha):
        passw.append(random.choice(alist))
    char = int(input("tedad meta char be kar rafte dar ramz chand ta bashad ?\n"))
    while char <= 5:
        os.system('cls')
        print("tedad meta char bayad bishtar az 5 ta bashad!")
        char = int(
            input("tedad meta char be kar rafte dar ramz chand ta bashad ?\n"))
    for i in range(0, char):
        passw.append(random.choice(mlist))
    os.system('cls')
    print("dar hal tolid ramz")
    time.sleep(3)
    real = ''.join(passw)
    print((f"ramz shoma = {real}"))


os.system('cls')
print("BE BARNAME RAMZ SAZ KHOSH AMADID")
print("1.RAMZ TASADOFI")
print("2.RAMZ SHAKHSI SAZI SHODE")
ch = int(input("choose your choice : "))
if ch == 1:
    rand()
else:
    custom()
