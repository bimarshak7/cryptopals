from cryptopals.helper import *


def q1():
    '''#Qn 1'''
    rw = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print(hex_b64(rw))


def q2():
    '''#Qn 2'''
    s1 = '1c0111001f010100061a024b53535009181c'
    s2 = '686974207468652062756c6c277320657965'
    #print(strxor(s1,s2))
    #print(help(strxor))
    print(xor_hex(s1, s2))
    

