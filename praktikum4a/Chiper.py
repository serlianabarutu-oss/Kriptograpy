import sys

def substitusi_cipher_func(plaintext, aturan):
    ciphertext = ""
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

def substitusi_cipher_manual():
    plaintext_asli = input("Plaintext: ").upper().strip()
    
    if not plaintext_asli:
        return
    
    aturan_substitusi = {
        'U': 'K', 'N': 'N', 'I': 'I', 'K': 'K', 'A': 'B', 
        'S': 'X', 'O': 'Z', 'T': 'J', 'H': 'Q', 'M': 'P',
        'E': 'R', 'R': 'T', 'D': 'Y', 'C': 'W', 'L': 'F',
        ' ': ' ' 
    }
    
    ciphertext_substitusi = substitusi_cipher_func(plaintext_asli, aturan_substitusi)
    
    print(f"Ciphertext: {ciphertext_substitusi}")

if __name__ == "__main__":
    substitusi_cipher_manual()