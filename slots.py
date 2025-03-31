import random

rnd1=random.randrange(1,10)
rnd2=random.randrange(1,10)
rnd3=random.randrange(1,10)
print(rnd1, rnd2, rnd3)
if rnd1 == rnd2 == rnd3:
    print("WIN")
else:
    print("POSKUSI PONOVNO")