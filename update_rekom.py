from fungsi import clear, pause
from data import jenis_senjata, model_senjata, rekomendasi_list
import inquirer

def update_rekomendasi():
    while True:
        clear()
        print("=== UPDATE REKOMENDASI SENJATA ===")

        pertanyaan = [
            inquirer.List('pertanyaan',
                        message="Pilih menu",
                        choices=['1. Tambah Rekomendasi', '2. Hapus Rekomendasi', '3. Kembali'],
                        carousel=True),
        ]  

        jawaban = inquirer.prompt(pertanyaan)
        nomor_pilih = jawaban['pertanyaan']
        pilih = nomor_pilih.split('.')[0]

        if pilih == '1':
            clear()
            print("=== JENIS SENJATA TERSEDIA ===")

            pilihan = []
            for i in range(len(jenis_senjata)):
                pilihan.append(f"{i+1}. {jenis_senjata[i]}")
            pilihan.append(f"{len(jenis_senjata)+1}. Kembali")

            pertanyaan = [
                inquirer.List('pilihan',
                            message="Pilih jenis senjata",
                            choices=pilihan,
                            carousel=True),
            ]

            jawaban = inquirer.prompt(pertanyaan)
            nomor_jenis = jawaban['pilihan']
            if nomor_jenis == (f"{len(jenis_senjata)+1}. Kembali"):
                continue

            jenis = int(nomor_jenis.split('.')[0]) - 1

            if jenis < len(jenis_senjata):
                clear()

                print("\n--- REKOMENDASI SAAT INI ---")
                for i in range(len(rekomendasi_list[jenis])):
                    print("- " + rekomendasi_list[jenis][i])

                print("=== DAFTAR MODEL " + jenis_senjata[jenis].upper() + " YANG TERSEDIA ===")

                daftar_model = []
                for i in range(len(model_senjata[jenis])):
                    daftar_model.append(str(i+1) + ". " + model_senjata[jenis][i])
                daftar_model.append(f"{len(model_senjata[jenis])+1}. Kembali")
                
                pertanyaan_model = [
                    inquirer.List('daftar_model',
                                message="Pilih model senjata",
                                choices=daftar_model,
                                carousel=True),
                ]

                jawaban_model = inquirer.prompt(pertanyaan_model)
                nomor_model = jawaban_model['daftar_model']

                if nomor_model == (f"{len(model_senjata[jenis])+1}. Kembali"):
                    continue

                model_index = int(nomor_model.split('.')[0]) - 1
                nama = model_senjata[jenis][model_index]

                if nama in rekomendasi_list[jenis]:
                    print("Model sudah ada di daftar rekomendasi.")
                    pause()

                elif nama in model_senjata[jenis]:
                    rekomendasi_list[jenis].append(nama)
                    print("Model berhasil ditambahkan ke rekomendasi!")
                    pause()

            else:
                print("Jenis tidak valid!")
                pause()

        elif pilih == '2':
            clear()
            print('=== DAFTAR JENIS SENJATA ===')
            pilihan = []
            for i in range(len(jenis_senjata)):
                pilihan.append(f"{i+1}. {jenis_senjata[i]}")
            pilihan.append(f"{len(jenis_senjata)+1}. Kembali")

            pertanyaan = [
                inquirer.List('pilihan_jenis',
                            message="Pilih jenis senjata",
                            choices=pilihan,
                            carousel=True),
            ]

            jawaban = inquirer.prompt(pertanyaan)
            nomor_jenis = jawaban['pilihan_jenis']
            if nomor_jenis == (f"{len(jenis_senjata)+1}. Kembali"):
                continue

            jenis = int(nomor_jenis.split('.')[0]) - 1
            if jenis < len(jenis_senjata):
                clear()
                print(f"=== Daftar Rekomendasi {jenis_senjata[jenis]} ===")

                daftar_hapus = []
                for k in range(len(rekomendasi_list[jenis])):
                    daftar_hapus.append(f"{k+1}. {rekomendasi_list[jenis][k]}")
                daftar_hapus.append(f"{len(rekomendasi_list[jenis])+1}. Kembali")

                pertanyaan_hapus = [
                    inquirer.List('daftar_hapus',
                                message="Pilih rekomendasi yang ingin dihapus",
                                choices=daftar_hapus,
                                carousel=True),
                ]

                jawaban_hapus = inquirer.prompt(pertanyaan_hapus)
                nomor_hapus = jawaban_hapus['daftar_hapus']
                if nomor_hapus == (f"{len(rekomendasi_list[jenis])+1}. Kembali"):
                    continue

                hapus = int(nomor_hapus.split('.')[0]) - 1
                
                if hapus < len(rekomendasi_list[jenis]):
                    del rekomendasi_list[jenis][hapus]
                    print("Rekomendasi berhasil dihapus!")
                    pause()

        elif pilih == '3':
            break