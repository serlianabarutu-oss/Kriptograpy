import itertools
import math
import sys


def input_elemen(prompt="Masukkan elemen (pisahkan dengan koma, cth: a,b,c): "):
    """Fungsi pembantu untuk mengambil input array dari user."""
    input_str = input(prompt).strip()
    if not input_str:
        return None
    return [x.strip() for x in input_str.split(',')]

def permutasi_menyeluruh():
    """1. Permutasi Menyeluruh (n P n)"""
    print("\n--- 1. Permutasi Menyeluruh (n P n) ---")
    arr = input_elemen()
    if arr is None:
        print("Input tidak boleh kosong.")
        return

    n = len(arr)

    hasil_permutasi = list(itertools.permutations(arr))
    
    # Output
    print(f"\nData Input: {arr}")
    print(f"Jumlah elemen (n): {n}")
    print(f"Jumlah Permutasi: {len(hasil_permutasi)} ({n}!)")
    print("Hasil Permutasi:")
    for perm in hasil_permutasi:
        print(f"  {perm}")

def permutasi_sebagian():
    """2. Permutasi Sebagian (n P r)"""
    print("\n--- 2. Permutasi Sebagian (n P r) ---")
    
    arr = input_elemen()
    if arr is None:
        print("Input tidak boleh kosong.")
        return
    
    n = len(arr)
    
    try:
        r = int(input(f"Masukkan jumlah elemen yang diambil (r, maks {n}): ").strip())
    except ValueError:
        print("Nilai r harus berupa bilangan bulat.")
        return

    if r <= 0 or r > n:
        print(f"Nilai r harus > 0 dan <= {n}.")
        return

    hasil_permutasi = list(itertools.permutations(arr, r))
    
    # Output
    print(f"\nData Input: {arr}, r = {r}")
    print(f"Jumlah Permutasi: {len(hasil_permutasi)}")
    print("Hasil Permutasi:")
    for perm in hasil_permutasi:
        print(f"  {perm}")

def permutasi_keliling():
    """3. Permutasi Keliling ((n-1)!)"""
    print("\n--- 3. Permutasi Keliling ((n-1)!) ---")
    
    arr = input_elemen()
    if arr is None:
        print("Input tidak boleh kosong.")
        return

    n = len(arr)
    
    if n <= 1:
        print("Permutasi keliling membutuhkan minimal 2 elemen.")
        return

    jumlah_cara = math.factorial(n - 1)
  
    pertama = arr[0]
    sisa = arr[1:]
    permutasi_sisa = list(itertools.permutations(sisa))

    hasil_keliling = [[pertama] + list(perm) for perm in permutasi_sisa]
    
    # Output
    print(f"\nData Input: {arr}")
    print(f"Jumlah Permutasi Keliling: {jumlah_cara} (yaitu ({n}-1)!)")
    print("Representasi Permutasi Keliling (Fixing elemen pertama):")
    for perm in hasil_keliling:
        print(f"  {perm}")

def permutasi_berkelompok_urutan():
    """4. Permutasi Data Berkelompok (Permutasi Antar Kelompok)"""
    print("\n--- 4. Permutasi Data Berkelompok (Antar Kelompok) ---")
    print("Tujuan: Mengurutkan elemen berdasarkan urutan kelompok.")
    print("Format Input: grup1_elem1,grup1_elem2|grup2_elem1,grup2_elem2")
    
    input_str = input("Masukkan grup (cth: 1,2|3,4): ").strip()
    
    if not input_str:
        print("❌ Input tidak boleh kosong.")
        return

    try:
      
        grup = []
        for kelompok_str in input_str.split('|'):
            elemen = [x.strip() for x in kelompok_str.split(',')]
            grup.append(elemen)

    except Exception:
        print("Format input grup salah. Gunakan format seperti: 1,2|3,4")
        return

    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
          
            for perm in itertools.permutations(kelompok): 
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    
    # Output
    print(f"\nData Input Grup: {grup}")
    print(f"Jumlah Permutasi: {len(hasil)}")
    print("Hasil Permutasi Berkelompok:")
    
    for i, perm in enumerate(hasil):
        if i < 20: 
            print(f"  {perm}")
        else:
            print("  ... (hanya menampilkan 20 hasil pertama)")
            break
 

def atur_buku_di_rak():
    
    print("\n--- Latihan 2: Mengatur n Buku di r Bagian Rak (r^n) ---")
    
    try:
        n = int(input("Masukkan jumlah buku (n): ").strip())
        if n <= 0:
            print(" Jumlah buku (n) harus positif.")
            return

        r = int(input("Masukkan jumlah bagian rak (r): ").strip())
        if r <= 0:
            print(" Jumlah bagian rak (r) harus positif.")
            return

    except ValueError:
        print(" Input harus berupa bilangan bulat positif.")
        return

    total_cara = r ** n

    print("\n--- Hasil Perhitungan ---")
    print(f"Jumlah Buku (n)      : {n}")
    print(f"Jumlah Bagian Rak (r): {r}")
    print(f"Total Cara Mengatur Buku: {r}^{n} = {total_cara}")
    print("\nIni adalah permutasi dengan pengulangan, di mana setiap buku (n) unik")
    print(f"dapat diposisikan di salah satu dari {r} bagian rak (r^n).")


def menu_permutasi():
    """Menampilkan menu utama dan menjalankan fungsi yang dipilih."""
    while True:
        print("\n======================================")
        print("      PROGRAM ARSITEKTUR PERMUTASI    ")
        print("======================================")
        print("1. Permutasi Menyeluruh (n P n)")
        print("2. Permutasi Sebagian (n P r)")
        print("3. Permutasi Keliling")
        print("4. Permutasi Data Berkelompok (Antar Kelompok)")
        print("--------------------------------------")
        print("5. Latihan 2: Atur n Buku di r Rak (r^n)")
        print("6. Keluar")
        print("--------------------------------------")
        
        pilihan = input("Pilih Opsi (1-6): ").strip()

        if pilihan == '1':
            permutasi_menyeluruh()
        elif pilihan == '2':
            permutasi_sebagian()
        elif pilihan == '3':
            permutasi_keliling()
        elif pilihan == '4':
            permutasi_berkelompok_urutan()
        elif pilihan.upper() == '5' or pilihan == '5':
             atur_buku_di_rak()
        elif pilihan == '6':
            print("\nSampai jumpa lagi, Bro! Program selesai.")
            sys.exit() 
        else:
            print("\n Pilihan tidak valid. Silakan masukkan angka 1 sampai 6.")

# Jalankan program
if __name__ == "__main__":
    menu_permutasi()