#Mohammad Mishal S. Noroña | BSCPE 1-5 | PROBLEM 3 - The Vigenère Cipher
# Import color module
import colorama
from colorama import Fore, Back, Style
colorama.init()
# add introduction
print("")
print(Fore.LIGHTYELLOW_EX + "The Vigenère Cipher Converter".center(40," ") )
print(Fore.CYAN + "By: Mishal Noroña".center(40," ") )
# asks the user for the plaintext (all uppercase letters, no spaces)
message = input (Fore.RESET + 'Enter your Message: ' + Fore.BLUE).upper().replace(' ','')      #(all uppercase letters, no spaces)
key = input (Fore.RESET + 'Enter your Key: ' + Fore.BLUE).upper().replace(' ','')              #(all uppercase letters, no spaces)
# define user's input
def input_key(message, key):
    out_key = ''
    x = 0
    for ltr in message:
        if ltr.isalpha():
            out_key += key[x % len(key)]
            x += 1
        else:
            out_key += ' '
    return out_key
# formula for encryption 
# encrypt the message
# decrypt the message
# add loading time
# add animation
# print output