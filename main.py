from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from tinydb import TinyDB, Query
from datetime import datetime
import os
import random

app = Flask(__name__)
app.secret_key = "UltraSigma"

db = TinyDB('users.json')
users = db.table('uporabniki') 
realdb = TinyDB('realusers.json')
realusers = realdb.table('uporabniki') 
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
                    session.pop('reallogin', None)  
                    return jsonify({'success': True, 'redirect': url_for('kazalo')})                 
                else:
                    return jsonify({'success': False, 'error': 'Napačno geslo'})
            else:
                users.insert({'username': username, 'password': password})
                session['username'] = username
                session.pop('reallogin', None)
                return jsonify({'success': True, 'redirect': url_for('kazalo')})
        except Exception as e:
            print(f"Napaka pri prijavi: {str(e)}")
            return jsonify({'success': False, 'error': 'Prišlo je do napake'})
    return render_template('login.html')


@app.route('/reallogin', methods=['GET', 'POST'])
def reallogin():
    session['role'] = 'user'
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            image = request.form.get('image')

            user = realusers.get(User.username == username)

            if user:
                if user['password'] == password:
                    session['username'] = username
                    session['reallogin'] = True
                    return jsonify({'success': True, 'redirect': url_for('realkazalo')})
                else:
                    return jsonify({'success': False, 'error': 'Napačno geslo'})
            else:
                realusers.insert({
                    'username': username,
                    'password': password,
                    'balance': 5,
                    'image': image
                })
                session['username'] = username
                session['reallogin'] = True
                return jsonify({'success': True, 'redirect': url_for('realkazalo')})
        except Exception as e:
            print(f"Napaka pri prijavi: {str(e)}")
            return jsonify({'success': False, 'error': 'Prišlo je do napake'})
    return render_template('reallogin.html')



