import random

def w(s):
    if(s==1):
        word = random.choice(["ironman",'hulk','thor','wanda','vision','tonystark','captain america','spiderman','blackwidow','thanos','ultron',"falcon","wintersoldier","scarlettwitch","loki",'shangchi',"venom"])
        return word
    elif(s==4):
        word = random.choice(['operatingsystem','network','algorithm','firewall','java','keyboard','linux','motherboard','teminal','windows'])
        return word
    elif(s==3):
        word = random.choice(['athletics','basketball','baseball','badminton','cricket','football','gymnastics','hockey','olympics','rugby','tabletennis'])
        return word
    elif(s==2):
        word = random.choice(['afghanistan','australia','brazil','china','canada','denmark','france','india','italy','japan','malaysia','unitedstatesofamerica'])
        return word
    else:
        print("Invalid choice!")

def game1():
    print("Choose your theme:\n")
    print("1:Avengers\n2:Country Names\n3:Sports\n4:Computers")
    
    s = int(input())
    if(s==0 or s>4):
        print("Invalid choice\nEnter one of the above options")
        s = int(input())
        word = w(s)
    else:
        word = w(s)

    validletters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessmade = ""
    while(len(word)>0):
        main = ""
        for i in word:
            if i in guessmade:
                main = main + i
            else:
                main = main + "-" + ""
        if(main==word):
            print(word)
            print("You Win!!")
            break


        print(main)
        guess = input()
        if guess in guessmade and word:
            print("Letter already guessed")

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Invalid input, Re-Enter: ")
            guess = input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("________")
                print("\n 9 turns left")
            if turns==8:
                print("________")
                print("    O   ")
                print("\n 8 turns left")
            if turns==7:
                print("________")
                print("    O   ")
                print("    |   ")
                print("\n 7 turns left")
            if turns==6:
                print("________")
                print("    O   ")
                print("    |   ")
                print("   /    ")
                print("\n 6 turns left")
            if turns==5:
                print("________")
                print("    O   ")
                print("    |   ")
                print("   / \  ")
                print("\n 5 turns left")
            if turns==4:
                print("________")
                print("    O /  ")
                print("    |   ")
                print("   / \  ")
                print("\n 4 turns left")
            if turns==3:
                print("________")
                print("  \ O /  ")
                print("    |   ")
                print("   / \  ")
                print("\n 3 turns left")
            if turns==2:
                print("________")
                print("         ")
                print("         ")
                print("    |    ")
                print("  \ O /  ")
                print("    |   ")
                print("   / \  ")
                print("\n 2 turns left")
            if turns==1:
                print("________")
                print("         ")
                print("    __    ")
                print("    |    ")
                print("  \ O /  ")
                print("    |   ")
                print("   / \  ")
                print("\n 1 turns left")
            if turns==0:
                print("________")
                print("      |  ")
                print("    __|    ")
                print("    |    ")
                print("  \ O /  ")
                print("    |   ")
                print("   / \  ")
                print("\n GAME OVER !!   Y-O-U-L-O-S-E")
                break




x=input('Enter your name: ')
print("Welcome to the game %s"%x)
print("---------------------")
print("Guess the word in 10 attempts")
game1()
