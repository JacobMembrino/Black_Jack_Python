from random import random, randint
import time
from colorama import Fore, Style

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
    face = randint(1, 4)
    val = randint(2, 14)
    valf = str(val)
    facechar = ''
    color = ''
    
    if(face==1):
        facechar = '\u2660'
        color = 'BLACK'
    elif(face==2):
        facechar = '\u2665'
        color = 'RED'
    elif(face==3):
        facechar = '\u2666'
        color = 'RED'
    else:
        facechar = '\u2663'
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
    Busted = False
    Nat21  = False
    total_val = card1_val + card2_val

    # check for nat 21
    if(total_val == 21):
        print("\nYou Got a Natural 21!!")
        Nat21 = True
        time.sleep(1)
        return(total_val, Busted, Nat21)
    
    print("\n\nType: Hit (h), Stand (s)")
    while(1):
        inp = input(f"What will you do?: (score:{total_val})")
        if(inp == 'h'):
            print()
            time.sleep(0.5)
            disp = getcard()
            displaycard(disp[0], disp[1])
            print()
            time.sleep(1)
            total_val += disp[2]
            if(total_val > 21):
                print(f"\nBUST! :({total_val}) :( \n")
                Busted = True
                break
            elif(total_val == 21):
                print("\nYour Score is 21!!")
                time.sleep(1)
                break
            else:
                total_val += 0
        elif(inp=='s'):
            print(f"\nFinal Score: {total_val} Dealer's Turn...")
            break
        else:
            print("Enter a valid action\n")
    return(total_val, Busted, Nat21)
    
def dealer_play(card1, card2):
    
    score = card1[2] + card2[2]
    print("*"*30)
    print("Dealer's Cards:\n")
    displaycard(card1[0], card1[1])
    displaycard(card2[0], card2[1])
    time.sleep(1)
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
            print("Dealer Busts!")
            break
    return(score)

def scoreboard(u_score, d_score):
    print("{:^}".format('-'*30))
    print(f"User Score: {}, Dealer Score: {}".format(u_score, d_score))
    print("{:^}".format('-'*30))
    

# Gameplay Loop starts here
usedcards = []
while(1):
    usedcards.clear()
    cards = deal()
    
    print("Dealer's Hand:")
    displaycard(cards[2][0], cards[2][1])
    print("[? ?]")
    print("\n\nPlayer's Hand:")
    displaycard(cards[0][0], cards[0][1])
    displaycard(cards[1][0], cards[1][1])
    
    user_score = user_play(cards[0][2], cards[1][2]) #returns a list containg [score, busted boolean, Nat 21 boolean]
    
    # skips dealer's play if you bust or get a Natural 21
    if user_score[1]:
        print("You Lose!\n")
    elif user_score[2]:
        print("You Win!\n")
    else:
        dealer_score = dealer_play(cards[2], cards[3])
        print(f"Dealer's Final Score: {dealer_score}\n")
        
    scoreboard(user_score, dealer_score)
    
    inp = chr(input("Continue? y/n : "))
    if(inp == 'n'):
        print("Thanks For Playing!/n")
        break
    elif(inp == 'y'):
        print("\nStarting New Game")
        time.sleep(1)
    else:
        print("Please enter y/n")
