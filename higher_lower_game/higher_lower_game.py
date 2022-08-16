import logo 
from db import data
import os
from time import sleep
import random

play=True
score=0

print(logo.art)

while play:  
    account_a=random.choice(data)
    account_b=random.choice(data)
    if account_a['follower_count']>account_b['follower_count']:
        winner='A'
    else:
        winner='B'
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(logo.vs)
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
    user_vote=input("Who has more followers? Type 'A' or 'B':")
    if user_vote==winner:
        score+=1
        
    else:
        play=False
        print(f"Sorry, that's wrong. Final Score: {score}")
    sleep(2)
    os.system('cls')
