import enchant
import sys
import requests

alphabet_r = {\
        0:"a",
        1:"b",
        2:"c",
        3:"d",
        4:"e",
        5:"f",
        6:"g",
        7:"h",
        8:"i",
        9:"j",
        10:"k",
        11:"l",
        12:"m",
        13:"n",
        14:"o",
        15:"p",
        16:"q",
        17:"r",
        18:"s",
        19:"t",
        20:"u",
        21:"v",
        22:"w",
        23:"x",
        24:"y",
        25:"z"}

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

def array_to_string(array):
    return "".join([alphabet_r[num] for num in array])

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


d = enchant.Dict("en_US")
def crack_cipher(key_len,cipher):
    key = Vigenere_Key(key_len)
    c_words = cipher.split()
    c_words = [string_to_array(word) for word in c_words]
    offsets = get_offsets(c_words)
    word_off_pairs = {}
    for i in range(0,len(c_words)):
        word_off_pairs[offsets[i]] = c_words[i]
    word_off_pairs = sort_by_len(word_off_pairs)
    print(word_off_pairs)
    print("")
    while not key.overflowed:
        all_are_words = True
        for i in range(0,len(word_off_pairs)):
            word = word_off_pairs[i][1]
            offset = word_off_pairs[i][0]
            index = 0
            result = key.decrypt(word,offset=offset)
            message = array_to_string(result)
            if not d.check(message):
                all_are_words = False
                break
        if all_are_words:
            print("")
            return key
        key = increment_key(key)
    print("\r")

class Vigenere_Key():
    #TODO: this class could be adjusted to work for arbitrary alphabet size. but for now, let's hardcode 26 (a-z)
    def __init__(self,length):
        self.length = length
        self._key = [0]*length
        self.overflowed = 0

    #lexographic increment
    def increment(self):
        index = self.length - 1
        key[index] += 1
        while(self._key[index] > 25):
            self._key[index] = 0
            index -= 1
            if index < 0:
                index = self.length - 1
                self.overflowed += 1
            self._key[index] += 1

    def decrypt(self,C,offset=0):
        kl = len(self._key)
        M = list(C)
        for i in range(0,len(C)):
            M[i] = (C[i]-K[(i+offset)%kl])%26
        return M

    def encrypt(self,M,offset=0):
        kl = len(self._key)
        C = list(M)
        for i in range(0,len(M)):
            C[i] = (M[i]+K[(i+offset)%kl])%26
        return C

    def string(self):
        return "".join([alphabet_r[num] for num in self._key])



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
