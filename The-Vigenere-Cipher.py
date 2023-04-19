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
def enc_dec_ltr(message_ltr, key_ltr, process='encrypt'):
    if message_ltr.isalpha():
        first_letter = 'a'
        if message_ltr.isupper():
            first_letter = 'A'

        old_ltr = ord(message_ltr) - ord(first_letter)
        key_ltr = ord(key_ltr.lower()) - ord('a')

        if process == 'encrypt':
            new_ltr = (old_ltr + key_ltr) % 26
        else:
            new_ltr = (old_ltr - key_ltr + 26) % 26
        return chr(new_ltr + ord(first_letter))
    return message_ltr
# encrypt the message
def encrypt(message, key):
    cipher_txt = ''
    out_key = input_key(message, key)
    for message_ltr, key_ltr in zip(message, out_key):
        cipher_txt += enc_dec_ltr(message_ltr, key_ltr)
    return cipher_txt

cipher_txt = encrypt(message, key)
# decrypt the message
def decrypt(cipher_txt, key):
    message = ''
    out_key = input_key(cipher_txt, key)
    for cipher_txt_ltr, key_ltr in zip(cipher_txt, out_key):
        message += enc_dec_ltr(cipher_txt_ltr, key_ltr, process='decrypt')
    return message

decrypted_message = decrypt(cipher_txt, key)
# add loading time
# add animation
# print output