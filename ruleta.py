import random

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
