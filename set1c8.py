from Crypto.Cipher.AES import block_size

def is_ecb_encoded(ct,l=16):
	'''check if the cipher text is encrypted withAES in ECB mode'''
	if len(ct)%l !=0:
		return False
	unique=[]
	for i in range(0,len(ct),l):
		chunk=ct[i:i+l]
		if chunk in unique:
			return True
		else:
			unique.append(chunk)

def main():
	ciphertexts = [bytes.fromhex(line.strip()) for line in open("8.txt")]
	for i, ct in enumerate(ciphertexts):
		if is_ecb_encoded(ct):
			print (i, ct)
			print("\n")
	
if __name__ == "__main__":
    main()