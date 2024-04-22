import pyperclip
from os import system
chars = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!§$%&/()=?`´+-*~',.:;<>_"

# wild

def filter_word(word, char_list):
    filtered = ""
    for i in word:
        if i in char_list:
            filtered += i

    return filtered

def encrypt(unfiltered_word, unfiltered_key, char_list):
    global chars
    crypted = ""
    word = filter_word(unfiltered_word, chars)
    key = filter_word(unfiltered_key, chars)
    for i in range(0, len(word)):
        crypted += char_list[(  char_list.index(word[i])  +  char_list.index(key[i % len(key)])) % len(char_list)]

    return crypted

def decrypt(word, key, char_list):
    decrypted = ""
    for i in range(0, len(word)):
        decrypted += char_list[((char_list.index(word[i])-char_list.index(key[i%len(key)]))%len(char_list))]
    return decrypted



running = True
user_input = ""

while running:
    print("encrypt or decrypt? (en / de)")
    while not user_input == "de" and not user_input == "en":
        user_input = input("> ")
        if user_input == "/clear":
            system("clear")
        if user_input == "/quit":
            running = False
            break

    if user_input == "de":
        word = input("type your text - ")
        key = input("type your key - ")
        print("your decrypted text")
        print(decrypt(word, key, chars))
        user_input = input("do you want to copy? (y)").lower()
        if user_input == "y":
            pyperclip.copy(decrypt(word, key, chars))

    if user_input == "en":
        word = input("type your text - ")
        key = input("type your key - ")
        print("Your encrypted text: ")
        print(encrypt(word, key, chars))
        user_input = input("do you want to copy? (y)").lower()
        if user_input == "y":
            pyperclip.copy(encrypt(word, key, chars))


    user_input = ""


# The Password: "1xzsoKrpmVvKjm?-(?"
# The KEy: hurensohn










