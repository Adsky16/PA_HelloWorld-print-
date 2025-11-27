from fungsi import clear, pause
from data import jenis_senjata, model_senjata, semua_statistik
import inquirer

def tambah_model():
    global model_senjata, semua_statistik
    while True:
        clear()
        print("=== TAMBAH MODEL + STATISTIK ===")
        daftar = []
        for i in range(len(jenis_senjata)):
            daftar.append(f"{i+1}. {jenis_senjata[i]}")
        daftar.append(str(len(jenis_senjata)+1)+'. Kembali')

        pertanyaan = [
            inquirer.List('pilihan_jenis',
                        message="Pilih jenis senjata",
                        choices=daftar,
                        carousel=True),
        ]

        jawaban = inquirer.prompt(pertanyaan)
        nomor_pilihan = jawaban['pilihan_jenis']

        if nomor_pilihan == (f"{len(jenis_senjata)+1}. Kembali"):
            break

        jenis = int(nomor_pilihan.split('.')[0]) - 1
        
        if jenis < len(jenis_senjata):
            clear()
            print(f"=== TAMBAH MODEL BARU UNTUK {jenis_senjata[jenis].upper()} ===")
            nama = input("Nama senjata baru: ").upper()
            try:
                dmg = int(input("Damage   : "))
                rate = int(input("Fire Rate: "))
                acc = int(input("Accuracy : "))
                mob = int(input("Mobility : "))
                rng = int(input("Range    : "))
                model_senjata[jenis].append(nama)
                semua_statistik[jenis].append({
                    "Damage": dmg,
                    "Fire Rate": rate,
                    "Accuracy": acc,
                    "Mobility": mob,
                    "Range": rng
                })
                print("Model & statistik baru berhasil ditambahkan!")
                pause()
            except ValueError:
                print("Input harus berupa angka!")
                pause()

