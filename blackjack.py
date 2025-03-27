import random

#DELJENJE KART
#DEALER
dealerCard1 = random.randrange(1, 12)
dealerCard2 = random.randrange(1, 12)
#PLAYER
playerCard1 = random.randrange(1, 12)
playerCard2 = random.randrange(1, 12)
#RETURN
print(f"Dealer Card: {dealerCard1}")
print(f"Player Card: {playerCard1}")
print(f"Player Card: {playerCard2}")
#PRVI IF
if dealerCard1 == 11:
    #MIGHT BLACKJACK
    #INSURANCE
    insurance = int(input("Dealer might have Blackjack, do you want to insure(Half or more tokens)"))
    if insurance == 0 and dealerCard1 + dealerCard2 == 21:
        print("BUST")
    #NI BLACKJACK(2x)
    else:
        insurance += insurance
        balance += insurance
else:
    yourCards = playerCard1+playerCard2
    #RETURN
    print(f"Vsota tvojih cart: {yourCards}")
    #IZBIRA
    #H = HIT
    #D = DOUBLE DOWN
    #P = PASS
    #S = SPLIT
    choice = str(input("Choice(H = HIT, D = DOUBLE DOWN, P = PASS, S = SPLIT): "))
#--------------------------------------------------- 
    #HIT GAME
    if choice == "H":
        while True:
            newCard = random.randrange(1, 12)
            yourCards += newCard
            print(f"Your new card was: {newCard}")
            print(f"Your cards: {yourCards}")
            if yourCards > 21:
                print("BUST")
                break
            else:
                pass
            choice2 = str(input("S = Stop, H = Another: "))
            if choice2  == "H":
                newCard2 = random.randrange(1, 12)
                yourCards += newCard2
                print(f"Your new card was: {newCard2}")
                print(f"Your cards: {yourCards}")
            else:
                break
        #RETURN 
        print(yourCards)    

#---------------------------------------------------             
    #DOUBE DOWN GAME
    elif choice == "D":
        newCard = random.randrange(1, 12)
        yourCards += newCard
        print(f"Your new card was: {newCard}")
        print(f"Your cards: {yourCards}")
        if yourCards > 21:
            print("BUST")

        else:
            pass

                
#---------------------------------------------------                
    #PASS GAME      
    elif choice == "P":
        #RETURN
        print(yourCards)
            
#---------------------------------------------------        
    #SPLIT GAME
    elif choice == "S":
        if playerCard1 == playerCard2:
            playerCard1 += random.randrange(1, 12)
            playerCard2 += random.randrange(1, 12)
            if playerCard1 > 21:
                print("BUST")
            elif playerCard2 > 21:
                print("BUST")
            else:
                choice2 = str(input("1 for first new card, 2 for second new card, 3 for both new cards, 4 to stop"))
                if choice2 == "1":
                    playerCard1 += random.randrange(1, 12)
                    if playerCard1 > 21:
                        print("BUST")
                    else:
                        #RETURN 
                        print(playerCard1)
                        print(playerCard2)
                elif choice2 == "2":
                    playerCard1 += random.randrange(1, 12)
                    if playerCard1 > 21:
                        print("BUST")
                    else:
                        #RETURN 
                        print(playerCard1)
                        print(playerCard2)
                elif choice2 == "3":
                    playerCard1 += random.randrange(1, 12)
                    playerCard2 += random.randrange(1, 12)
                    if playerCard1 > 21 or playerCard2 > 21:
                        print("BUST")
                    else:
                        #RETURN 
                        print(playerCard1)
                        print(playerCard2) 
                elif choice2 == "4":
                    #RETURN 
                    print(playerCard1)
                    print(playerCard2) 
        else:
            print("NOT SAME CARDS")
#--------------------------------------------------- 
    #RESULTS
    print(f"Dealers cards are {dealerCard1} and {dealerCard2}")
    dealerCards = dealerCard1+dealerCard2
    if choice == "H" or choice == "P" or choice == "D":
        while dealerCards < 16:
            newDealerCard = random.randrange(1, 12)
            print(f"Delare got: {newDealerCard}")
            dealerCards += newDealerCard
            print(f"Dealers cards are {dealerCards}")
            if dealerCards > 21:
                print("YOU WIN")
                break
            elif dealerCards == yourCards:
                print("DRAW")
            else:
                pass
        if dealerCards > yourCards:
            print("You lost")
        else:
            print("You won")
    elif choice == "S":
        while dealerCards < 16:
            dealerCards += random.randrange(1, 12)
            print()
            if dealerCards > 21:
                print("DEALER BUSTED")
            elif dealerCards < yourCard1 and dealerCards < playerCard2:
                print("DOUBLE")
            elif dealerCards < playerCard1 and dealerCards > playerCard2:
                print("ONE")
            elif dealerCards > playerCard2 and dealerCards > playerCard2:
                print("ONE")
            elif dealerCards < playerCard2 and dealerCards < playerCard2:
                print("NONE")
