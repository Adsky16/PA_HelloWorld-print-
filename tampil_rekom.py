from fungsi import clear, pause
from data import jenis_senjata
from tampil_model_rekom import tampil_model_rekomendasi
import inquirer

def tampil_rekomendasi():
    while True:
        clear()
        print('=== REKOMENDASI SENJATA ===')

        daftar = []
        for i in range(len(jenis_senjata)):
            daftar.append(f"{i+1}. {jenis_senjata[i]}")
        daftar.append(f"{len(jenis_senjata)+1}. Kembali")

        pertanyaan = [
            inquirer.List('daftar',
                        message="Pilih jenis senjata",
                        choices=daftar,
                        carousel=True),
        ]

        jawaban = inquirer.prompt(pertanyaan)
        
        nomor_pilihan = jawaban['daftar']

        if nomor_pilihan == (f"{len(jenis_senjata)+1}. Kembali"):
            return
        
        pilih = int(nomor_pilihan.split('.')[0]) - 1

        if pilih < len(jenis_senjata):
            tampil_model_rekomendasi(pilih)
        elif pilih == len(jenis_senjata):
            break
        else:
            print("Pilihan tidak valid!")
            pause()
