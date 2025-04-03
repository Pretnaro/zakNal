import random
#BET INPUT
balance = 1000
print(f"Your balance is: {balance}")
bet = int(input("Input bet: "))
balance -= bet
print(f"Your new balance is: {balance}")


#SEZNAM Z ŠTEVILKAMI 
numbers = [str(i) for i in range(10001)]
#DELJENJE KART
#DEALER
dealerCard1 = random.randrange(1, 12)
dealerCard2 = random.randrange(1, 12)
    #PLAYER
    playerCard1 = random.randrange(1, 12)
    playerCard2 = random.randrange(1, 12)
    #RETURN
    print(f"Dealer Card: {dealerCard1}")
    print("---------------------------")
    print(f"Player Card: {playerCard1}")
    print(f"Player Card: {playerCard2}")
    print("---------------------------")
    while True: 
        #PRVI IF
        if playerCard1 + playerCard2 == 21:
            print("AVTOMATSKI BLACKJACK")
            print("You win")
            break
        if dealerCard1 == 11:
            #MIGHT BLACKJACK
            #INSURANCE
            insurance = str(input("Dealer might have Blackjack, do you want to insure(Y/N): "))
            if insurance == "Y":
                vnosek = int(input("Input insurance: "))
            elif insurance == "N":
                pass
            print(f"Second card was: {dealerCard2}")
            if insurance == 0 and dealerCard1 + dealerCard2 == 21:
                print("BUST")
                break
            #NI BLACKJACK(2x)
            else:
                vnosek += vnosek
                balance += vnosek
        else:
            yourCards = playerCard1+playerCard2
            #RETURN
            print(f"Vsota tvojih cart: {yourCards}")
        #IZBIRA
        #H = HIT
        #D = DOUBLE DOWN
        #P = PASS
        #S = SPLIT
        if playerCard1 == playerCard2:
            choice = str(input("Choice(H = HIT, D = DOUBLE DOWN, P = PASS, S = SPLIT): "))
        else: 
            choice = str(input("Choice(H = HIT, D = DOUBLE DOWN, P = PASS): "))
    
    #--------------------------------------------------- 
    
        #HIT GAME
        if choice == "H" or choice == "h":
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
            if choice2  == "H" or choice2 == "h":
                newCard2 = random.randrange(1, 12)
                yourCards += newCard2
                print(f"Your new card was: {newCard2}")
                print(f"Your cards: {yourCards}")
                if yourCards > 21:
                    print("BUST")
                    break
                else:
                    pass
                choice3 = str(input("S = Stop, H = Another: "))
                if choice3  == "H" or choice3 == "h":
                    newCard2 = random.randrange(1, 12)
                    yourCards += newCard2
                    print(f"Your new card was: {newCard2}")
                    print(f"Your cards: {yourCards}")
                    if yourCards > 21:
                        print("BUST")
                        break
                    else:
                        pass
                else:
                    pass
            else:
                pass
                
        #RETURN 
            print(yourCards)    
    
    #---------------------------------------------------             
        #DOUBE DOWN GAME
        elif choice == "D" or choice == "d":
            newCard = random.randrange(1, 12)
            yourCards += newCard
            print(f"Your new card was: {newCard}")
            print(f"Your cards: {yourCards}")
            if yourCards > 21:
                print("BUST")
                break
            else:
                pass
    
                    
    #---------------------------------------------------                
        #PASS GAME      
        elif choice == "P" or choice == "p":
            pass
                
    #---------------------------------------------------        
        #SPLIT GAME
        elif choice == "S" or choice == "s":
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
        print(f"Dealers cards are {dealerCards}")
        if choice == "H" or choice == "P" or choice == "D":
            while dealerCards < 16:
                newDealerCard = random.randrange(1, 12)
                print(f"Delare got: {newDealerCard}")
                dealerCards += newDealerCard
                print(f"Dealers cards are {dealerCards}")
                if dealerCards > 21:
                    print("YOU WIN")
                    break
                else:
                    pass
            if dealerCards > yourCards:
                print("You lost")
                break
            elif dealerCards == yourCards:
                print("DRAW")
                balance += bet
                break
            else:
                print("You won")
                balance += bet*2
                break
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
    print(f"Your new balance is: {balance}")
    