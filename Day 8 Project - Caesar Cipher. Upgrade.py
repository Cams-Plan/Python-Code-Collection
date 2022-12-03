## Upgrade to my original caesar cipher python script: this version accomodates for space separated phrases and sentances while maintaining 
 # the spacing when returning the ciphertext
    ### WORK IN PROGRESS - NEED TO SOLVE HOW TO STOP ACCUMULATION OF LIST INSERTS/ APPENDS ###

def caesar_phrase():
    ## A function that encrypts/decrypts input 'msg' by shifting characters a specific amount ('shift_num') against an 'alphabet' list.
    
    # Alphabet list for co-ordinating shift of letters
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l'
    , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Data collection for encryption or decryption
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    msg = input("Type your message:\n").lower()
    shift_num = int(input("Type the shift number:\n"))

    new = msg.split()
    reference = []
    if (type(new) is list) == True and len(new) > 1:
        print('handling multiple words') 
        msg_len = len(new)
        if direction == "encode" or "e" in direction[0]:
            cipher_text = ""
            for position in range(msg_len):
                print(position)
                for letter in new[position]:
                    move = int(alphabet.index(letter) + shift_num)
                    cipher_text += alphabet[move]
                reference.insert(position,cipher_text)
                print(reference)
        print(f"The encoded text is {reference}")
                    
#     # if statements for encryption/ decryption/ accounting for unwanted input
#     if direction == "encode" or "e" in direction[0]:
#         cipher_text = ""
#         for position in range(msg_len):
#             letter = msg[position]
#             for character in letter:
#                 move = int(alphabet.index(letter) + shift_num)
#                 cipher_text += alphabet[move]
#         print(f"The encoded text is {cipher_text}")

#     elif direction == "decode" or "d" in direction[0]:
#         decipher = ""
#         for position in range(msg_len):
#             letter = msg[position]
#             move = int(alphabet.index(letter) - shift_num)
#             decipher += alphabet[move]
#         print(f"The encoded text is {decipher}")
#     else:
#         print("'ENCODE' and 'DECODE' are the only available options, please try again.")

caesar_phrase()
# ## allow for messages with spaces by using the .split() method
