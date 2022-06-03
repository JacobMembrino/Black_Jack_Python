from random import random, randint
import time
from colorama import Fore, Style
import readchar

def deal():
    # dealer recieves 1 card up, 1 down
    # player recieves 2 cards
    d_card1 = getcard()
    d_card2 = getcard()
    p_card1 = getcard()
    p_card2 = getcard()
    return(p_card1, p_card2, d_card1, d_card2)

def getcard():
    #randint used to generate a face and value of a card in a 52-card deck
    suit = randint(1, 4)
    facechar = ''
    val = randint(2, 14)
    valf = str(val)
    color = ''
    if(suit==1):
        suitchar = '\u2660'
        color = 'BLACK'
    elif(suit==2):
        suitchar = '\u2665'
        color = 'RED'
    elif(suit==3):
        suitchar = '\u2666'
        color = 'RED'
    else:
        suitchar = '\u2663'
        color = 'BLACK'
    if(val==11):
        valf = 'J'
        val = 10
    elif(val==12):
        valf = 'Q'
        val = 10
    elif(val==13):
        valf = 'K'
        val = 10
    elif(val==14):
        valf = 'A'
        val = 11
    card = f"[{valf} {facechar}]"
    
    # remove duplicate cards using recursion
    if(card not in usedcards):
        usedcards.append(card)
        return(card, color, val)
    else:
        return(getcard())
    
def displaycard(card, color):
    # display cards (with color)  
    if color == 'RED':
        print(f"{Fore.RED}{card}{Style.RESET_ALL}", end='\t')
    else:
        print(f"{card}", end='\t')

def user_play(card1_val, card2_val):
    total_val = card1_val + card2_val
    Nat21 = False
    Busted = False
    
    # check for nat 21
    if(total_val == 21):
        time.sleep(1)
        print("\n\nYou Got a Natural 21!!")
        Nat21 = True
        time.sleep(1)
        return(total_val, Busted, Nat21)
    
    while(1):
        print(f"\nYou may either: Hit (h) or Stand (s) (score:{total_val}): ")
        inp = repr(readchar.readchar())
        if(inp == "b'h'"):
            print()
            time.sleep(0.5)
            disp = getcard()
            displaycard(disp[0], disp[1])
            print()
            time.sleep(1)
            total_val += disp[2]
            if(total_val > 21):
                print(f"\nBUST! ({total_val})\n")
                Busted = True
                total_val = 0
                break
            elif(total_val == 21):
                print("\nYour Score is 21!!")
                time.sleep(1)
                break
            else:
                total_val += 0
        elif(inp == "b's'"):
            print(f"\nFinal Score: {total_val}")
            break
        else:
            print("Enter a valid action\n")
    return(total_val, Busted, Nat21)
    
def dealer_play(card1, card2):
    score = card1[2] + card2[2]
    print()
    print("*"*30)
    print("Dealer's Cards:\n")
    displaycard(card1[0], card1[1])
    displaycard(card2[0], card2[1])
    time.sleep(2)
    print()
    
    while(1):
        print(f"\nDealer's Score: {score}\n")
        if score < 17:
            time.sleep(0.5)
            print("Dealer must hit\n")
            time.sleep(0.5)
            disp = getcard()
            displaycard(disp[0], disp[1])
            print()
            time.sleep(1)
            score += disp[2]
        elif 17<=score<=20:
            time.sleep(0.5)
            print("Dealer must stand\n")
            time.sleep(0.5)
            break
        elif score == 21:
            time.sleep(0.5)
            print("Dealer got 21!\n")
            time.sleep(0.5)
            break
        else:
            print("Dealer Busts!\n")
            score = 0
            break
    return(score)

def scoreboard(u_score, d_score, wins, loses, busts, nat21s):
    curScores = "User Score: {}, Dealer Score: {}".format(u_score, d_score)
    ScoreBoard = "Wins  :{:^8} | Loses:{:^8}\nNat21s:{:^8} | Busts:{:^8}".format(wins, loses, nat21s, busts)

    #scoreboard instance
    print("{:^}".format('-'*30))
    print(curScores)
    print()
    print(ScoreBoard)
    print("{:^}".format('-'*30))

# Gameplay Loop starts here
usedcards = []
wins = 0
loses = 0
busts = 0
nat21s = 0

while(1):
    usedcards.clear()
    dealer_score = 0
    cards = deal()
    
    print('*'*30)
    print("Dealer's Hand:")
    displaycard(cards[2][0], cards[2][1])
    print("[? ?]")
    print("\n\nPlayer's Hand:")
    displaycard(cards[0][0], cards[0][1])
    displaycard(cards[1][0], cards[1][1])
    
    user_score = user_play(cards[0][2], cards[1][2]) #returns a list containg [score, busted boolean, Nat 21 boolean]
    
    # skips dealer's play if you bust or get a Natural 21
    if user_score[1]:
        print("You Lose! Bust!\n")
        dealer_score = 1
        busts+=1
    elif user_score[2]:
        dealer_score = 0
        nat21s+=1
    else:
        dealer_score = dealer_play(cards[2], cards[3])
        print(f"Dealer's Final Score: {dealer_score}\n")

    if(dealer_score < user_score[0]):
        print("You Win!\n")
        wins+=1
    elif(dealer_score > user_score[0]):
        print("Dealer Wins!\n")
        loses+=1
    else:
        print("Tie!!\n")
        
    scoreboard(user_score[0], dealer_score, wins, loses, busts, nat21s)
    
    inp1 = ''
    print("\nContinue? (y/n): ")
    inp1 = repr(readchar.readchar())
    while(inp1 != "b'n'"):
        if(inp1 == "b'y'"):
            print("\nStarting New Game...\n")
            time.sleep(1)
            break
        else:
            print("Please enter y/n")
    if(inp1 == "b'n'"):
            print("Thanks For Playing!\n")
            break
