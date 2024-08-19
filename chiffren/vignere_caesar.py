# Nils Thomas
# 19.08.2024
# Implement Caesar and Vignere

def chiffrieren_caesar(text, key):
    alph = "abcdefghijklmnopqrstuvwxyz"
    if type(key) == str:
        keynum = alph.find(key)
        #print("DEBUG keynum: ", keynum)
    else:
        keynum = key
    cipher = ""
    for i in range(len(text)):
        letternum = alph.find(text[i])
        #print("DEBUG letternum: ", letternum)
        #print("DEBUG Sum: ", letternum + keynum, len(alph))
        if (letternum + keynum) >= len(alph):
            #print("FALL 1")
            newletter = alph[letternum + keynum - len(alph)]
        else:
            newletter = alph[letternum + keynum]
        cipher += newletter
    return cipher

def chiffrieren_vignere(text, key):
    len_kt = len(text)
    len_key = len(key)
    geheimtext = ""
    for i in range(len_kt):
        #print(i)
        caesar_key = key[i%len_key]
        geheimtext += chiffrieren_caesar(text[i], caesar_key)
    return geheimtext


print(chiffrieren_vignere("informatik", "sarnen"))