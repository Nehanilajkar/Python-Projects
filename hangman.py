import random
word_list = ["apple", "baboon", "camel","dbr"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word=list(random.choice(word_list))

display=''
n=0
m=0
flag=0
blank=[]
pattern=['''
           ____
           |   |
           |   O
           |
           |
           |
           |
          ---''','''
           ____
           |   |
           |   O
           |   |
           |
	   |
           |
          ---''',
		'''
           ____
           |   |
           |   O
           |  /|
           |
           |
           |
          ---''',
                '''
           ____
           |   |
           |   O
           | //|
           |
           |
           |
          ---''',
		'''
           ____
           |   |
           |   O
           | //|
           |  /
           | 
           | 
          ---''',
		'''
           ____
           |   |
           |   O
           | //|
           |  //
           |
           |
          ---''']
		

for i in range(len(chosen_word)):
    blank.append("_")
display='_ '.join(blank)
print(display)

while n<len(chosen_word):
        guess=input("Guess a letter  ").lower()
        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if guess==chosen_word[i]:
                    blank[i]=guess
            print(" ".join(blank))
        else:
            print(pattern[m])
            m+=1
            if m==6:
                break
 
        if "_" not in blank:
            break

if "_" not in blank:
    print("You win")
else:
    print("You lost")

        
