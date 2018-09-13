import codecs

string1 = '1c0111001f010100061a024b53535009181c'
string2 = '686974207468652062756c6c277320657965'

def xor(data1, data2):
    dec1 = int(data1, 16)
    dec2 = int(data2, 16)
    result = dec1 ^ dec2
    print(hex(result)[2:])

# xor(string1, string2)

# http://www.data-compression.com/english.html
letterFrequencies = [{   "letter" : "a", 
                          "score" : 0.0651738
                    },{   "letter" : "b", 
                        "score" : 0.0124248
                    },{   "letter" : "c", 
                        "score" : 0.0217339
                    },{   "letter" : "d", 
                        "score" : 0.0349835
                    },{   "letter" : "e", 
                        "score" : 0.1041442
                    },{   "letter" : "f", 
                        "score" : 0.0197881
                    },{   "letter" : "g", 
                        "score" : 0.0158610
                    },{   "letter" : "h", 
                        "score" : 0.0492888
                    },{   "letter" : "i", 
                        "score" : 0.0558094
                    },{   "letter" : "j", 
                        "score" : 0.0009033
                    },{   "letter" : "k", 
                        "score" : 0.0050529
                    },{   "letter" : "l", 
                        "score" : 0.0331490
                    },{   "letter" : "m", 
                        "score" : 0.0202124
                    },{   "letter" : "n", 
                        "score" : 0.0564513
                    },{   "letter" : "o", 
                        "score" : 0.0596302
                    },{   "letter" : "p", 
                        "score" : 0.0137645
                    },{   "letter" : "q", 
                        "score" : 0.0008606	
                    },{   "letter" : "r", 
                        "score" : 0.0497563
                    },{   "letter" : "s", 
                        "score" : 0.0515760
                    },{   "letter" : "t", 
                        "score" : 0.0729357
                    },{   "letter" : "u", 
                        "score" : 0.0225134
                    },{   "letter" : "v", 
                        "score" : 0.0082903
                    },{   "letter" : "w", 
                        "score" : 0.0171272
                    },{   "letter" : "x", 
                        "score" : 0.0013692
                    },{   "letter" : "y", 
                        "score" : 0.0145984
                    },{   "letter" : "z", 
                        "score" : 0.0007836
                    },{   "letter" : " ", 
                        "score" : 0.1918182
                    }]

hexEncodedString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def Score(string):
    score = 0
    for character in string:
        for item in letterFrequencies:
            if item["letter"] == character.lower():
                score += item["score"]
    return score

def singlecharXor(ciphertext, key):
    result = b''
    for char in codecs.decode(ciphertext, "hex"):
        result += bytes([char ^ key])
    return result

array = []
for item in range(128):
    value = singlecharXor(hexEncodedString, item)
    plaintext = bytes.decode(value, "utf-8")
    textScore = Score(plaintext)
    textObject = {  "key" : item,
                "score": textScore,
                "plaintext" : plaintext }
    array.append(textObject)
    
newlist = sorted(array, key=lambda k: k['score'], reverse=True) 
print(newlist[0])

    








