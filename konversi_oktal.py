

def oktal_ke_desimal(oktal_str):
    """Mengonversi bilangan oktal ke desimal"""
    try:
        desimal = int(oktal_str, 8)
        return desimal
    except ValueError:
        return None

def oktal_ke_biner(oktal_str):
    """Mengonversi bilangan oktal ke biner"""
    try:
        desimal = int(oktal_str, 8)
        biner = bin(desimal)[2:]  
        return biner
    except ValueError:
        return None

def oktal_ke_heksadesimal(oktal_str):
    """Mengonversi bilangan oktal ke heksadesimal"""
    try:
        desimal = int(oktal_str, 8)
        heksa = hex(desimal)[2:].upper()  
        return heksa
    except ValueError:
        return None



print("=== KONVERSI BILANGAN OKTAL ===")
oktal_input = input("Masukkan bilangan oktal: ")

desimal = oktal_ke_desimal(oktal_input)
biner = oktal_ke_biner(oktal_input)
heksadesimal = oktal_ke_heksadesimal(oktal_input)

if desimal is not None:
    print(f"\nHasil Konversi:")
    print(f"Desimal      : {desimal}")
    print(f"Biner        : {biner}")
    print(f"Heksadesimal : {heksadesimal}")
else:
    print("\nInput tidak valid! Pastikan hanya angka 0–7.")
