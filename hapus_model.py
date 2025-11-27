from fungsi import clear, pause
from data import jenis_senjata, model_senjata, semua_statistik
import inquirer

def hapus_model():
    while True:
        clear()
        print("=== HAPUS MODEL & STATISTIK ===")

        daftar = []
        for i in range(len(jenis_senjata)):
            daftar.append(str(i+1)+". "+jenis_senjata[i])
        daftar.append(str(len(jenis_senjata)+1)+". Kembali")

        pertanyaan = [
            inquirer.List('jenis',
                            message="Pilih jenis senjata yang modelnya ingin dihapus",
                            choices=daftar,
                            carausel=True),
        ]

        jawaban = inquirer.prompt(pertanyaan)
        selected_jenis = jawaban['jenis']
        jenis = int(selected_jenis.split('.')[0]) - 1

        if jenis < len(jenis_senjata):
            clear()
            print(F"=== DAFTAR SENJATA {jenis_senjata[jenis].upper()} ===")
            pilih_model = []
            for j in range(len(model_senjata[jenis])):
                pilih_model.append(str(j+1)+". "+model_senjata[jenis][j])
            pilih_model.append(str(len(model_senjata[jenis])+1)+". Kembali")

            pertanyaan_model = [
                inquirer.List('model',
                            message="Pilih model yang ingin dihapus",
                            choices=pilih_model,
                            carousel=True),
            ]

            jawaban_model = inquirer.prompt(pertanyaan_model)
            nomor_pilihan = jawaban_model['model']
            hapus = int(nomor_pilihan.split('.')[0]) - 1

            if hapus < len(model_senjata[jenis]):
                dihapus = model_senjata[jenis].pop(hapus)
                semua_statistik[jenis].pop(hapus)
                print(f"Model & statistik '{dihapus}' berhasil dihapus!")
                pause()

        elif jenis == len(jenis_senjata):
            break