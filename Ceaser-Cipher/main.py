from words import alphabet
from os import system


def encode(str, shift):
    new_str = ""
    for word in str:
        possition = shift
        possition += alphabet.index(word)
        if (possition) >= 26:
            n = int(possition / 26)
            if n == 0:
                n = 1
            possition -= n * 26
        new_str += alphabet[possition]
    return new_str


def decode(str, shift):
    new_str = ""
    for word in str:
        possition = shift
        possition = alphabet.index(word) - shift
        if possition < 0:
            n = int(abs(possition) / 26)
            if n == 0:
                n = 1
            possition += n * 26
        new_str += alphabet[possition]
    return new_str


stat = True
while stat:
    system("clear")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    new_str = ""
    if direction == "encode":
        new_str = encode(text, shift)
    else:
        new_str = decode(text, shift)
    print(f"your new string is = {new_str}")
    continu = input("Do you continue?(yes/no)")
    if continu == "no":
        break
