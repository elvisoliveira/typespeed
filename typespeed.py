import sys
import time
from random import randint

words = ["one", "two", "three"]
name = ""
nameList = []
totalPlayers = 3
totalWords = 1

def play():
    global words, name

    # Ask for players name
    count = 0
    while count < totalPlayers:
        nameList.append(input("Whats your name:\n"))
        count += 1

    word = words[randint(0, len(words) - 1)]
    print(f"Type the word: {word}")

    speed = time.time();
    response = input()
    if response == word:
        print("Correct!\n")
    else:
        print("Wrong!\n")
    total_secs = round(time.time() - speed)
    print(f"Seu tempo foi de {total_secs}")
    main()

def config():
    global totalPlayers, totalWords
    print("Configure the game")
    response = input(f"1 - Quantos players? [{totalPlayers}]\n2 - Quantas palavras? [{totalWords}]\n")
    if(response == "1"):
        totalPlayers = input("Digite um valor entre 2 e 5\n")
    if(response == "2"):
        totalWords = input("Digite um valor entre 2 e 5\n")
    main()

def main():
    global name
    # Menu
    response = input(f"Hello {name}\n1 - Play\n2 - Change configurations\n3 - Exit\n")
    if(response.strip() == "1"):
        play()
    elif(response.strip() == "2"):
        config()
    elif(response.strip() == "3"):
        sys.exit()
    else:
        main()

main()
