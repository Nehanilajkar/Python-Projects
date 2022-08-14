import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
play=True
    
print(logo.art)
def caesar(text,shift,direction):
    end_text=''
    text_shift=0    
    
    for i in text:
        if i.isalpha():    
            if direction=="decode":
                sub_shift=alphabet.index(i)-shift
                text_shift=sub_shift%26       #to access alphabets if shift >26
  
            else:
                add_shift=alphabet.index(i)+shift
                text_shift=add_shift%26
            letter=alphabet[text_shift]
        else:
            letter=i   
        end_text+=letter
    print(f"The {direction}d text is {end_text}.")
    

while play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(shift=shift,direction=direction,text=text)
    replay=input("Do you want to play again ?'y' or 'n'")
    if replay=='y':
        play=True
    else:
        print("Thanks for playing , visit again!")
        play=False




