#!/usr/bin/python3
# coding: utf-8

def transposition_encryption(txt):
    cel = 3
    enc = ""
    for j in range(cel):
        for i in range((len(txt)//cel)+1):
            if cel*i+j < len(txt):
                enc += txt[cel*i+j]
    return enc

def transposition_decryption(txt):
    cel = 3
    if len(txt)%cel == 0:
        quotient = len(txt)//cel
    else:
        quotient = len(txt)//cel + 1
    dec = ""
    for j in range(quotient):
        for i in range(len(txt)//quotient+1):
            if quotient*i+j < len(txt):
                dec += txt[quotient*i+j]
    return dec

if __name__=='__main__':
    txt = "i am a perfect human."
    print("plane text : " + txt)

    txt = transposition_encryption(txt)
    print("encry text : " + txt)

    txt = transposition_decryption(txt)
    print("decry text : " + txt)

