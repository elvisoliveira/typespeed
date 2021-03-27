import sys
from random import randint

words = ["one", "two", "three"]

def play():
    global words
    word = words[randint(0, len(words) - 1)]
    print(f"Type the word: {word}")
    response = input()
    if response == word:
        print("Correct!")
    else:
        print("Wrong!")
    main()

def config():
    print("Configure the game")

def main():
    response = input("1 - Play\n2 - Change configurations\n3 - Exit\n")
    if(response.strip() == "1"):
        play()
    elif(response.strip() == "2"):
        config()
    elif(response.strip() == "3"):
        sys.exit()
    else:
        main()

main()
