from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from tinydb import TinyDB, Query
from datetime import datetime
import os

app = Flask(__name__)

db = TinyDB('users.json')
users = db.table('uporabniki')  
messages = db.table('sporocila') 
User = Query()


@app.route('/login', methods=['GET', 'POST'])
def login():
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

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/blackjack")
def BlackJack():
    return render_template("blackjack.html")

@app.route("/blackjackGet")
def getBlackjack():
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
        if choice == "H" or choice == "P" or choice == "D":
            while dealerCards < 16:
                dealerCards += random.randrange("1, 12")
                if dealerCards > 21:
                    print("YOU WIN")
                elif dealerCards > yourCards:
                    print("YOU LOST")
        elif choice == "S"
            while dealerCards < 16:
                dealerCards += random.randrange("1, 12")
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

#---------------------------------------------------

#RULETA
def ruleta():
    numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    firstThird = [1,2,3,4,5,6,7,8,9,10,11,12]
    secondThird = [13,14,15,16,17,18,19,20,21,22,23,24]
    thirdThird = [25,26,27,28,29,30,31,32,33,34,35,36]
    odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
    even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    black = [2,4,6,8,10,11,13,15,17,20,22,24,26,29,31,33,35]
    firstHalf = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    secondHald = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    firstTol = [1,4,7,10,13,16,19,22,25,28]
    secondTol = [2,5,8,11,14,17,20,23,26,29]
    thirdTol = [3,6,9,12,15,18,21,24,27,30]
    choice = str(input("Input: "))
    #SPIN
    number = random.randrange(0,37)
    #NUMBER
    if i == in numbers:
        choice = int(choice)
        if choice == number:
            print("WIN")
        else:
            print("LOST")
    #FIRST THIRD
    elif choice == "firstthird"
        if number in firstThird:
            print("WIN")
        else:
            print("LOST")
    #SECOND THIRD
    elif choice == "secondthird"
        if number in secondThird:
            print("WIN")
        else:
            print("LOST")
    #THIRD THIRD
    elif choice == "thirdthird"
        if number in thirdThird:
            print("WIN")
        else:
            print("LOST")
    #ODD
    elif choice == "odd"
        if number in odd:
            print("WIN")
        else:
            print("LOST")
    #EVEN
    elif choice == "even"
        if number in even:
            print("WIN")
        else:
            print("LOST")
    #RED
    elif choice == "red"
        if number in red:
            print("WIN")
        else:
            print("LOST")
    #BLACK
    elif choice == "black"
        if number in black:
            print("WIN")
        else:
            print("LOST")
    #FIRST HALF
    elif choice == "firsthalf"
        if number in black:
            print("WIN")
        else:
            print("LOST")
    #SECOND HALF
    elif choice == "secondhalf"
        if number in black:
            print("WIN")
        else:
            print("LOST")
    #FIRST STOL
    elif choice == "firsttol"
        if number in black:
            print("WIN")
        else:
            print("LOST")
    #SECOND STOL
    elif choice == "secondtol"
        if number in black:
            print("WIN")
        else:
            print("LOST")
    #THIRD STOL
    elif choice == "thirdtol"
        if number in black:
            print("WIN")
        else:
            print("LOST")


#---------------------------------------------------
#SLOTS
def slots():
    rnd1=random.randrange(1,10)
    rnd2=random.randrange(1,10)
    rnd3=random.randrange(1,10)
    if rnd1 == 7 and rnd3 == 7 and rnd2 == 7:
        print("WIN")
    else:
        print("POSKUSI PONOVNO")


#---------------------------------------------------
#HORSE RACES
def horseRaces():
    horseNumber = int(input("Input horse number: "))
    videoNumber = random.randrange(5)
    if horseNumber == videoNumber:
        print("YOU WIN")
    else:
        print("YOU LOST")

app.run(debug = True)





               

    
