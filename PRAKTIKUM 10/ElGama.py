def mod_inverse(a, p):
    return pow(a, p - 2, p)

def char_to_num(c):
    if c == ' ':
        return 27
    return ord(c.upper()) - 64   

def num_to_char(n):
    if n == 27:
        return ' '
    return chr(n + 64)

# ---------- INPUT ----------
plaintext = input("Masukkan plaintext (12 huruf): ")
p = int(input("Masukkan bilangan prima (p): "))
g = int(input("Masukkan generator (g): "))
x = int(input("Masukkan kunci privat (x): "))
k = int(input("Masukkan bilangan acak (k): "))

y = pow(g, x, p)

print("\n==============================")
print("KUNCI PUBLIK ELGAMAL")
print("==============================")
print(f"p = {p}")
print(f"g = {g}")
print(f"x = {x}")
print(f"y = g^x mod p = {y}")

ciphertext = []

# ---------- ENKRIPSI ----------
print("\n==============================")
print("PROSES ENKRIPSI PER BLOK")
print("==============================")

for i, char in enumerate(plaintext):
    m = char_to_num(char)
    a = pow(g, k, p)
    yk = pow(y, k, p)
    b = (yk * m) % p
    ciphertext.append((a, b))

    print(f"\nBlok m{i+1}")
    print(f"Karakter : '{char}'")
    print(f"Nilai m{i+1} = {m}")
    print(f"a = {a}")
    print(f"b = {b}")

# ---------- DEKRIPSI ----------
print("\n==============================")
print("PROSES DEKRIPSI PER BLOK")
print("==============================")

hasil = ""

for i, (a, b) in enumerate(ciphertext):
    s = pow(a, x, p)
    s_inv = mod_inverse(s, p)
    m = (b * s_inv) % p
    char = num_to_char(m)
    hasil += char

    print(f"\nBlok m{i+1}")
    print(f"s = {s}")
    print(f"s⁻¹ = {s_inv}")
    print(f"m{i+1} = {m}")
    print(f"Karakter = '{char}'")

# ---------- HASIL ----------
print("\n==============================")
print("HASIL AKHIR")
print("==============================")
print("Ciphertext :", ciphertext)
print("Plaintext hasil dekripsi :", hasil)
