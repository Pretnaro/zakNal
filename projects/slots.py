import random

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