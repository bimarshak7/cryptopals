import base64

def hex_b64(s):
    '''Takes hex string and encode back to base64 string'''
    plain = bytes.fromhex(s)
    return base64.b64encode(plain)


def xor_hex(a, b):
    '''peroform xor between two hex strings, return values in hex'''
    return hex(int(a, 16) ^ int(b, 16))[2:]


def score(s):
    '''Get total probaplity of character frequency in a string'''
    freqs = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
    }
    #print(s)
    score = 0
    for x in s:
        score+=freqs.get(chr(x).lower(),0)
        
        #print(score)
    return score

def hamming_dist(s1,s2):
    '''find hamming distance between two byte strings.'''
    #check if the hamming function is working 
    assert len(s1)==len(s2),"Both strings mustbe of equal lengths"
    dist=0
    for i in range(len(s1)):
        d=s1[i]^s2[i]
        dist+=sum([1 for b in bin(d) if b=='1'])

    return dist


def repeating_xor(text,key):
    '''perform repeating xor '''
    op=b''
    i=0
    for c in text:
        op+=bytes([c^key[i]])
        i+=1
        if i+1>len(key):i=0
    return op
	
def main():
    print(1)

if __name__=='__main__':
    main()