@app.route('/api/add_money', methods=['POST'])
def api_add_money():
    if 'username' not in session:
        return jsonify({'success': False, 'error': 'Uporabnik ni prijavljen.'}), 401

    try:
        amount = float(request.form['amount'])
        if amount <= 0:
            return jsonify({'success': False, 'error': 'Znesek mora biti večji od 0.'}), 400

        username = session['username']
        User = Query()
        user = realusers.get(User.username == username)

        if user:
            new_balance = user['balance'] + amount
            realusers.update({'balance': new_balance}, User.username == username)
            return jsonify({'success': True, 'new_balance': new_balance})
        else:
            return jsonify({'success': False, 'error': 'Uporabnik ni najden.'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('reallogin', None)
    return redirect(url_for('login'))

@app.route("/kazalo")
def kazalo():
    if 'username' in session:
        return render_template("kazalo.html")
    return redirect(url_for('login'))

@app.route('/realkazalo')
def realkazalo():
    if 'username' not in session:
        return redirect(url_for('reallogin'))

    user = realusers.get(User.username == session['username'])
    balance = user['balance'] if user else 0

    return render_template('realkazalo.html', balance=balance)
    
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
    card1 = random.randint(1, 13)
    card2 = random.randint(1, 13)
    card3 = random.randint(1, 13)
    card4 = random.randint(1, 13)
    while True:
        print(card1)
        guess1 = request.args.get("U/L: ")
        print(card2)
        if card2 == card1:
            result = "isti karti"
            break
        if (card2 > card1 and guess1 == "U") or (card2 < card1 and guess1 == "L"):
            guess1 = request.args.get("U/L: ")
            print(card3)
            if card3 == card2:
                result = "isti karti"
                break
            if (card3 > card2 and guess2 == "U") or (card3 < card2 and guess2 == "L"):
                guess1 = request.args.get("U/L: ")
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

@app.route("/getbalance")
def get_balance():
    user_id = request.args.get("user_id")
    with open("realuser.json", "r") as f:
        data = json.load(f)

    user = data.get("uporabniki", {}).get(user_id)
    if not user:
        return jsonify({"error": "User not found", "balance": 0})

    return jsonify({"balance": user.get("balance", 0)})

#SLOTS
@app.route("/realslots")
def realslots():
    return render_template("realslots.html")


@app.route("/realSlotsGet")
def getRealSlots():
    if 'username' not in session:
        return jsonify(result="Niste prijavljeni.", prize=0, balance=0, numbers=["", "", ""])

    username = session['username']
    user = realusers.get(User.username == username)

    if not user:
        # Če še ni v realusers bazi, dodaj z začetnim stanjem
        user = {'username': username, 'balance': 50.0}
        realusers.insert(user)
    balance = user['balance']

    if balance < 5:
        return jsonify(result="Premalo denarja!", prize=0, balance=balance, numbers=["", "", ""])

    balance -= 5  # Odštej stavo

    rnd1 = random.randint(1, 9)
    rnd2 = random.randint(1, 9)
    rnd3 = random.randint(1, 9)

    prize = 0
    result = "POSKUSI PONOVNO"

    if rnd1 == rnd2 == rnd3:
        prize_dict = {
            1: 1, 2: 20, 3: 30, 4: 40, 5: 500,
            6: 60, 7: 1000, 8: 80, 9: 90
        }
        prize = prize_dict.get(rnd1, 0)
        result = f"ČESTITKE! DOBIL SI {prize}€"
        balance += prize

    # Posodobi stanje uporabnika v TinyDB
    realusers.update({'balance': balance}, User.username == username)

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

    return jsonify(
        result=result,
        prize=prize,
        balance=round(balance, 2),
        numbers=[img_map[rnd1], img_map[rnd2], img_map[rnd3]]
    )






@app.route("/realblackjack")
def realblackjack():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("realblackjack.html")

@app.route("/realbalance")
def realbalance():
    if 'username' not in session:
        return jsonify({"error": "Ni prijave"}), 401
    user = realusers.get(User.username == session['username'])
    if user:
        return jsonify({"balance": user.get("balance", 0)})
    return jsonify({"error": "Uporabnik ne obstaja"}), 404

@app.route("/realblackjackStart")
def realblackjack_start():
    if 'username' not in session:
        return jsonify({"error": "Ni prijave"}), 401

    bet = int(request.args.get("bet", 0))
    user = realusers.get(User.username == session['username'])

    if not user:
        return jsonify({"error": "Uporabnik ne obstaja"}), 404

    balance = user.get("balance", 0)

    if bet <= 0 or bet > balance:
        return jsonify({"error": "Neveljavna stava"}), 400

    balance -= bet
    realusers.update({"balance": balance}, User.username == session['username'])

    playerCards = [random.randint(1, 11), random.randint(1, 11)]
    dealerCards = [random.randint(1, 11)]

    session["playerCards"] = playerCards
    session["dealerCards"] = dealerCards
    session["bet"] = bet

    return jsonify({
        "playerCards": playerCards,
        "dealerCards": dealerCards,
        "balance": balance
    })

@app.route("/realblackjackResult", methods=["POST"])
def realblackjack_result():
    if 'username' not in session:
        return jsonify({"error": "Ni prijave"}), 401

    data = request.get_json()
    outcome = data.get("outcome")  # "win", "lose", "draw"
    user = realusers.get(User.username == session['username'])

    if not user:
        return jsonify({"error": "Uporabnik ne obstaja"}), 404

    balance = user.get("balance", 0)
    bet = session.get("bet", 0)

    if outcome == "win":
        balance += bet * 2
    elif outcome == "draw":
        balance += bet
    elif outcome == "lose":
        pass
    else:
        return jsonify({"error": "Neveljaven rezultat"}), 400

    realusers.update({"balance": balance}, User.username == session['username'])
    return jsonify({"balance": balance})


# ROLETA
@app.route("/realroleta")
def realroleta():
    return render_template("realroleta.html")


@app.route("/realroletaGet")
def getrealRoleta():
    choice = request.args.get('choice')
    bet = float(request.args.get('bet', 0))

    # Uporabnik iz seje
    username = session.get('username')
    if not username:
        return jsonify({"error": "Uporabnik ni prijavljen."}), 401

    user = realusers.get(User.username == username)
    if not user:
        return jsonify({"error": "Uporabnik ne obstaja."}), 404

    if user['balance'] < bet:
        return jsonify({"error": "Nimaš dovolj sredstev za to stavo."}), 400

    # Spin rulete
    number = str(random.randint(0, 36))
    result = "LOST"

    def in_group(numlist):
        return number in [str(n) for n in numlist]

    # Skupine
    firstThird = range(1, 13)
    secondThird = range(13, 25)
    thirdThird = range(25, 37)
    odd = [n for n in range(1, 37) if n % 2 == 1]
    even = [n for n in range(1, 37) if n % 2 == 0]
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 29, 31, 33, 35]
    firstHalf = range(1, 19)
    secondHalf = range(19, 37)
    firstTol = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    secondTol = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    thirdTol = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

    # Logika zmage
    if choice == number:
        result = "WIN"
    elif choice == "firstthird" and in_group(firstThird):
        result = "WIN"
    elif choice == "secondthird" and in_group(secondThird):
        result = "WIN"
    elif choice == "thirdthird" and in_group(thirdThird):
        result = "WIN"
    elif choice == "odd" and in_group(odd):
        result = "WIN"
    elif choice == "even" and in_group(even):
        result = "WIN"
    elif choice == "red" and in_group(red):
        result = "WIN"
    elif choice == "black" and in_group(black):
        result = "WIN"
    elif choice == "firsthalf" and in_group(firstHalf):
        result = "WIN"
    elif choice == "secondhalf" and in_group(secondHalf):
        result = "WIN"
    elif choice == "firsttol" and in_group(firstTol):
        result = "WIN"
    elif choice == "secondtol" and in_group(secondTol):
        result = "WIN"
    elif choice == "thirdtol" and in_group(thirdTol):
        result = "WIN"

    # Posodobi balance
    new_balance = user['balance'] - bet
    if result == "WIN":
        new_balance += bet * 2

    realusers.update({'balance': new_balance}, User.username == username)

    return jsonify({
        "result": result,
        "number": number,
        "choice": choice,
        "new_balance": new_balance
    })



#UPPERLOWER
@app.route("/realupperlower")
def realupperlower():
    return render_template("realupperlower.html")


#PODATKOVNI ROUTE HORSE RACES
@app.route("/realupperlowerGet")
def getrealUpperlower():

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
    card1 = random.randint(1, 13)
    card2 = random.randint(1, 13)
    card3 = random.randint(1, 13)
    card4 = random.randint(1, 13)
    while True:
        print(card1)
        guess1 = request.args.get("U/L: ")
        print(card2)
        if card2 == card1:
            result = "isti karti"
            break
        if (card2 > card1 and guess1 == "U") or (card2 < card1 and guess1 == "L"):
            guess1 = request.args.get("U/L: ")
            print(card3)
            if card3 == card2:
                result = "isti karti"
                break
            if (card3 > card2 and guess2 == "U") or (card3 < card2 and guess2 == "L"):
                guess1 = request.args.get("U/L: ")
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
@app.route("/realupperlowerStart")
def real_upperlower_start():
    username = session.get('username')
    if not username:
        return jsonify(error="Niste prijavljeni.")

    user = realusers.get(User.username == username)
    if not user:
        return jsonify(error="Uporabnik ne obstaja.")

    try:
        bet = float(request.args.get('bet', 0))
    except:
        return jsonify(error="Neveljavna stava.")

    if bet <= 0:
        return jsonify(error="Stava mora biti večja od 0.")
    if user['balance'] < bet:
        return jsonify(error="Premalo sredstev za stavo.")

    # Posodobi stanje
    new_balance = user['balance'] - bet
    realusers.update({'balance': new_balance}, User.username == username)

    # Shrani stavo v session (če hočeš jo uporabit kasneje)
    session['last_bet'] = bet

    cards = [random.randint(1, 13) for _ in range(4)]

    return jsonify(cards=cards, balance=round(new_balance, 2))

@app.route("/realupperlowerWin")
def real_upperlower_win():
    username = session.get('username')
    if not username:
        return jsonify(error="Niste prijavljeni.")

    user = realusers.get(User.username == username)
    if not user:
        return jsonify(error="Uporabnik ne obstaja.")

    bet = session.get('last_bet', 0)
    prize = round(bet * 2, 2) if bet else 10  # fallback

    new_balance = user['balance'] + prize
    realusers.update({'balance': new_balance}, User.username == username)

    return jsonify(prize=prize, balance=round(new_balance, 2))

#HORSE RACES
@app.route("/realhorseraces")
def realhorseraces():
    return render_template("realhorseraces.html")

@app.route("/realhorceracesGet")
def getrealHorseraces():
    if 'username' not in session:
        return jsonify({"error": "Not logged in"}), 401

    chosen = request.args.get("chosen")
    stake = request.args.get("stake")

    if chosen is None or stake is None:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        chosen = int(chosen)
        stake = float(stake)
    except ValueError:
        return jsonify({"error": "Invalid parameters"}), 400

    username = session["username"]

    with open("realuser.json", "r") as f:
        data = json.load(f)

    uporabniki = data.get("uporabniki", {})

    user_id = None
    for uid, user in uporabniki.items():
        if user["username"] == username:
            user_id = uid
            break

    if not user_id:
        return jsonify({"error": "User not found"}), 404

    user = uporabniki[user_id]
    balance = user.get("balance", 0)

    if stake > balance:
        return jsonify({"error": "Not enough balance", "balance": balance}), 400

    winner = random.randint(0, 4)

    if chosen == winner:
        balance += stake
        result = "YOU WIN"
    else:
        balance -= stake
        result = "YOU LOSE"

    user["balance"] = balance
    data["uporabniki"][user_id] = user

    with open("realuser.json", "w") as f:
        json.dump(data, f, indent=4)

    return jsonify({
        "result": result,
        "winner": winner,
        "balance": balance
    })


app.run(debug = True)





               

    
