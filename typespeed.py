import sys
import time
from random import randint

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
nameList = []
totalPlayers = 2
totalWords = 5

def play():
    global words

    count = 0
    while count < totalPlayers:
        nameList.append(input(f"Whats your name player {count}\n"))
        count += 1

    for name in nameList:
        totalTime = 0
        countwords = 0
        while countwords < totalWords:
            word = words[randint(0, len(words) - 1)]
            print(f"{name}, type the word: {word}")
            speed = time.time();
            response = input()
            if response == word:
                print("Correct!")
            else:
                print("Wrong!")
            total_speed = round(time.time() - speed)
            print(f"Your time {total_speed} seconds")
            countwords = countwords + 1
            totalTime = totalTime + total_speed
        print(f"{name}, your total time is {totalTime} seconds")

    main()

def config():
    global totalPlayers, totalWords
    print("Configure the game")
    response = input(f"1 - Quantos players? [{totalPlayers}]\n2 - Quantas palavras? [{totalWords}]\n")
    if(response == "1"):
        totalPlayersTemp = input("Digite um valor entre 2 e 5\n ")
        if totalPlayersTemp < "2" or totalPlayersTemp > "5":
            print("Quantidade inválida")
        else:
            totalPlayers = totalPlayersTemp
    if(response == "2"):
        totalWordsTemp = input("Digite um valor entre 5 e 10\n")
        if totalWordsTemp < "5" or totalWordsTemp > "10":
            print("Quantidade inválida")
        else:
            totalWords = totalWordsTemp
    main()

def main():
    response = input(f"1 - Play\n2 - Change configurations\n3 - Exit\n")
    if(response.strip() == "1"):
        play()
    elif(response.strip() == "2"):
        config()
    elif(response.strip() == "3"):
        sys.exit()
    else:
        main()

main()
