import sys
from random import randint

words = ["one", "two", "three"]
name = ""

def play():
    global words, name
    word = words[randint(0, len(words) - 1)]
    print(f"Type the word: {word}")
    response = input()
    if response == word:
        print("Correct!")
        podium = open("podium.txt","a")
        print(name, file=podium)
        podium.close()
    else:
        print("Wrong!")
    main()

def config():
    print("Configure the game\n")
    main()

def main():
    global name

    # Ask for player name
    if(len(name.strip()) == 0):
        name = input("Whats your name:\n")

    # Menu
    response = input(f"Hello {name}\n1 - Play\n2 - Change configurations\n3 - Score\n4 - Exit\n")
    if(response.strip() == "1"):
        play()
    elif(response.strip() == "2"):
        config()
    elif(response.strip() == "4"):
        sys.exit()
    else:
        main()

main()
