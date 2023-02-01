import random
options =['rock','paper','scissors']
computer = random.choices(options)
user = input("Enter your move -->")
if user == computer :
    print("Tie !")
elif user == 'rock' :
    if computer == 'scissors' :
        print("The computer played scissors . So you won !")
    else :
        print("The computer played paper . So you lost !")
elif user == 'paper' :
    if computer == 'scissors' :
        print("The computer played scissors . So you lost !")
    else :
        print("The computer played rock . So you won !")
else:
    if computer == 'paper' :
        print("The computer played paper . So you won !")
    else :
        print("The computer played rock . So you lost !")       