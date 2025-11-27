from fungsi import clear, pause
from data import jenis_senjata, rekomendasi_list
from tampil_stat import tampil_statistik
import inquirer

def tampil_model_rekomendasi(pilih_jenis):
    while True:
        clear()
        print(f"REKOMENDASI {jenis_senjata[pilih_jenis].upper()}:")

        daftar = []
        for j in range(len(rekomendasi_list[pilih_jenis])):
            daftar.append(f"{j+1}. {rekomendasi_list[pilih_jenis][j]}")
        daftar.append(str(len(rekomendasi_list[pilih_jenis])+1) + ". Kembali")

        pertanyaan = [
            inquirer.List('daftar',    
                        message="Pilih model untuk lihat statistik",
                        choices=daftar,
                        carousel=True),
        ]

        jawaban = inquirer.prompt(pertanyaan)

        nomor_pilihan = jawaban['daftar']

        if nomor_pilihan == (str(len(rekomendasi_list[pilih_jenis])+1) + ". Kembali"):
            return
        
        pilih = int(nomor_pilihan.split('.')[0]) - 1

        if pilih < len(rekomendasi_list[pilih_jenis]):
            tampil_statistik(pilih_jenis, pilih)
        elif pilih == len(rekomendasi_list[pilih_jenis]):
            break
        else:
            print("Pilihan tidak valid!")
            pause()