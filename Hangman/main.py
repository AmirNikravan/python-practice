import os
import time
import random
from arts import *
from words import *


def menu():
    print(logo)
    os.system('cls')
    print("*************BE BAZI HANGMAN KHOSH AMADID*************")
    print("1.shorou bazi")
    print("2.moshahede kalamat")
    print("3.ezafe kardan kalame")
    print("4.khoroj")


def start():
    os.system('cls')
    print(logo)
    word = random.choice(word_list)
    guess = []
    time = 7
    for _ in word:
        guess += '_'
    while time:
        os.system('cls')
        print(logo)
        print(word)
        game_stats = False
        print(stages[time-1])
        print(f"time = {time}")
        print(''.join(guess))
        char = input("yek harf ra hads bezanid : ")

        for pos in range(len(word)):
            if word[pos] == char:
                guess[pos] = char
                game_stats = True
        if not game_stats:
            time = time - 1
        if "_" not in guess:
            time = 0
    if "_" not in guess:
        return True
    else:
        return False


def cont():
    val = input("aya edame midahaid(yes/no): ")
    if val == 'yes':
        return True
    else:
        return False


def add():
    os.system('cls')
    print(logo)
    print("**************ezafe kardan kalame*****************")
    word = input("lotfan kalame mored nazar ra vared konid : ")
    word_list.append(word)
    edame = cont()


edame = True
while (edame):

    menu()
    choice = int(input("lotfan gozine mored nazar ra vared konid : "))
    if choice == 1:
        stat = start()
        if stat == True:
            print("shoma barande shodid :D")
        else:
            print("shoma bakhtid :(")
        edame = cont()
    elif choice == 2:
        for i in range(len(word_list)):
            print(f"{i+1} = {word_list[i]}")
        edame = cont()
    elif choice == 3:
        add()
        edame = cont()
    else :
        edame = False
os.system('cls')
print(logo)
print("kharej shodid :D")