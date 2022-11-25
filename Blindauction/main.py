from art import logo
import os


def log():
    os.system('cls')
    print(logo)


def find(bids_rec):
    val = 0
    winner = ""
    for i in bids_rec:
        if bids_rec[i] > val:
            val = bids_rec[i]
            winner = i
    print(f"{winner} ba mablagh {val} barande shod :D")


bids = {}
cont = 'yes'
while cont == 'yes':
    log()
    name = input("nam khod ra vared konid : ")
    bid = int(input("mablagh khod ra vared knoid : $"))
    bids.update({name: bid})
    cont = input("add user ? yes/no : ")
find(bids)
