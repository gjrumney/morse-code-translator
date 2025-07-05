morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', 
    ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', 
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', 
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', 
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', 
    '@': '.--.-.'
}

# decodes ENG input
def decode_eng(message):
    post = []
    
    for p in message:
        if p != ' ':
            key = p.upper()
            post.append(morse_code_dict[key])
        else:
            space = p.replace(' ', '/')
            post.append(space)

    return post

# delivers MORSE output
def deliver_morse(post):
    print(' '.join(post))
    
# decodes MORSE input
def decode_morse(message):
    post = []
    
    for p in message:
        if p != '/':
            for key, val in morse_code_dict.items():
                if val == p:
                    letter = key
                    post.append(letter)
        else:
            space = p.replace('/', ' ')
            post.append(space)
    
    return post

# delivers ENG output
def deliver_eng(post):
    print(''.join(post))            

# controls ENG -> MORSE sequence
def eng_morse(message):
    print('\n')
    post = decode_eng(message)
    morse = deliver_morse(post)
    print('\n')

# controls MORSE -> ENG sequence
def morse_eng(message):
    print('\n')
    message = error_handler(message)
    post = decode_morse(message)
    eng = deliver_eng(post)
    print('\n')

# a seemingly superfluous attempt at error handling
def error_handler(message):
    
    for m in message:
        for val in morse_code_dict.items():
            if val != m:
                print('This message is invalid.')
                return None


   
def main():
    while True:
        eng_or_morse = input('Type your message: ')
        
        message = list(eng_or_morse)

        '''
        Process determines whether the language is in morse or English
        It splits the input into a list and measures the length of its first item
        If the item is one it might be 'E:.', so it checks - if not, it is still English
        '''
        
        if len(eng_or_morse[0]) == 1:
            if eng_or_morse[0] == '.':
                message = str(''.join(message))
                message = message.split(' ')
                morse_eng(message)
            else:
                eng_morse(message)
        else:
            morse_eng(message)  

if __name__ == '__main__':
    main()

        
    
    
