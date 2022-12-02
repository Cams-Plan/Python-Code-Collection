## Create a Ceasar Cipher that encrypts and decrypts any message

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l'
, 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(char, shift_no):
    ##Function that encrypts input 'char' by shifting characters a specific amount against an existing alphabet var.
    char_len = len(char)
    cipher_text = ""
    for position in range(char_len):
        letter = char[position]
        move = int(alphabet.index(letter) + shift_no)
        cipher_text += alphabet[move]
    print(f"The encoded text is {cipher_text}")

#1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher, shift_no):
    cipher_len = len(cipher)
    decipher = ""
    for position in range(cipher_len):
        letter = cipher[position]
        move = int(alphabet.index(letter) - shift_no)
        decipher += alphabet[move]
    print(f"The decoded text is {decipher}")

##ceaser cipher script
#collect and direct data input paths based on encoding or decoding
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#control for unwanted inputs and slight input errors.
if direction == "encode" or "e" in direction[0]:
    plaintext = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(char=plaintext, shift_no=shift)
elif direction == "decode" or "d" in direction[0]:
    coded_text = input("Type your coded message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(cipher=coded_text, shift_no=shift)
else:
    print("'ENCODE' and 'DECODE' are the only available options, please try again.")
