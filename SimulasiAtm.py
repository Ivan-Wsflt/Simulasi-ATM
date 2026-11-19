# =====================================================
# BANK IVAN - Mesin ATM Mini
# Tugas Akhir Bootcamp Programming Day 3
# =====================================================

NAMA_BANK = "BANK IVAN"
BATAS_SALAH_PIN = 3

data_nasabah = {
    "nama": "Ivan",
    "pin": "210108",
    "saldo": 1500000,
}

daftar_riwayat = []


def ubah_ke_rupiah(angka):
    return "Rp " + f"{angka:,}".replace(",", ".")


def catat_riwayat(jenis_transaksi, jumlah_uang):
    daftar_riwayat.append({
        "jenis": jenis_transaksi,
        "jumlah": jumlah_uang,
        "saldo_setelahnya": data_nasabah["saldo"],
    })


def minta_angka(pertanyaan):
    try:
        angka = int(input(pertanyaan).strip())
    except ValueError:
        print("Itu huruf, bos. Uang kamu mau dibayar pakai abjad? Ketik angka, bukan puisi.")
        return None

    if angka <= 0:
        print("Nol rupiah? Minus? Ini ATM, bukan tempat latihan matematika anak TK.")
        return None

    return angka


def cek_pin():
    jumlah_salah = 0

    while jumlah_salah < BATAS_SALAH_PIN:
        pin_yang_diketik = input("Masukkan PIN kamu (jangan sampai lupa PIN sendiri ya): ").strip()

        if pin_yang_diketik == data_nasabah["pin"]:
            print(f"\nAkhirnya benar juga. Silakan masuk, {data_nasabah['nama']}, sang nasabah prioritas (versi kasihan).")
            return True

        jumlah_salah += 1
        sisa_kesempatan = BATAS_SALAH_PIN - jumlah_salah

        if sisa_kesempatan > 0:
            print(f"PIN salah. Sisa kesempatan: {sisa_kesempatan}. Itu PIN atau tanggal jadian sama mantan?")

    print("\nHayoloo salah 3 kali! Kasian deh, kartu kamu aku blokir.")
    print("Transfer dulu ke bank ini 1 M, baru saya tinjau lagi wkwk")
    return False


def lihat_saldo():
    print("\n--- CEK SALDO ---")
    print(f"Saldo kamu: {ubah_ke_rupiah(data_nasabah['saldo'])}")
    print("Tenang, dilihat berapa kali pun angkanya ga bakal nambah sendiri.")
    catat_riwayat("Cek Saldo", 0)


def setor_uang():
    print("\n--- SETOR TUNAI ---")
    jumlah_setor = minta_angka("Mau setor berapa? (jangan bilang receh doang) Rp ")

    if jumlah_setor is None:
        return

    data_nasabah["saldo"] += jumlah_setor
    catat_riwayat("Setor Tunai", jumlah_setor)

    print(f"{ubah_ke_rupiah(jumlah_setor)} masuk. Wah, ada yang lagi gajian atau habis ketemu sultan nih?")
    print(f"Saldo sekarang: {ubah_ke_rupiah(data_nasabah['saldo'])}. Awas, jangan langsung habis buat checkout keranjang kuning.")


def tarik_uang():
    print("\n--- TARIK TUNAI ---")
    jumlah_tarik = minta_angka("Mau tarik berapa? (inget, ini uang kamu sendiri) Rp ")

    if jumlah_tarik is None:
        return

    if jumlah_tarik > data_nasabah["saldo"]:
        print("Saldo ga cukup. Ambisi kamu sebesar gaji direktur, isi rekening kamu sebesar uang jajan SD.")
    else:
        data_nasabah["saldo"] -= jumlah_tarik
        catat_riwayat("Tarik Tunai", jumlah_tarik)

        print(f"{ubah_ke_rupiah(jumlah_tarik)} keluar. Selamat tinggal, uang. Semoga bahagia di tangan kasir minimarket.")
        print(f"Sisa saldo: {ubah_ke_rupiah(data_nasabah['saldo'])}. Tanggal tua mulai mengintip.")


def lihat_riwayat():
    print("\n--- RIWAYAT MUTASI ---")

    if not daftar_riwayat:
        print("Kosong melompong. Belum ngapa-ngapain kok minta riwayat, mau stalking diri sendiri?")
        return

    print("Berikut jejak keuangan kamu. Silakan merenung.\n")

    for nomor, catatan in enumerate(daftar_riwayat, start=1):
        if catatan["jenis"] == "Cek Saldo":
            tulisan_jumlah = "-"
        else:
            tulisan_jumlah = ubah_ke_rupiah(catatan["jumlah"])

        print(f"{nomor}. {catatan['jenis']:<12} | {tulisan_jumlah:>15} "
              f"| Saldo: {ubah_ke_rupiah(catatan['saldo_setelahnya'])}")


def tampilkan_menu():
    print("\n" + "=" * 40)
    print(f"        {NAMA_BANK}")
    print("=" * 40)
    print("[1] Cek Saldo (siap-siap kecewa)")
    print("[2] Setor Tunai (mimpi dulu gapapa)")
    print("[3] Tarik Tunai (hati-hati nyesel)")
    print("[4] Riwayat Mutasi (jejak dosa belanja)")
    print("[0] Keluar (kabur dari kenyataan)")
    print("=" * 40)


def jalankan_program():
    print("=" * 40)
    print(f"  Selamat datang di {NAMA_BANK}")
    print("  Bank paling jujur: saldo kamu ya segitu.")
    print("=" * 40)

    if not cek_pin():
        return

    program_masih_jalan = True

    while program_masih_jalan:
        tampilkan_menu()
        pilihan_menu = input("Mau ngapain lagi, bos? ").strip()

        if pilihan_menu == "1":
            lihat_saldo()
        elif pilihan_menu == "2":
            setor_uang()
        elif pilihan_menu == "3":
            tarik_uang()
        elif pilihan_menu == "4":
            lihat_riwayat()
        elif pilihan_menu == "0":
            print(f"\nMakasih udah mampir ke {NAMA_BANK}. Sana pulang, jangan lupa nabung. Atau minimal jangan checkout lagi.")
            program_masih_jalan = False
        else:
            print("Menu itu ga ada. Kamu baca daftar menunya atau cuma lihat angkanya doang?")


if __name__ == "__main__":
    jalankan_program()