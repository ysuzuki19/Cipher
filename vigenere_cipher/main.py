#!/usr/bin/python3
# coding: utf-8

def polybius_encryption(txt,key):
    enc = ""
    for i in range(len(txt)):
        enc += chr(ord(txt[i]) + ord(key[i%len(key)])-ord("a"))
    return enc

def polybius_decryption(txt,key):
    dec = ""
    for i in range(len(txt)):
        dec += chr(ord(txt[i]) - ord(key[i%len(key)])+ord("a"))
    return dec

if __name__=='__main__':
    key = "hand"

    txt = "i am a human."
    print("plane text : " + txt)

    txt = polybius_encryption(txt,key)
    print("encry text : " + txt)

    txt = polybius_decryption(txt,key)
    print("decry text : " + txt)

