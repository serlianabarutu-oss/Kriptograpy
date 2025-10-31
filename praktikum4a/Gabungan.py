import math
import sys

def substitusi_cipher_func(plaintext, aturan):
    ciphertext = ""
    for char in plaintext.upper(): 
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char 
    return ciphertext

def transposisi_cipher_func(plaintext):
    teks_bersih = plaintext.replace(' ', '')
    
    part_length = math.ceil(len(teks_bersih) / 4) 

    parts = []
    for i in range(0, len(teks_bersih), part_length):
        parts.append(teks_bersih[i: i + part_length])

    ciphertext = ""
    for col in range(4): 
        for part in parts:
            if col < len(part):
                ciphertext += part[col] 
                
    return ciphertext


def latihan_gabungan_manual():
    print("\n--- Latihan: Substitusi diikuti Transposisi (Input Manual) ---")
    
    plaintext_asli = input("Masukkan Plaintext yang ingin dienkripsi: ").upper().strip()
    
    if not plaintext_asli:
        print("Plaintext tidak boleh kosong. Program dibatalkan.")
        return
    
    aturan_substitusi = {
        'U': 'K', 'N': 'N', 'I': 'I', 'K': 'K', 'A': 'B', 
        'S': 'X', 'O': 'Z', 'T': 'J', 'H': 'Q', 'M': 'P',
        'E': 'R', 'R': 'T', 'D': 'Y', 'C': 'W', 'L': 'F',
        ' ': ' ' 
    }
    
    ciphertext_substitusi = substitusi_cipher_func(plaintext_asli, aturan_substitusi)
    
    ciphertext_final = transposisi_cipher_func(ciphertext_substitusi)

    print("\n--- Hasil Proses Enkripsi Dua Tahap ---")
    print(f"1. Plaintext Awal: {plaintext_asli}")
    print(f"2. Ciphertext (Substitusi): {ciphertext_substitusi}")
    print(f"3. Ciphertext (Substitusi + Transposisi, 4 Blok): {ciphertext_final}")

if __name__ == "__main__":
    latihan_gabungan_manual()