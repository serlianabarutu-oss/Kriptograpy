# ==========================
#   PROGRAM RSA PYTHON
#   LATIHAN 1 & LATIHAN 2
#   Dengan tahapan lengkap
# ==========================

import random
import math

# ---------- Fungsi Cek Prima ----------
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r+1, 2):
        if n % i == 0:
            return False
    return True

# ---------- Extended Euclidean ----------
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

# ---------- Invers Modulo ----------
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Tidak punya invers modulo")
    return x % m

# ---------- Enkripsi ----------
def encrypt_message(message, e, n):
    print("\n--- LANGKAH 4: ENKRIPSI ---")
    cipher = []
    for ch in message:
        m = ord(ch)
        c = pow(m, e, n)
        print(f"Konversi '{ch}' → {m}, Enkripsi: {m}^{e} mod {n} = {c}")
        cipher.append(c)
    return cipher

# ---------- Dekripsi ----------
def decrypt_message(cipher, d, n):
    print("\n--- LANGKAH 5: DEKRIPSI ---")
    text = ""
    for c in cipher:
        m = pow(c, d, n)
        print(f"Dekripsi: {c}^{d} mod {n} = {m} → '{chr(m)}'")
        text += chr(m)
    return text

# ======================================================
#                  LATIHAN 1
# ======================================================

print("\n========== LATIHAN 1 ==========")
p = 17
q = 11
e = 7

print(f"Bilangan prima: p = {p}, q = {q}, e = {e}")

# LANGKAH 1
n = p * q
print(f"\n--- LANGKAH 1: Hitung n = p*q = {n}")

# LANGKAH 2
phi = (p - 1) * (q - 1)
print(f"--- LANGKAH 2: Hitung φ(n) = (p-1)(q-1) = {phi}")

# LANGKAH 3
d = modinv(e, phi)
print(f"--- LANGKAH 3: Hitung d = e^(-1) mod φ(n) = {d}")

plaintext1 = input("\nMasukkan plaintext Latihan 1: ")

cipher1 = encrypt_message(plaintext1, e, n)
print("\nCiphertext:", cipher1)

decrypted1 = decrypt_message(cipher1, d, n)
print("\nHasil Dekripsi:", decrypted1)

# ======================================================
#                  LATIHAN 2 (acak)
# ======================================================
print("\n========== LATIHAN 2 (acak) ==========")

# generate p & q acak
while True:
    p2 = random.randint(50, 200)
    if is_prime(p2):
        break
while True:
    q2 = random.randint(50, 200)
    if is_prime(q2) and q2 != p2:
        break

print(f"Bilangan prima acak: p = {p2}, q = {q2}")

# LANGKAH 1
n2 = p2 * q2
print(f"\n--- LANGKAH 1: n = p*q = {n2}")

# LANGKAH 2
phi2 = (p2 - 1) * (q2 - 1)
print(f"--- LANGKAH 2: φ(n) = {phi2}")

# LANGKAH 3 - pilih e
candidates = [x for x in range(3, phi2) if math.gcd(x, phi2) == 1]
e2 = random.choice(candidates)
print(f"--- LANGKAH 3: Pilih e acak yang relatif prima dengan φ(n) → e = {e2}")

d2 = modinv(e2, phi2)
print(f"Invers modulo: d = {d2}")

plaintext2 = input("\nMasukkan plaintext Latihan 2: ")

cipher2 = encrypt_message(plaintext2, e2, n2)
print("\nCiphertext:", cipher2)

decrypted2 = decrypt_message(cipher2, d2, n2)
print("\nHasil Dekripsi:", decrypted2)
