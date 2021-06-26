from base64 import b64decode
from cryptopals.helper import hamming_dist
from set1c3 import bestmatch

def break_repeating_xor(ct):
	'''Breaks the repeating key XOR encryption '''
	distances = []
	for ksize in range(2, 41):
		blocks=[]
		for i in range(16): #taking more block samples for acuracy
		        blocks.append(ct[i*ksize:(i+1)*ksize])
		block_distances = []
		for i in range(len(blocks)):
			for j in range(i+1, len(blocks)):
				block_distances.append(hamming_dist(blocks[i], blocks[j]))
	    
		total_distance = sum(block_distances)
		normalized_distance = total_distance / ksize
		distances.append((normalized_distance, ksize))

	distances.sort()
	ksize=distances[0][1]

	blocks = []
	for i in range(ksize):
		block = ct[i::ksize]
		blocks.append(block)
	k=''
	for block in blocks:
		k+=bestmatch(block)['key']

	return k

def main():
	with open('6.txt','rb') as f:
		t=b64decode(f.read())

	key=break_repeating_xor(t)
	print(key)


if __name__ == "__main__":
    main()
