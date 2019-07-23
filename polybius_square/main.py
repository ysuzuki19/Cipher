#!/usr/bin/python3
# coding: utf-8

#####################
## my square ########
#####################
##   1  2  3  4  5 ##
## 0    ,  .  ?  a ##
## 1 b  c  d  e  f ##
## 2 g  h  i  j  k ##
## 3 l  m  n  o  p ##
## 4 q  r  s  t  u ##
## 5 v  w  x  y  z ##
#####################
#####################

def polybius_encryption(txt):
    col = 5
    row = 5
    enc = ""
    for i in range(len(txt)):
        if txt[i] == " ":
            enc += "01 "
        elif txt[i] == ",":
            enc += "02 "
        elif txt[i] == ".":
            enc += "03 "
        elif txt[i] == "?":
            enc += "04 "
        elif txt[i] == "a":
            enc += "05 "
        else:
            enc += str((ord(txt[i])-ord("b"))//col + 1) + str((ord(txt[i])-ord("b"))%col + 1)+ " "
    return enc

def polybius_decryption(txt):
    col = 5
    row = 5
    dec = ""
    for i in range(0, len(txt), 3):
        if txt[i] == "0":
            if txt[i+1] == "1":
                dec += " "
            elif txt[i+1] == "2":
                dec += ","
            elif txt[i+1] == "3":
                dec += "."
            elif txt[i+1] == "4":
                dec += "?"
            else:
                dec += "a"
        else:
            dec += chr((int(txt[i])-1)*5 + (int(txt[i+1])-1) + ord("b"))
    return dec

if __name__=='__main__':
    txt = "i am a human."
    print("plane text : " + txt)

    txt = polybius_encryption(txt)
    print("encry text : " + txt)

    txt = polybius_decryption(txt)
    print("decry text : " + txt)

