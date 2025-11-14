"""
DES encryption (CLI)
"""
import sys
from math import ceil

# Permuted Choice 1 (PC-1) - 64 -> 56 bits (drop parity bits)
PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

# Permuted Choice 2 (PC-2) - 56 -> 48 bits
PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

# Initial Permutation (IP)
IP = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

# Final Permutation (IP inverse)
IP_INV = [
    40,8,48,16,56,24,64,32,
    39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25
]

# Expansion table (E) 32 -> 48
E = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]

# S-boxes (8 boxes), each 4x16 table flattened row-wise
S_BOX = [
# S1
[
    14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
    0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
    4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
    15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13
],
# S2
[
    15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
    3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
    0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
    13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9
],
# S3
[
    10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
    13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
    13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
    1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12
],
# S4
[
    7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
    13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
    10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
    3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14
],
# S5
[
    2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
    14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
    4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
    11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3
],
# S6
[
    12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
    10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
    9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
    4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13
],
# S7
[
    4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
    13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
    1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
    6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12
],
# S8
[
    13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
    1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
    7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
    2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11
]
]

# P permutation (32-bit)
P = [
    16,7,20,21,
    29,12,28,17,
    1,15,23,26,
    5,18,31,10,
    2,8,24,14,
    32,27,3,9,
    19,13,30,6,
    22,11,4,25
]

# Pergeseran 
SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# --- Helper functions ---
def bytes_to_bitstring(b: bytes) -> str:
    return ''.join(f'{byte:08b}' for byte in b)

def bitstring_to_bytes(s: str) -> bytes:
    if len(s) % 8 != 0:
        s = s + '0' * (8 - (len(s) % 8))
    return bytes(int(s[i:i+8], 2) for i in range(0, len(s), 8))

def permute(bitstr: str, table: list) -> str:
    return ''.join(bitstr[i-1] for i in table)

def left_rotate(s: str, n: int) -> str:
    return s[n:] + s[:n]

def xor_bits(a: str, b: str) -> str:
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

def sbox_substitution(bits48: str) -> str:
    out = []
    for i in range(8):
        block = bits48[i*6:(i+1)*6]
        row = int(block[0] + block[5], 2)  
        col = int(block[1:5], 2)
        val = S_BOX[i][row*16 + col]
        out.append(f'{val:04b}')
    return ''.join(out)  

#Key schedule 
def generate_subkeys(key_bytes: bytes) -> list:
    if len(key_bytes) < 8:
        raise ValueError("Key must be at least 8 bytes.")
    key64 = key_bytes[:8]  
    key64bits = bytes_to_bitstring(key64)  
    #PC-1 -> 56 bits
    key56 = permute(key64bits, PC1)
    C = key56[:28]
    D = key56[28:]
    subkeys = []
    for round_i in range(16):
        shift = SHIFT_SCHEDULE[round_i]
        C = left_rotate(C, shift)
        D = left_rotate(D, shift)
        CD = C + D
        Ki = permute(CD, PC2)  
        subkeys.append(Ki)
    return subkeys

#DES block encryption (64-bit)
def des_block_encrypt(block8: bytes, subkeys: list) -> bytes:
    if len(block8) != 8:
        raise ValueError("Block must be 8 bytes")
    block_bits = bytes_to_bitstring(block8)  # 64 bits
    # Initial permutation
    permuted = permute(block_bits, IP)
    L = permuted[:32]
    R = permuted[32:]
    # 16 rounds
    for i in range(16):
        # Expansion E
        expanded_R = permute(R, E)  # 48 bits
        # XOR with subkey
        x = xor_bits(expanded_R, subkeys[i])
        # S-box substitution -> 32 bits
        s_out = sbox_substitution(x)
        # P permutation
        p_out = permute(s_out, P)
        # Feistel: new R = L xor p_out
        newR = xor_bits(L, p_out)
        L = R
        R = newR
    # combine R and L 
    preoutput = R + L
    cipher_bits = permute(preoutput, IP_INV)
    return bitstring_to_bytes(cipher_bits)

#Padding
def pkcs7_pad(data: bytes, block_size: int = 8) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    if pad_len == 0:
        pad_len = block_size
    return data + bytes([pad_len]) * pad_len

#functions
def format_bitgroups(bs: str, group: int = 8) -> str:
    return ' '.join(bs[i:i+group] for i in range(0, len(bs), group))

def bytes_to_bitstring_concat(bs: bytes) -> str:
    return ''.join(f'{b:08b}' for b in bs)

#CLI main
def main():
    print("=== DES Encryption (CLI) ===")
    plaintext = input("Plaintext (any text): ").rstrip("\n")
    key_input = input("Key (min 8 chars) : ").rstrip("\n")
    if len(key_input.encode('utf-8')) < 8:
        print("Error: key must be at least 8 bytes when encoded (use at least 8 ASCII chars).")
        sys.exit(1)
    key_bytes = key_input.encode('utf-8')[:8]

    # Generate subkeys K1..K16
    subkeys = generate_subkeys(key_bytes)

    print("\nSubkeys (K1 .. K16) -- each 48 bits (binary):")
    for i, k in enumerate(subkeys, start=1):
        print(f"K{i:2d}: {format_bitgroups(k, 6)}  ({k})")  

    # Prepare plaintext bytes and padding
    pt_bytes = plaintext.encode('utf-8')
    padded = pkcs7_pad(pt_bytes, 8)
    num_blocks = len(padded) // 8
    print(f"\nPlaintext length: {len(pt_bytes)} bytes, after PKCS#7 padding: {len(padded)} bytes ({num_blocks} blocks of 8 bytes)")

    cipher_blocks = []
    cipher_bits_all = ''
    for bi in range(num_blocks):
        blk = padded[bi*8:(bi+1)*8]
        cblk = des_block_encrypt(blk, subkeys)
        cipher_blocks.append(cblk)
        cipher_bits_all += bytes_to_bitstring_concat(cblk)

    ciphertext_bytes = b''.join(cipher_blocks)
    # Output
    print("\nCiphertext (binary):")
    # show per-block 64-bit groups
    for i in range(num_blocks):
        block_bits = bytes_to_bitstring_concat(cipher_blocks[i])
        print(f"Block {i+1:02d}: {format_bitgroups(block_bits, 8)}  ({block_bits})")

    print("\nCiphertext (hex):")
    print(ciphertext_bytes.hex().upper())

    # For convenience, also show combined binary
    print("\nCiphertext combined binary (blocks concatenated):")
    print(format_bitgroups(cipher_bits_all, 8))

    print("\nDone.")

if __name__ == "__main__":
    main()
