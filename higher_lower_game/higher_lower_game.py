import logo 
from db import data
import os
from time import sleep

i,j=0,1
play=True
score=0

print(logo.art)

while play:
    if data[i]['follower_count']>data[j]['follower_count']:
        winner='A'
    else:
        winner='B'
    print(f"Compare A: {data[i]['name']}, a {data[i]['description']}, from {data[i]['country']}")
    print(logo.vs)
    print(f"Against B: {data[j]['name']}, a {data[j]['description']}, from {data[j]['country']}")
    user_vote=input("Who has more followers? Type 'A' or 'B':")
    if user_vote==winner:
        score+=1
        i=j
        j=j+1
        
    else:
        play=False
        print(f"Sorry, that's wrong. Final Score: {score}")
    sleep(2)
    os.system('cls')
