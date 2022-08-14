alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
play=True
    
def caesar(text,shift,direction):
    end_text=''
    text_shift=0    

    for i in text:
        if direction=="decode":
            text_shift=alphabet.index(i)-shift
            if text_shift<0:
                text_shift+=26       #access again from z-a and 'z' is at index 25 so 26 is added.
        else:
            text_shift=alphabet.index(i)+shift
            if text_shift>25:
               text_shift-=26       #access again from a-z and 'a' is at index 0 so 26 is substracted.

        end_text+=alphabet[text_shift]
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



