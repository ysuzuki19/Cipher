#!/usr/bin/python3
# coding: utf-8

def caesar_encryption(txt):
    enc = ""
    for i in range(len(txt)):
        enc += chr(ord(txt[i])-1)
    return enc

def caesar_decryption(txt):
    dec = ""
    for i in range(len(txt)):
        dec += chr(ord(txt[i])+1)
    return dec

if __name__=='__main__':
    txt = "i am human."
    print("plane text : " + txt)

    txt = caesar_encryption(txt)
    print("crypt text : " + txt)

    txt = caesar_decryption(txt)
    print("plane text : " + txt)

