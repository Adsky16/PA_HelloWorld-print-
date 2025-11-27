from fungsi import clear, pause
from data import jenis_senjata, model_senjata, semua_statistik
import inquirer

def update_statistik():
    global semua_statistik, model_senjata
    while True:
        clear()
        print("=== UPDATE STATISTIK SENJATA (BUFF/NERF) ===")

        daftar = []
        for i in range(len(jenis_senjata)):
            daftar.append(f"{i+1}. {jenis_senjata[i]}")
        daftar.append(str(len(jenis_senjata)+1)+". Kembali")

        pertanyaan = [
            inquirer.List('jenis',
                        message="Pilih jenis senjata",
                        choices=daftar,
                        carousel=True),
        ]   
        jawaban = inquirer.prompt(pertanyaan)
        nomor_jenis = jawaban['jenis']
        jenis = int(nomor_jenis.split('.')[0]) - 1

        if jenis < len(jenis_senjata):
            while True:
                clear()
                print(f"=== UPDATE STATISTIK {jenis_senjata[jenis]} ===")

                pilih_model = []
                for j in range(len(model_senjata[jenis])):
                    pilih_model.append(f"{j+1}. {model_senjata[jenis][j]}")
                pilih_model.append(str(len(model_senjata[jenis])+1) + ". Kembali")

                pertanyaan_model = [
                    inquirer.List('model',
                                message="Pilih model yang statistiknya ingin diupdate",
                                choices=pilih_model,
                                carousel=True),
                ]
                jawaban_model = inquirer.prompt(pertanyaan_model)
                nomor_model = jawaban_model['model']
                pilihan = int(nomor_model.split('.')[0]) - 1

                if pilihan < len(model_senjata[jenis]):
                    try:
                        dmg = int(input("Damage baru   : "))
                        rate = int(input("Fire Rate baru: "))
                        acc = int(input("Accuracy baru : "))
                        mob = int(input("Mobility baru : "))
                        rng = int(input("Range baru    : "))
                        semua_statistik[jenis][pilihan] = {
                            "Damage": dmg,
                            "Fire Rate": rate,
                            "Accuracy": acc,
                            "Mobility": mob,
                            "Range": rng
                        }
                        print("Statistik berhasil diperbarui!")
                        pause()
                    except ValueError:
                        print("Input harus berupa angka!")
                        pause()
                elif pilihan == len(model_senjata[jenis]):
                    break
        elif jenis == len(jenis_senjata):
            break