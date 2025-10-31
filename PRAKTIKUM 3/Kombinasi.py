import itertools
import math
import sys

def hitung_jumlah_kombinasi(n, r):

    if r < 0 or r > n:
        return 0
    try:
     
        return math.comb(n, r)
    except AttributeError:
      
        faktorial_n = math.factorial(n)
        faktorial_r = math.factorial(r)
        faktorial_n_r = math.factorial(n - r)
        return faktorial_n // (faktorial_r * faktorial_n_r)

def tampilkan_kombinasi_huruf():
    """
    Menghitung dan menampilkan semua hasil kombinasi C(n, r)
    menggunakan huruf inisial (A, B, C, ...) sebagai objek,
    sesuai permintaan pengembangan.
    """
    print("\n==================================")
    print(" PROGRAM KOMBINASI C(n, r) LENGKAP")
    print("==================================")
    
    try:
        n = int(input("Masukkan jumlah total objek (n): ").strip())
        r = int(input("Masukkan jumlah objek yang dipilih (r): ").strip())
    except ValueError:
        print("❌ Input harus berupa bilangan bulat positif.")
        return
    
    if r < 0 or n < 0:
        print("❌ n dan r harus bilangan non-negatif.")
        return
        
    if r > n:
        print(f"❌ r ({r}) tidak boleh lebih besar dari n ({n}).")
        return

    objek = [chr(65 + i) for i in range(n)] 

    jumlah_kombinasi = hitung_jumlah_kombinasi(n, r)

    semua_kombinasi = list(itertools.combinations(objek, r))
    
    # Output Hasil
    print("\n--- Hasil Perhitungan ---")
    print(f"Objek yang tersedia (n={n}): {objek}")
    print(f"Jumlah yang dipilih (r={r}): {r}")
    print(f"Jumlah total kombinasi C({n}, {r}) adalah: **{jumlah_kombinasi}**")
    
    print("\n--- Semua Hasil Kombinasi ---")
    
    # Mencetak kombinasi
    for i, combo in enumerate(semua_kombinasi):
        # Batasi tampilan jika hasilnya terlalu banyak
        if i < 50:
            print(f"  {i+1}. {combo}")
        else:
            print(f"  ... dan {jumlah_kombinasi - 50} kombinasi lainnya.")
            break
            
    # Menambahkan opsi untuk keluar
    input("\nTekan ENTER untuk keluar...")
    sys.exit()

if __name__ == "__main__":
    tampilkan_kombinasi_huruf()