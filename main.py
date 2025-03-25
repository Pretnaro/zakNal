import random
from flask import Flask
from tinydb import tinydb


def main():
    #login()
    BlackJack()
    #Ruleta()
    #Slots()
    #Poker()
    #HorseRaces()

def BlackJack():
    #DELJENJE KART
    #DEALER
    dealerCard1 = random.randrange("1, 12")
    dealerCard2 = random.randrange("1, 12")
    #PLAYER
    playerCard1 = random.randrange("1, 12")
    playerCard2 = random.randrange("1, 12")
    #RETURN
    dealerCard1
    playerCard1
    playerCard2
    #PRVI IF
    if dealerCard1 == 11:
        #MIGHT BLACKJACK
        #INSURANCE
        insurance = int(input("Pou ali več žetonov: "))
        if insurance == 0 and dealerCard1 + dealerCard2 == 21:
            print("BUST")
        #NI BLACKJACK(2x)
        else:
            insurance += insurance
            balance += insurance
    else:
        yourCards = playerCard1+playerCard2
        #RETURN
        yourCards
        #IZBIRA
        #H = HIT
        #D = DOUBLE DOWN
        #P = PASS
        #S = SPLIT
        choice = str(input("Choice: "))
#--------------------------------------------------- 
        #HIT GAME
        if choice == "H":
            while True:
                yourCards += random.randrange("1, 12")
                if yourCards > 21:
                    print("BUST")
                    break
                else:
                    pass
                choice2 = str(input("S = Stop, H = Another"))
                if choice2  == "H"
                    pass
                else:
                    break
            #RETURN 
            yourCards    

#---------------------------------------------------             
        #DOUBE DOWN GAME
        elif choice == "D":
            yourCards += random.randrange("1, 12")
            if yourCards > 21:
                print("BUST")
            elif: 
                #RETURN
                yourCards
                
#---------------------------------------------------                
        #PASS GAME      
        elif choice == "P":
            #RETURN
            yourCards
            
#---------------------------------------------------        
        #SPLIT GAME
        elif choice == "S":
            if playerCard1 == playerCard2:
                playerCard1 += random.randrange("1, 12")
                playerCard2 += random.randrange("1, 12")
                if playerCard1 > 21:
                    print("BUST")
                elif playerCard2 > 21:
                    print("BUST")
                else:
                    choice2 = str(input("1 for first new card, 2 for second new card, 3 for both new cards, 4 to stop"))
                    if choice2 == "1":
                        playerCard1 += random.randrange("1, 12")
                        if playerCard1 > 21:
                            print("BUST")
                        else:
                            #RETURN 
                            playerCard1
                            playerCard2
                    elif choice2 == "2":
                        playerCard1 += random.randrange("1, 12")
                        if playerCard1 > 21:
                            print("BUST")
                        else:
                            #RETURN 
                            playerCard1
                            playerCard2
                    elif choice2 == "3":
                        playerCard1 += random.randrange("1, 12")
                        playerCard2 += random.randrange("1, 12")
                        if playerCard1 > 21 or playerCard2 > 21:
                            print("BUST")
                        else:
                            #RETURN 
                            playerCard1
                            playerCard2 
                    elif choice2 == "4":
                        #RETURN 
                        playerCard1
                        playerCard2 
            else:
                print("NOT SAME CARDS")
#--------------------------------------------------- 
        #RESULTS
        print(f"Dealers cards are {dealerCard1} and {dealerCard2}")
        dealerCards = dealerCard1+dealerCard2
        while dealerCards < 16:
            dealerCards += random.randrange("1, 12")
            if dealerCards > 21:
                print("YOU WIN")
            elif dealerCards 
               

    
