#Return alphabets (lowercase)
def alphabets():
    return "abcdefghijklmnopqrstuvwxyz"

#Return number of alphabets
def number_of_alphabets():
    return len(alphabets())

#This function return true if and only if the character c is an alphabetic character
def is_alphabetic_char(c):
    return (c.lower() in alphabets())

#This function converts a single character into its numeric value
def char_to_num(c):
    letters = alphabets()
    return letters.index(c.lower())

#this function return the character corresponding to x mod 26 in the English alphabet
def num_to_char(x):
    letters = alphabets()
    return letters[x % number_of_alphabets()]

def CaesarEncrypt(key, string):
    EncryptedString = ""
    for x in string:
        if(is_alphabetic_char(x)):
            y = char_to_num(x)
            EncryptedString += num_to_char(y + key)
        else:
            EncryptedString += x
    # print(EncryptedString)
    return EncryptedString

def CaesarDecrypt(key, string):
    DecryptedString = ""
    for x in string:
        if(is_alphabetic_char(x)):
            y = char_to_num(x)
            DecryptedString += num_to_char(y - key)
        else:
            DecryptedString += x
    # print(DecryptedString)
    return DecryptedString

# CaesarDecrypt(3, CaesarEncrypt(3, "abc#defgz"))

def CaesarBrutefoce(ciphertext, substring=""):
    for x in range(1,26):
        if (substring != ""):
            if substring in CaesarDecrypt(x, ciphertext):
                print(str(x) + ": " + CaesarDecrypt(x, ciphertext))
        else:
            print(str(x) + ": " + CaesarDecrypt(x, ciphertext))

CaesarBrutefoce("Uizs mv Zwuiv hqrv abwu pipi omxzivsb", "geprankt")

