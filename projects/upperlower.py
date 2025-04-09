import random
card1 = random.randint(1, 15)
card2 = random.randint(1, 15)
card3 = random.randint(1, 15)
card4 = random.randint(1, 15)


while True:
    print(card1)

    guess1 = input("U/L: ")
    print(card2)

    if card2 == card1:
        print("isti karti")
        break

    if (card2 > card1 and guess1 == "U") or (card2 < card1 and guess1 == "L"):
        guess2 = input("U/L: ")
        print(card3)

        if card3 == card2:
            print("isti karti")
            break

        if (card3 > card2 and guess2 == "U") or (card3 < card2 and guess2 == "L"):
            guess3 = input("U/L: ")
            print(card4)

            if card4 == card3:
                print("isti karti")
                break

            if (card4 > card3 and guess3 == "U") or (card4 < card3 and guess3 == "L"):
                print("WIN")
                break
            else:
                print("BUST")
                break
        else:
            print("BUST")
            break
    else:
        print("BUST")
        break
