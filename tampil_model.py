from fungsi import clear, pause
from data import jenis_senjata, model_senjata, semua_statistik
from prettytable import PrettyTable
import inquirer

def tampil_model():
    global jenis_senjata, model_senjata, semua_statistik
    while True:
        clear()
        print("=== DAFTAR JENIS SENJATA ===")

        daftar = []
        for i in range(len(jenis_senjata)):
            daftar.append(f"{i+1}. {jenis_senjata[i]}")
        daftar.append(f"{len(jenis_senjata)+1}. Kembali")
        
        pertanyaan = [
            inquirer.List('pilihan',
                        message="Pilih jenis senjata",
                        choices=daftar,
                        carousel=True),
        ]
        
        jawaban = inquirer.prompt(pertanyaan)
            
        nomor_pilihan = jawaban['pilihan']
        
        if nomor_pilihan == (f"{len(jenis_senjata)+1}. Kembali"):
            return
            
        jenis = int(nomor_pilihan.split('.')[0]) - 1
        
        if jenis < len(jenis_senjata):
            clear()
            print(f"=== DAFTAR MODEL SENJATA {jenis_senjata[jenis].upper()} ===")

            pilihan_model = []
            for j in range(len(model_senjata[jenis])):
                pilihan_model.append(f"{j+1}. {model_senjata[jenis][j]}")
            pilihan_model.append(f"{len(model_senjata[jenis])+1}. Kembali")
            
            pertanyaan_model = [
                inquirer.List('pilihan_model',
                            message="Pilih model",
                            choices=pilihan_model,
                            carousel=True),
            ]
            
            jawaban_model = inquirer.prompt(pertanyaan_model)
                
            nomor_model = jawaban_model['pilihan_model']
            
            if nomor_model == (f"{len(model_senjata[jenis])+1}. Kembali"):
                continue
                
            model = int(nomor_model.split('.')[0]) - 1
            
            if model < len(model_senjata[jenis]):
                clear()
                
                print(f"=== STATISTIK {model_senjata[jenis][model].upper()} ===")
                stats = semua_statistik[jenis][model]
                
                table = PrettyTable()
                table.field_names = ["Statistik", "Nilai"]
                table.align["Statistik"] = "l"
                table.align["Nilai"] = "r"

                for k, v in stats.items():
                    table.add_row([k, v])

                print(table)
                pause()

        else:
            print("Jenis tidak valid!")
            pause()
