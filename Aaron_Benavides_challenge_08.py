'''

This program converts text to Morse code.
Written by: Aaron Benavides

'''

def converter(text): #store tuples and convert/return text in this function
    
    morse = (' ', '--..--', '.-.-.-', '..--..',
             '-----', '.----', '..---', '...--',
             '....-', '.....', '-....', '--...',
             '---..', '----.', '.-', '-...', '-.-.',
             '-..', '.', '..-.', '--.', '....', '..',
             '.---', '-.-', '.-..', '--', '-.', '---',
             '.--.', '--.-', '.-.', '...', '-', '..-',
             '...-', '.--', '-..-', '-.-', '--..')
    
    character = (' ', ',', '.', '?', '0', '1', '2', '3',
                 '4', '5', '6', '7', '8', '9', 'A', 'B',
                 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    
    compiler = [] #list that stores user text to be converted
    
    for ch in text: #user input validation
        if ch not in character:
            result = 'invalid characters in text. Try again.'
            return (result)
            
    for ch in text: #each character in user input gets converted and stored in 'compiler'
        if ch in character:
            charindx = character.index(ch)
            compiler.append(morse[charindx])
            
            
    result = ' '.join(compiler)
    #' '.join() concatenates elements in a list with a space between elements
    return (result)
    
    
    
def user_text():  #gather user input in this function
    
    while True:
        text = input('\nenter text or type "STOP" to exit: ')
        result = converter(text.upper())
    
        if text == "STOP": #sentinel
            break
        else:
            print(result)


if __name__ == "__main__":
    print("\nHello, this program converts text to binary")
    user_text()