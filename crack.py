import enchant
import sys
import requests
from cryptolib.crypto import Vigenere_Key

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
    for i in range(0,len(c_words)):
        word_off_pairs[offsets[i]] = c_words[i]
    word_off_pairs = sort_by_len(word_off_pairs)
    ciphers = []
    for i in range(0,len(c_words)):
        ciphers.append(Vigenere_Cipher(word_off_pairs[i][1],word_off_pairs[i][0])
        #HERE
    return ciphers

d = enchant.Dict("en_US")
def crack_cipher(key_len,cipher):
    key = Vigenere_Key(key_len)
    cipher_words = get_ciphers_shortest_word_first(cipher)
    print(word_off_pairs)
    print("")
    while not key.overflowed:
        all_are_words = True
        for i in range(0,len(word_off_pairs)):
            word = word_off_pairs[i][1]
            offset = word_off_pairs[i][0]
            index = 0
            result = key.decrypt(word,offset=offset)
            message = key.string()
            message = array_to_string(result)
            if not d.check(message):
                all_are_words = False
                break
        if all_are_words:
            print("")
            return key
        key = increment_key(key)
    print("\r")



C = "ccoheal ieu w qwu tcb"
key_len = 8
key = crack_cipher(key_len,C)
print("------")
print(key)
print(array_to_string(key))
if not key: quit()
c_words = C.split()
c_words = [string_to_array(word) for word in c_words]
offsets = get_offsets(c_words)
message = ""
for i in range(0,len(c_words)):
    temp = key.decrypt(c_words[i],offsets[i])
    message += array_to_string(temp)+" "
message = message.strip()
print("key: "+array_to_string(key))
print("message: "+message)
