print("Welcome to the Word Guessing Game")
word=input("Enter word to guess \n")
count=0
ans=[]
word_list=list(word)
for i in word:
    ans.append('_')
while True:
    guess=input("Guess the letter \n")
    if guess in word:
        print('correct:')
        for j in range(0,len(word_list)):
            if guess == word_list[j]:
                ans[j]=guess
        print(" ".join(ans))
        if ans == word_list:
            print("WoW: you have correctly guessed the word!! " + word)
            break
    else:
        if count > 6:
            print("Ohh you exceded the chances!!")
        count+=1
        print(str(6-count) + ' chances left\n')
