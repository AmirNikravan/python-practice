import random


def deal_card():  # return a radnom number
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def check(player, computer):

    if player == computer:
        print("draw")
    elif player > 21:
        print("you lose")
    elif computer > 21:
        print("you win")
    elif player > computer:
        print("you win")
    else:
        print("you lose")


print("welcome to game")

while 1:

    player_cards = list()
    for i in range(2):
        player_cards.append(deal_card())
    print(f"your cards : {player_cards}")
    computer_cards = list()
    computer_cards.append(deal_card())
    print(f"computer first card : {computer_cards[0]}")
    st = input("type y to another card type n to pass")
    if st == "n":
        print(f"your final cards : {player_cards}")
        total_player = sum(player_cards)
        total_computer = sum(computer_cards)
        while total_computer < total_player:
            computer_cards.append(deal_card())
            total_computer = sum(computer_cards)
        print(f"your cards : {player_cards}")
        print(f"comp cards : {computer_cards}")
        check(total_player,total_computer)
        break
    else :
        stat = True
        while stat :
            player_cards.append(deal_card())