# Orhun Dogan
# October 11th 2020
# This program encryots/decrypts texts


def encrypt_letter(c,offset):
    ascii_index  = ord(c) - offset
    if ascii_index <65:
        ascii_index  +=26
    return chr(ascii_index)

def encrypt(text,offset):
    s=""
    for letter in text:
        s+=encrypt_letter(letter,offset)
    return s    

def break_cipher(text):
    text = text.upper()
    frequency={}            # Initializing Dictionary
    for letter in text:
        if letter in frequency:
            frequency[letter] +=1       # Update if the letter is in the dictionary
        else:
            frequency[letter] =1            # Add the letter if it is new
    
    
    max_frequency=0
    max_letter=""
    
    for keyword in frequency:
        if frequency[keyword]>max_frequency:
            max_frequency=frequency[keyword]
            max_letter=keyword                      # Finding the most used letter
    
    ascii_max=ord(max_letter)
    ascii_e=ord('E')
    offset = abs(ascii_max-ascii_e)
    de_text= encrypt(text,offset)
    return de_text
     
a="Letter frequency is simply the amount of times letters of the alphabet appear on average in written language."
a=a.upper()     # Turns the text UPPERCASE
a = a.replace(" ","")       # NO SPACES
a = a.replace(".","")       # NO .
a=encrypt(a,13)         # Encrypting a
print(a + "\n")

    
print(break_cipher(a))
    
