

def heksa_ke_desimal(heksa_str):
    """Mengonversi bilangan heksadesimal ke desimal"""
    try:
        desimal = int(heksa_str, 16)
        return desimal
    except ValueError:
        return None

def heksa_ke_biner(heksa_str):
    """Mengonversi bilangan heksadesimal ke biner"""
    try:
        desimal = int(heksa_str, 16)
        biner = bin(desimal)[2:]  
        return biner
    except ValueError:
        return None

def heksa_ke_oktal(heksa_str):
    """Mengonversi bilangan heksadesimal ke oktal"""
    try:
        desimal = int(heksa_str, 16)
        oktal = oct(desimal)[2:]  
        return oktal
    except ValueError:
        return None



print("=== KONVERSI BILANGAN HEKSADESIMAL ===")
heksa_input = input("Masukkan bilangan heksadesimal: ")

desimal = heksa_ke_desimal(heksa_input)
biner = heksa_ke_biner(heksa_input)
oktal = heksa_ke_oktal(heksa_input)

if desimal is not None:
    print(f"\nHasil Konversi:")
    print(f"Desimal : {desimal}")
    print(f"Biner   : {biner}")
    print(f"Oktal   : {oktal}")
else:
    print("\nInput tidak valid! Pastikan hanya karakter 0–9 dan A–F.")
