with open('alice.txt', 'rb') as f:
    t = f.read()

KEY = b'PRASANT'

def encrypt_w_repeated_xor(pt: bytes, key: bytes) -> bytes:
    print(type(pt), type(key))
    ct = bytes([pt[i] ^ key[i % len(key)] for i in range(len(pt))])
    return ct

def decrypt_w_repeated_xor(ct: bytes, key: bytes) -> bytes:
    return encrypt_w_repeated_xor(ct, key)

ct = encrypt_w_repeated_xor(t, KEY)

def edit_distance(s1, s2):
    assert len(s1) == len(s2), "Opps! the strings need to be of equal length"
    distance = 0
    for i in range(len(s1)):
        b1 = s1[i]
        b2 = s2[i]
        while b1 or b2:
            if ((b1 ^ b2) & 0x1) == 1:
                distance += 1
            b1 = b1 >> 1
            b2 = b2 >> 1
    return distance

s1 = b'this is a test'
s2 = b'wokka wokka!!!'
print(edit_distance(s1, s2))
assert edit_distance(s1, s2) == 37, "Opps! edit_distance function is wrongly implemented"

# 3.
distances = []
for keysize in range(2, 40):
    blocks = []
    for i in range(200):
        blocks.append(ct[i*keysize:(i+1)*keysize])
    block_distances = []
    for i in range(len(blocks)):
        for j in range(i+1, len(blocks)):
            block_distances.append(edit_distance(blocks[i], blocks[j]))
    total_distance = sum(block_distances)
    normalized_distance = total_distance / keysize

    distances.append((normalized_distance, keysize))

distances.sort()

keysize = distances[0][1]

blocks = []
for i in range(keysize):
    block = ct[i::keysize]
    blocks.append(block)

def brute_single_byte_xor(ct: bytes) -> int:
    frequency_table = { 'a' :  8.167,  'b' : 1.492, 'c' : 2.782, 'd' : 4.253,
                'e' : 12.702,  'f' : 2.228, 'g' : 2.015, 'h' : 6.094,
                'i' :  6.966,  'j' : 0.153, 'k' : 0.772, 'l' : 4.025,
                'm' :  2.406,  'n' : 6.749, 'o' : 7.507, 'p' : 1.929,
                'q' :  0.095,  'r' : 5.987, 's' : 6.327, 't' : 9.056,
                'u' :  2.758,  'v' : 0.978, 'w' : 2.360, 'x' : 0.150,
                'y' :  1.974,  'z' : 0.074, ' ' : 15 }
    scores = []
    for k in range(256):
        pt = bytes([ct[i] ^ k for i in range(len(ct))])
        score = 0
        for i in pt:
            if chr(i) in frequency_table:
                score += frequency_table[chr(i)]
        scores.append((score, k))
    scores.sort(reverse=True)
    return scores[0][1]

calculated_key = ''
for block in blocks:
    k = brute_single_byte_xor(block)
    calculated_key += chr(k)

print(calculated_key.encode())

print(decrypt_w_repeated_xor(ct[:200], calculated_key.encode()))
