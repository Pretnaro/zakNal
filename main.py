from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from tinydb import TinyDB, Query
from datetime import datetime
import os
import random

app = Flask(__name__)
app.secret_key = "UltraSigma"

db = TinyDB('users.json')
users = db.table('uporabniki')  
User = Query()

@app.route('/')
def index():
    if 'username' in session:
        return render_template('kazalo.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    session['role'] = 'user'
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            user = users.get(User.username == username)          
            if user:
                if user['password'] == password:
                    session['username'] = username
                    return jsonify({'success': True})                 
                else:
                    return jsonify({'success': False, 'error': 'Napačno geslo'})
            else:
                users.insert({'username': username, 'password': password})
                session['username'] = username
                return jsonify({'success': True})
        except Exception as e:
            print(f"Napaka pri prijavi: {str(e)}")
            return jsonify({'success': False, 'error': 'Prišlo je do napake'})
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))



@app.route("/kazalo")
def kazalo():
    return render_template("kazalo.html")

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
    result = "POSKUSI PONOVNO"  # MESS
    prize = 0  # PRIZE
    #REZULTATI
    if rnd1 == rnd2 == rnd3 == 1:
        print("YOU WON 1€")
        prize = 1
    elif rnd1 == rnd2 == rnd3 == 2:
        print("YOU WON 20€")
        prize = 20
    elif rnd1 == rnd2 == rnd3 == 3:
        print("YOU WON 30€")
        prize = 30
    elif rnd1 == rnd2 == rnd3 == 4:
        print("YOU WON 40€")
        prize = 40
    elif rnd1 == rnd2 == rnd3 == 5:
        print("YOU WON 500€")
        prize = 500
    elif rnd1 == rnd2 == rnd3 == 6:
        print("YOU WON 60€")
        prize = 60
    elif rnd1 == rnd2 == rnd3 == 7:
        print("YOU WON 1000€")
        prize = 1000
    elif rnd1 == rnd2 == rnd3 == 8:
        print("YOU WON 80€")
        prize = 80
    elif rnd1 == rnd2 == rnd3 == 9:
        print("YOU WON 90€")
        prize = 90
    else:
        print("POSKUSI PONOVNO")
        prize = 0

    img_map = {
    1: "/static/images/slots/apple.jpg",
    2: "/static/images/slots/banana.jpg",
    3: "/static/images/slots/bell.jpg",
    4: "/static/images/slots/cherries.jpg",
    5: "/static/images/slots/coins.jpg",
    6: "/static/images/slots/grape.jpg",
    7: "/static/images/slots/sedmica.jpg",
    8: "/static/images/slots/rubby.jpg",
    9: "/static/images/slots/strawberry.jpg",
    }

    return jsonify(result=result, prize=prize, numbers=[img_map[rnd1], img_map[rnd2], img_map[rnd3]])



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
    choice = request.args.get('choice')
    #SPIN
    number = random.randrange(0,37)
    number = str(number)
    print(f"NUMBER IS {number}")
    #NUMBER
    result = "LOST"
    if choice in numbers: 
        if choice == number:
            result  = "WIN"
    #FIRST THIRD
    elif choice == "firstthird":
        if number in firstThird:
            result  = "WIN"
    #SECOND THIRD
    elif choice == "secondthird":
        if number in secondThird:
            result  = "WIN"
    #THIRD THIRD
    elif choice == "thirdthird":
        if number in thirdThird:
            result  = "WIN"
    #ODD
    elif choice == "odd":
        if number in odd:
            result  = "WIN"
    #EVEN
    elif choice == "even":
        if number in even:
            result  = "WIN"
    #RED
    elif choice == "red":
        if number in red:
            result  = "WIN"
    #BLACK
    elif choice == "black":
        if number in black:
            result  = "WIN"
    #FIRST HALF
    elif choice == "firsthalf":
        if number in black:
            result  = "WIN"
    #SECOND HALF
    elif choice == "secondhalf":
        if number in black:
            result  = "WIN"
    #FIRST STOL
    elif choice == "firsttol":
        if number in black:
            result  = "WIN"
    #SECOND STOL
    elif choice == "secondtol":
        if number in black:
            result  = "WIN"
    #THIRD STOL
    elif choice == "thirdtol":
        if number in black:
            result  = "WIN"

    return jsonify({
        "result": result,
        "number": number,
        "choice": choice
    })

#HORSE RACES
@app.route("/horseraces")
def horseraces():
    return render_template("horseraces.html")


#PODATKOVNI ROUTE HORSE RACES
@app.route("/horceracesGet")
def getHorseraces():
    horseNumber = int(input("Input horse number: "))
    videoNumber = random.randrange(5)
    if horseNumber == videoNumber:
        print("YOU WIN")
    else:
        print("YOU LOST")

#UPPERLOWER
@app.route("/upperlower")
def upperlower():
    return render_template("upperlower.html")


#PODATKOVNI ROUTE HORSE RACES
@app.route("/upperlowerGet")
def getUpperlower():

    img_map = {
    0: "/static/images/upperlower/cardback.jpg",
    1: "/static/images/upperlower/ace.jpg",
    2: "/static/images/upperlower/two.jpg",
    3: "/static/images/upperlower/three.jpg",
    4: "/static/images/upperlower/four.jpg",
    5: "/static/images/upperlower/five.jpg",
    6: "/static/images/upperlower/six.jpg",
    7: "/static/images/upperlower/seven.jpg",
    8: "/static/images/upperlower/eight.jpg",
    9: "/static/images/upperlower/nine.jpg",
    10: "/static/images/upperlower/ten.jpg",
    11: "/static/images/upperlower/jack.jpg",
    12: "/static/images/upperlower/queen.jpg",
    13: "/static/images/upperlower/king.jpg"
    }


    result = "LOST"
    card1 = random.randint(1, 14)
    card2 = random.randint(1, 14)
    card3 = random.randint(1, 14)
    card4 = random.randint(1, 14)
    while True:
        print(card1)
        guess1 = input("U/L: ")
        print(card2)
        if card2 == card1:
            result = "isti karti"
            break
        if (card2 > card1 and guess1 == "U") or (card2 < card1 and guess1 == "L"):
            guess2 = input("U/L: ")
            print(card3)
            if card3 == card2:
                result = "isti karti"
                break
            if (card3 > card2 and guess2 == "U") or (card3 < card2 and guess2 == "L"):
                guess3 = input("U/L: ")
                print(card4)
                if card4 == card3:
                    result = "isti karti"
                    break
                if (card4 > card3 and guess3 == "U") or (card4 < card3 and guess3 == "L"):
                    result = "WIN"
                    break
                else:
                    result = "BUST"
                    break
            else:
                result = "BUST"
                break
        else:
            result = "BUST"
            break
    return jsonify(result=result, numbers=[img_map[card1], img_map[card2], img_map[card3], img_map[card4] ])

app.run(debug = True)





               

    
