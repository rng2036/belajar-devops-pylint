"""Modul kode bersih hasil perbaikan kode_bau untuk Pylint."""
TOTAL_AWAL = 10
def hitung_hasil(flag_a, flag_b, flag_c, angka_d, angka_e):
    """Hitung hasil dari flag dan angka yang diberikan.
    Args:
        flag_a: Kondisi pertama yang harus True.
        flag_b: Kondisi kedua yang harus False.
        flag_c: Kondisi ketiga yang harus None.
        angka_d: Angka tambahan pertama.
        angka_e: Daftar berisi minimal satu angka.
    Returns:
        Hasil penjumlahan atau None jika kondisi tidak terpenuhi.
    """
    if not flag_a or flag_b or flag_c is not None:
        return None
    try:
        hasil = angka_d + angka_e[0] + TOTAL_AWAL
    except (IndexError, TypeError) as err:
        print(f"Gagal menghitung: {err}")
        return None
    print(hasil)
    return hasil
def main():
    """Fungsi utama program."""
    hitung_hasil(True, False, None, 1, [2])
if __name__ == "__main__":
    main()