
class Vigenere_Message():

    alphabet_r = {\
        0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n", \
        14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}

    def __init__(self,array):
        self.int_array = array
        self.length = len(array)

    def encrypt(self,K,offset=0):
        C = list(self.int_array)
        for i in range(0,self.length):
            C[i] = (self.int_array[i]+K.int_array[(i+offset)%K.length])%26
        return Vigenere_Cipher(C)

    def string(self):
        return "".join([Vigenere_Message.alphabet_r[num] for num in self.int_array])

class Vigenere_Cipher():

    alphabet_r = {\
        0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n", \
        14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}


    def __init__(self,array,offset=0):
        self.int_array = array
        self.offset = offset
        self.length = len(array)

    def decrypt(self,K):
        M = list(self.int_array)
        for i in range(0,self.length):
            M[i] = (self.int_array[i]-K.int_array[(i+self.offset)%K.length])%26
        return Vigenere_Message(M)

    def string(self):
        return "".join([Vigenere_Cipher.alphabet_r[num] for num in self.int_array])


class Vigenere_Key():

    alphabet_r = {\
        0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n", \
        14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}

    def __init__(self,length):
        self.length = length
        self.int_array = [0]*length
        self.overflowed = 0

    #lexographic increment, with "around the block" overflow implemented
    def increment(self):
        index = self.length - 1
        self.int_array[index] += 1
        while(self.int_array[index] > 25):
            self.int_array[index] = 0
            index -= 1
            if index < 0:
                index = self.length - 1
                self.overflowed += 1
            self.int_array[index] += 1

    def string(self):
        return "".join([Vigenere_Key.alphabet_r[num] for num in self.int_array])


