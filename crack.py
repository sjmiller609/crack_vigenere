import enchant
import sys
import requests
from cryptolib.crypto import Vigenere_Key, Vigenere_Cipher, Vigenere_Message

alphabet = {\
        "a":0,
        "b":1,
        "c":2,
        "d":3,
        "e":4,
        "f":5,
        "g":6,
        "h":7,
        "i":8,
        "j":9,
        "k":10,
        "l":11,
        "m":12,
        "n":13,
        "o":14,
        "p":15,
        "q":16,
        "r":17,
        "s":18,
        "t":19,
        "u":20,
        "v":21,
        "w":22,
        "x":23,
        "y":24,
        "z":25}

def string_to_array(string):
    result = []
    for char in string:
        result.append(alphabet[char])
    return result

def get_offsets(words):
    offsets = []
    counter = 0
    for i in range(0,len(words)):
        offsets.append(counter)
        counter += len(words[i])
    return offsets

#this doesn't need to be fast.
def sort_by_len(pairs):
    if len(pairs) == 0: return []
    results = []
    shortest_len = 10000000000000000
    shortest = None
    for key in pairs:
        if len(pairs[key]) < shortest_len:
            shortest_len = len(pairs[key])
            shortest = key
    temp = [[shortest,pairs[shortest]]]
    pairs.pop(shortest)
    return temp+sort_by_len(pairs)

def get_ciphers_shortest_word_first(cipher):
    c_words = cipher.split()
    c_words = [string_to_array(word) for word in c_words]
    offsets = get_offsets(c_words)
    word_off_pairs = {}
    for i in range(0,len(c_words)):
        word_off_pairs[offsets[i]] = c_words[i]
    word_off_pairs = sort_by_len(word_off_pairs)
    ciphers = []
    for i in range(0,len(c_words)):
        ciphers.append(Vigenere_Cipher(word_off_pairs[i][1],word_off_pairs[i][0]))
    return ciphers

def get_ciphers(cipher):
    c_words = cipher.split()
    c_words = [string_to_array(word) for word in c_words]
    offsets = get_offsets(c_words)
    word_off_pairs = []
    for i in range(0,len(c_words)):
        word_off_pairs.append([offsets[i],c_words[i]])
    ciphers = []
    for i in range(0,len(c_words)):
        ciphers.append(Vigenere_Cipher(word_off_pairs[i][1],word_off_pairs[i][0]))
    return ciphers

english_dict = enchant.Dict("en_US")
def crack_cipher(key_len,cipher,key=None):

    #it's a performance improvement to check the smallest word first, because it's the fastest to decrypt.
    # and we can more quickly eliminate keys that don't decrypt the small cipher words into real english words
    cipher_words = get_ciphers_shortest_word_first(cipher)

    #if we are not starting from an existing key, instantiate a new key object
    if not key:
        key = Vigenere_Key(key_len)

    while not key.overflowed:
        all_are_words = True
        for i in range(0,len(cipher_words)):
            #decrypt and see if it's a word or not
            if not english_dict.check(cipher_words[i].decrypt(key).string()):
                all_are_words = False
                break
        if all_are_words:
            return key
        key.increment()

    #if the key overflows, then we have checked the entire key space.
    return None

def main():
    #C = "ccoheal ieu w qwu tcb"
    #C = "ccoheal"
    C = "niayhc kyryqydmakpji xfsw robr"
    key_len = 0
    max_key_len = 6
    key = None
    while not key and key_len <= max_key_len:
        key_len += 1
        print("cracking key space with |K| = "+str(key_len))
        key = crack_cipher(key_len,C)

    if key_len > max_key_len:
        print("key space exhausted. failed to crack cipher with max key length as "+str(max_key_len))
        quit()

    print("------")
    print("key: "+key.string())
    c_words = get_ciphers(C)
    message = ""
    for i in range(0,len(c_words)):
        message += c_words[i].decrypt(key).string()+" "
    message = message.strip()

    print("message: "+message)

if __name__ == "__main__":
    main()
