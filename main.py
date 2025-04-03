from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from tinydb import TinyDB, Query
from datetime import datetime
import os

app = Flask(__name__)

db = TinyDB('users.json')
users = db.table('uporabniki')  
messages = db.table('sporocila') 
User = Query()

@app.route("/")
def index():
    return render_template("index.html")

#BLACKJACK
@app.route("/blackjack")
def blackjack():
    return render_template("blackjack.html")


#PODATKOVNI ROUTE BLACKJACK
@app.route("/blackjackGet")
def getBlackjack():
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
        #MIGHT BLACKJACK
            if dealerCard1 == 11:
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

#SLOTS
@app.route("/slots")
def slots():
    return render_template("slots.html")


#PODATKOVNI ROUTE SLOTS
@app.route("/slotsGet")
def getSlots():
    rnd1=random.randrange(1,10)
    rnd2=random.randrange(1,10)
    rnd3=random.randrange(1,10)
    print(rnd1, rnd2, rnd3)
    if rnd1 == rnd2 == rnd3 == 1:
    
        print("YOU WON 1€")
    if rnd1 == rnd2 == rnd3 == 2:
        print("YOU WON 20€")
    if rnd1 == rnd2 == rnd3 == 3:
        print("YOU WON 30€")
    if rnd1 == rnd2 == rnd3 == 4:
        print("YOU WON 40€")
    if rnd1 == rnd2 == rnd3 == 5:
        print("YOU WON 500€")
    if rnd1 == rnd2 == rnd3 == 6:
        print("YOU WON 60€")
    if rnd1 == rnd2 == rnd3 == 7:
        print("YOU WON 1000€")
    if rnd1 == rnd2 == rnd3 == 8:
        print("YOU WON 80€")
    if rnd1 == rnd2 == rnd3 == 9:
        print("YOU WON 90€")
    else:
        print("POSKUSI PONOVNO")


#ROLETA
@app.route("/roleta")
def roleta():
    return render_template("roleta.html")


#PODATKOVNI ROUTE ROLETA
@app.route("/roletaGet")
def getRoleta():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
    firstThird = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    secondThird = ["13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
    thirdThird = ["25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
    odd = ["1", "3", "5", "7", "9", "11", "13", "15", "17", "19", "21", "23", "25", "27", "29", "31", "33", "35"]
    even = ["2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30", "32", "34", "36"]
    red = ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"]
    black = ["2", "4", "6", "8", "10", "11", "13", "15", "17", "20", "22", "24", "26", "29", "31", "33", "35"]
    firstHalf = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]
    secondHald = ["19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
    firstTol = ["1", "4", "7", "10", "13", "16", "19", "22", "25", "28", "31", "34"]
    secondTol = ["2", "5", "8", "11", "14", "17", "20", "23", "26", "29", "32", "35"]
    thirdTol = ["3", "6", "9", "12", "15", "18", "21", "24", "27", "30", "33", "36"]
    print("Your choices are: input number, type: firstthird, secondthird, thirdthird, odd, even, red, black, firsthalf, secondhalf, firsttol, secondtol or thirdtol")
    choice = str(input("Input choice you want to play with: "))
    #SPIN
    number = random.randrange(0,37)
    number = str(number)
    print(f"NUMBER IS {number}")
    #NUMBER
    if choice in numbers: 
        if choice == number:
            print("WIN")
        else:
            print("LOST")
    #FIRST THIRD
    elif choice == "firstthird":
        if number in firstThird:
            print("WIN")
        else:
            print("LOST")
    #SECOND THIRD
    elif choice == "secondthird":
        if number in secondThird:
            print("WIN")
        else:
            print("LOST")
    #THIRD THIRD
    elif choice == "thirdthird":
        if number in thirdThird:
            print("WIN")
        else:
            print("LOST")
    #ODD
    elif choice == "odd":
        if number in odd:
            print("WIN")
        else:
            print("LOST")
    #EVEN
    elif choice == "even":
        if number in even:
            print("WIN")
        else:
            print("LOST")
    #RED
    elif choice == "red":
        if number in red:
            print("WIN")
        else:
            print("LOST")
    #BLACK
    elif choice == "black":
        if number in black:
            print("WIN")
        else:
            print("LOST")
    #FIRST HALF
    elif choice == "firsthalf":
        if number in black:
            print("WIN")
        else:
            print("LOST")
    #SECOND HALF
    elif choice == "secondhalf":
        if number in black:
            print("WIN")
        else:
            print("LOST")
    #FIRST STOL
    elif choice == "firsttol":
        if number in black:
            print("WIN")
        else:
            print("LOST")
    #SECOND STOL
    elif choice == "secondtol":
        if number in black:
            print("WIN")
        else:
            print("LOST")
    #THIRD STOL
    elif choice == "thirdtol":
        if number in black:
            print("WIN")
        else:
            print("LOST")
    else:
        print("THIS IS NOT AN OPTION")

#ROLETA
@app.route("/horseraces")
def horseraces():
    return render_template("horseraces.html")


#PODATKOVNI ROUTE ROLETA
@app.route("/horceracesGet")
def getHorseraces():
 

app.run(debug = True)





               

    
