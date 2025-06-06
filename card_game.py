#This is a card game, where user and computer will pick cards until they want whoever is having sum of the cards greater than other will win.

import random
comp_card=[]
user_card=[]
comp_sum=0
user_sum=0
while True:
    user_num=int(input("Enter card num (1 to 10) \n"))
    level=input("Enter if you want to continue playing y or n? \n").lower()
    comp_card.append(random.randint(1,10))
    user_card.append(user_num)
    
    if level=='n':
        for i in range(len(comp_card)):
            comp_sum+=comp_card[i]
            user_sum+=user_card[i]
        break
print(f'Comp sum of {comp_card}={comp_sum}')
print(f'User sum of {user_card}={user_sum}')

if comp_sum>user_sum:
    print(f'Computer won, as sum of the cards is {comp_sum} which is greater than user')
else:
    print(f'User won, as sum of the cards is {user_sum} which is greater than computer !!')

