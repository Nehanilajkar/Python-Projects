import random
names=["Virat","Neha","Anushka","Kiara","Siddhart"]
score=0
a=random.choice(names)
b=random.choice(names)
while True:
    if a==b:
        print(b)
        b=random.choice(names)
        print(b)
    guess=input(f'Guess who has more instagram followers A={a} or B={b} \n').lower()
    print(guess)
    a_followers=random.randint(1,100)
    b_followers=random.randint(1,100)
    print(a_followers,b_followers)
    if a_followers>b_followers:
        if guess=='a':
            score+=1
            print("You are correct !!")
        else:
            print(f"Your guess is wrong,{b} has {b_followers} and {a} has {a_followers}.  !!")
            break
    else:
        if guess=='b':
            score+=1
            print("You are correct !!")
        else:
            print(f"Your guess is wrong,{b} has {b_followers} and {a} has {a_followers}.  !!")
            break
    print(f"You score is {score}")
