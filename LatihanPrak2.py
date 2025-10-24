# Kalkulator Hybrid

def kalkulator_hybrid():
    print("=== Kalkulator Hybrid ===")
    ekspresi = input("Input (Ekspresi): ")

    try:
        # Hapus spasi agar bisa diproses
        ekspresi_bersih = ekspresi.replace(" ", "")

        # Evaluasi ekspresi matematika
        hasil = eval(ekspresi_bersih)

        # Tampilkan hasil
        print("Hasil Diproses")
        print(f"Output > {hasil}")

    except Exception as e:
        print("Terjadi kesalahan dalam ekspresi!")
        print(f"Error: {e}")


# Jalankan program
if __name__ == "__main__":
    kalkulator_hybrid()
