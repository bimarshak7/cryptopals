from binascii import hexlify

def main():
    ciphertext=b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal" 
    op=repeating_xor(ciphertext,b'ICE')
    print(hexlify(op).decode())
   
if __name__ == "__main__":
    main()