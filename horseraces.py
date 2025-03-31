horseNumber = int(input("Input horse number: "))
videoNumber = random.randrange(5)
if horseNumber == videoNumber:
    print("YOU WIN")
else:
    print("YOU LOST")