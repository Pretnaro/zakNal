import random

card1 = random.randrange(2,15)
card2 = random.randrange(2,15)
if card1 == 11:
    print(f"Your card: J")
elif card1 == 12:
    print(f"Your card: Q")
elif card1 == 13:
    print(f"Your card: K")
elif card1 == 14:    
    print(f"Your card: A")
else:
    print(f"Your card: {card1}")

if card2 == 11:
    print(f"Your card: J")
elif card2 == 12:
    print(f"Your card: Q")
elif card2 == 13:
    print(f"Your card: K")
elif card2 == 14:    
    print(f"Your card: A")
else:
    print(f"Your card: {card2}")

p21 = random.randrange(2,15)
p22 = random.randrange(2,15)

while True: 
    while True:
        firstint = str(input("Call, Raise, Fold: "))
        if firstint == "call":
            break
        elif firstint == "raise":
            chip = int(input("Input number for raise: "))
        elif firstint == "fold":
            break
        break



dealerCard1 = random.randrange(2,15)
dealerCard1 = random.randrange(2,15)
dealerCard1 = random.randrange(2,15)