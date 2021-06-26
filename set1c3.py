
from cryptopals.helper import score

def single_xor(s,k):
    '''xor each char of a string against a key'''
    op = b''
    for char in s:
        op += bytes([char ^ k])

    return op

def bestmatch(ct):
    '''find best result from each single_xor'''
    result=[]
    for i in range(256):
        xored=single_xor(ct,i)
        res={
            'xored':xored,
            'score':score(xored),
            'key':chr(i)
        }
        result.append(res)

    return sorted(result, key=lambda c: c['score'], reverse=True)[0]
        
def main():
    ciphertext = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    plain=bestmatch(ciphertext)
    print(plain)


if __name__ == "__main__":
    main()