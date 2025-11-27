from fungsi import clear
import inquirer

def menu_utama(status):
    clear()
    print('=== DELTA FORCE ARMORY ===')
    pilihan = [
        "1. Daftar senjata",
        "2. Rekomendasi senjata",
        "3. Gacha Senjata",
    ]

    if status == "admin":
        pilihan.extend([
            "4. Update Rekomendasi Senjata",
            "5. Kelola Model & Statistik Senjata",
            "6. Kembali"
        ])
    else:
        pilihan.append("4. Kembali")

    pertanyaan = [
        inquirer.List('menu',
                        message="Pilih menu",
                        choices=pilihan,
                        carousel=True),
    ]

    jawaban = inquirer.prompt(pertanyaan)
    nomor_pilihan = jawaban['menu'].split('.')[0]
    return nomor_pilihan