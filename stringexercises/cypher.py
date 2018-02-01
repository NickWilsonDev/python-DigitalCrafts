# cypher.py
import string


alphabet = list(string.lowercase)

print alphabet

def prompt_message():
    message = raw_input("Please input a message you would like decrypted...\n")
    return message

def prompt_key():
    key = abs(int(raw_input("Please input number to shift by...")))
    key = key % len(alphabet)
    print key
    return key

def caesar_encrypt(msg, key):
    msg_list = list(msg)
    new_list = []
    for letter in msg_list:
        if letter == ' ':
            new_list.append(letter)
        else:
            new_char = alphabet[alphabet.index(letter) - key]
            new_list.append(new_char)
    new_message = ''.join(new_list)
    return new_message

print """Welcome to the Caesar cypher, you will be prompted for a message
         and a key(number to shift alphabet """
msg = prompt_message()
key = prompt_key()
print caesar_encrypt(msg, key)
