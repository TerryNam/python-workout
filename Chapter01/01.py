import random


def guessing_game():
    number = random.randint(0,100)

    while True:
     guess_num = int(input('Enter thoughts:')) 

     if guess_num==number:
        break
     elif guess_num<number:
           print(f'Too low') 
     else :
           print(f'Too High')

guessing_game()