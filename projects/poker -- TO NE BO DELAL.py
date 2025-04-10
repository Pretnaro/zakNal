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
    firstint = str(input("Call, Raise, Fold: "))
    if firstint == "call":
        break
    elif firstint == "raise":
        chip = int(input("Input number for raise: "))
        break
    elif firstint == "fold":
        break



dealerCard1 = random.randrange(2,15)
if dealerCard1 == 11:
    print(f"First card: J")
elif dealerCard1 == 12:
    print(f"First card: Q")
elif dealerCard1 == 13:
    print(f"First card: K")
elif dealerCard1 == 14:    
    print(f"First card: A")
else:
    print(f"First card: {dealerCard1}")
dealerCard2 = random.randrange(2,15)
if dealerCard2 == 11:
    print(f"Second card: J")
elif dealerCard2 == 12:
    print(f"Second card: Q")
elif dealerCard2 == 13:
    print(f"Second card: K")
elif dealerCard2 == 14:    
    print(f"Second card: A")
else:
    print(f"Second card: {dealerCard2}")
dealerCard3 = random.randrange(2,15)
if dealerCard3 == 11:
    print(f"Third card: J")
elif dealerCard3 == 12:
    print(f"Third card: Q")
elif dealerCard3 == 13:
    print(f"Third card: K")
elif dealerCard3 == 14:    
    print(f"Third card: A")
else:
    print(f"Third card: {dealerCard3}")