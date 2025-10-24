

def biner_ke_desimal(biner_str):
    """Mengonversi bilangan biner (string) ke desimal (int)."""
    try:
        desimal = int(biner_str, 2)
        return desimal
    except ValueError:
        return None

def biner_ke_heksadesimal(biner_str):
    """Mengonversi bilangan biner (string) ke heksadesimal (string)."""
    try:
        desimal = int(biner_str, 2)
        heksa = hex(desimal)[2:].upper()
        return heksa
    except ValueError:
        return None


print("=== KONVERSI BILANGAN BINER ===")
biner_input = input("Masukkan bilangan biner: ")

desimal = biner_ke_desimal(biner_input)
heksadesimal = biner_ke_heksadesimal(biner_input)

if desimal is not None:
    print(f"\nHasil konversi:")
    print(f"Desimal      : {desimal}")
    print(f"Heksadesimal : {heksadesimal}")
else:
    print("\nInput tidak valid! Pastikan hanya memasukkan angka 0 dan 1.")
