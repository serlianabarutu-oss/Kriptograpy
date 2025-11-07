class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def _format_text(self, text):
        """Menghapus spasi dan ubah ke huruf besar"""
        return ''.join([c.upper() for c in text if c.isalpha()])

    def _extend_key(self, text):
        """Perpanjang key agar panjangnya sama dengan teks"""
        key_repeated = (self.key * ((len(text) // len(self.key)) + 1))[:len(text)]
        return key_repeated

    def encrypt(self, plaintext):
        plaintext = self._format_text(plaintext)
        key = self._extend_key(plaintext)
        ciphertext = ""
        print("\n=== PROSES ENKRIPSI ===")
        for p, k in zip(plaintext, key):
            p_val = ord(p) - 65
            k_val = ord(k) - 65
            c_val = (p_val + k_val) % 26
            c = chr(c_val + 65)
            ciphertext += c
            print(f"{p}({p_val}) + {k}({k_val}) -> {c}({c_val})")
        print("========================\n")
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = self._format_text(ciphertext)
        key = self._extend_key(ciphertext)
        plaintext = ""
        print("\n=== PROSES DEKRIPSI ===")
        for c, k in zip(ciphertext, key):
            c_val = ord(c) - 65
            k_val = ord(k) - 65
            p_val = (c_val - k_val + 26) % 26
            p = chr(p_val + 65)
            plaintext += p
            print(f"{c}({c_val}) - {k}({k_val}) -> {p}({p_val})")
        print("========================\n")
        return plaintext


# === Menu Utama Program ===
if __name__ == "__main__":
    while True:
        print("==== MENU VIGENERE CIPHER ====")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        pilihan = input("Pilih mode (1/2/3) 🫵  : ")

        if pilihan == "1":
            key = input("Masukkan kunci 🧐: ")
            cipher = VigenereCipher(key)
            text = input("Masukkan plaintext 🙂‍↕: ")
            hasil = cipher.encrypt(text)
            print(f"Hasil Enkripsi 😯: {hasil}\n")

        elif pilihan == "2":
            key = input("Masukkan kunci 🤨: ")
            cipher = VigenereCipher(key)
            text = input("Masukkan ciphertext 😏: ")
            hasil = cipher.decrypt(text)
            print(f"Hasil Dekripsi 😋: {hasil}\n")

        elif pilihan == "3":
            print("Byeee💃💃")
            break

        else:
            print("Pilihan tidak valid, silakan pilih 1, 2, atau 3.\n")
