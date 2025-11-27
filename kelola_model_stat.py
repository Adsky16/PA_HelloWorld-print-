from fungsi import clear, pause
from tambah_model import tambah_model
from hapus_model import hapus_model
from update_stat import update_statistik
import inquirer

def kelola_model_statistik():
    while True:
        clear()
        print("=== KELOLA MODEL & STATISTIK ===")

        pertanyaan = [
            inquirer.List('pilihan',
                        message="Pilih menu",
                        choices=['1. Tambah Model Baru', '2. Hapus Model', '3. Update Statistik Senjata', '4. Kembali'],
                        carousel=True),
        ]

        jawaban = inquirer.prompt(pertanyaan)
        nomor_pilihan = jawaban['pilihan']
        pilih = nomor_pilihan.split('.')[0]

        if pilih == '1':
            tambah_model()
        elif pilih == '2':
            hapus_model()
        elif pilih == '3':
            update_statistik()
        elif pilih == '4':
            break