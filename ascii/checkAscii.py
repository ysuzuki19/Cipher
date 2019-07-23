#!/usr/bin/python3
# coding: utf-8

if __name__=='__main__':
    for i in range(256):
        print str(i) + ' : ' + chr(i) + ' : ' + str(ord(chr(i)))
#        print chr(i+ord('A')) + ' : ' + str(i+ord('A'))
#    for i in range(26):
#        print(chr(i+ord('a')), i+ord('a'), end='')

