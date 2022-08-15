import logo
import random

print(logo.art)
flag=0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number=random.randint(1,100)
print("no.=",number)
level=input("Choose a difficulty. Type 'easy' or 'hard':")

if level=='easy':
    attempts=10
elif level=='hard':
    attempts=5

print(f"You have {attempts} attempts remaining to guess the number.")

for attempt in range(1,attempts+1):
    guess=int(input("Make a guess:"))
    if guess!=number:
        if guess<number:
            print("Too low")
        elif guess>number:
            print("Too high")
        print("Guess again")
        left_attempts=attempts-attempt
        print(f"You have {left_attempts} remaining to guess the number.")
    else:
        flag=1
        break
if flag==1:       
    print("You got it ! The answer was {}".format(number))
