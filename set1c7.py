from base64 import b64decode
from Crypto.Cipher import AES

def AES_ECB_decrypt(ct,key):
	'''AES decryption in ECB mode'''
	cipher=AES.new(key, AES.MODE_ECB)
	return cipher.decrypt(ct)

def main():
	with open('7.txt','rb') as f:
		ct=b64decode(f.read())

	pt=AES_ECB_decrypt(ct, b'YELLOW SUBMARINE')	
	print(pt.decode())

if __name__ == "__main__":
    main()