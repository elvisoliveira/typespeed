import sys

def play():
    print("Start the game")

def config():
    print("Config the game")

def main():
    response = input("1 - Jogar\n2 - Alterar configurações do jogo\n3 - Sair\n")
    if(response.strip() == "1"):
        #restarts the program
        play()
    elif(response.strip() == "2"):
        config()
    elif(response.strip() == "3"):
        sys.exit()
    else:
        main()

main()
