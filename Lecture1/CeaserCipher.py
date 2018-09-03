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
    return letters[x % number_of_alphabets]