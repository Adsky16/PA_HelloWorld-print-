import random
from fungsi import clear, pause
from data import jenis_senjata, model_senjata
<<<<<<< HEAD
import inquirer
=======
>>>>>>> e4931f6032d848a51c730afe515aecf187898e3e

def menu_gacha():
    while True:
        clear()
        print("=== MENU GACHA SENJATA ===")
<<<<<<< HEAD

        pertanyaan = [
            inquirer.List('pilihan',
                        message="Pilih menu",
                        choices=['1. Gacha Random', '2. Gacha Pilih Class', '3. Gacha 2x (1 Random + 1 Pilih Class)', '4. Kembali'],
                        carousel=True),
        ]
        jawaban = inquirer.prompt(pertanyaan)
        nomor_pilihan = jawaban['pilihan']
        pilih = nomor_pilihan.split('.')[0]
=======
        print("1. Gacha Random")
        print("2. Gacha Pilih Class")
        print("3. Gacha 2x (1 Random + 1 Pilih Class)")
        print("4. Kembali")
        
        pilih = input("Pilih menu: ")
>>>>>>> e4931f6032d848a51c730afe515aecf187898e3e
        
        if pilih == '1':
            clear()
            print("=== GACHA RANDOM ===")
            
            jenis = random.randint(0, len(jenis_senjata) - 1)
            model = random.randint(0, len(model_senjata[jenis]) - 1)
            senjata = model_senjata[jenis][model]
            
            print(f"Senjata: {senjata}")
            print(f"Jenis: {jenis_senjata[jenis]}")
            pause()
            
        elif pilih == '2':
            clear()
            print("=== GACHA PILIH CLASS ===")
<<<<<<< HEAD

            pilihan = []
            for i in range(len(jenis_senjata)):
                pilihan.append(f"{i+1}. {jenis_senjata[i]}")
            pilihan.append(f"{len(jenis_senjata)+1}. Kembali")

            pertanyaan = [
                inquirer.List('pilihan_class', 
                            message="Pilih class",
                            choices=pilihan,
                            carousel=True),
            ]
            
            jawaban = inquirer.prompt(pertanyaan)
            pilih_class = jawaban['pilihan_class']

            if pilih_class == (f"{len(jenis_senjata)+1}. Kembali"):
                continue

            pilih = int(pilih_class.split('.')[0]) - 1

            if pilih < len(jenis_senjata):
                clear()
                print("=== HASIL GACHA ===")
                model = random.randint(0, len(model_senjata[pilih]) - 1)
                senjata = model_senjata[pilih][model]
                
                print(f"\nSenjata: {senjata}")
                print(f"Jenis: {jenis_senjata[pilih]}")
                pause()
=======
            for i in range(len(jenis_senjata)):
                print(f"{i+1}. {jenis_senjata[i]}")
            
            try:
                pilih_class = int(input("Pilih class: ")) - 1
                if pilih_class >= 0 and pilih_class < len(jenis_senjata):
                    model = random.randint(0, len(model_senjata[pilih_class]) - 1)
                    senjata = model_senjata[pilih_class][model]
                    
                    print(f"\nSenjata: {senjata}")
                    print(f"Jenis: {jenis_senjata[pilih_class]}")
                else:
                    print("Pilihan tidak valid!")
            except ValueError:
                print("Input harus angka!")
            pause()
>>>>>>> e4931f6032d848a51c730afe515aecf187898e3e
            
        elif pilih == '3':
            clear()
            print("=== GACHA PERTAMA (RANDOM) ===")
            
            jenis1 = random.randint(0, len(jenis_senjata) - 1)
            model1 = random.randint(0, len(model_senjata[jenis1]) - 1)
            senjata1 = model_senjata[jenis1][model1]
            
            print(f"Senjata: {senjata1}")
            print(f"Jenis: {jenis_senjata[jenis1]}")
            pause()
            
            clear()
            print("=== GACHA KEDUA (PILIH CLASS) ===")
<<<<<<< HEAD

            pilihan = []
            for i in range(len(jenis_senjata)):
                pilihan.append(f"{i+1}. {jenis_senjata[i]}")
            pilihan.append(f"{len(jenis_senjata)+1}. Kembali")

            pertanyaan = [
                inquirer.List('pilihan_class',
                            message="Pilih class",
                            choices=pilihan,
                            carousel=True),
            ]

            jawaban = inquirer.prompt(pertanyaan)
            pilih_class = jawaban['pilihan_class']

            if pilih_class == (f"{len(jenis_senjata)+1}. Kembali"):
                continue

            pilih = int(pilih_class.split('.')[0]) - 1
            
            if pilih < len(jenis_senjata):
                model2 = random.randint(0, len(model_senjata[pilih]) - 1)
                senjata2 = model_senjata[pilih][model2]
                
                clear()
                print("=== HASIL GACHA ===")
                print(f"Senjata 1: {senjata1} ({jenis_senjata[jenis1]})")
                print(f"Senjata 2: {senjata2} ({jenis_senjata[pilih]})")
                pause()
=======
            for i in range(len(jenis_senjata)):
                print(f"{i+1}. {jenis_senjata[i]}")
            
            try:
                pilih_class = int(input("Pilih class: ")) - 1
                if pilih_class >= 0 and pilih_class < len(jenis_senjata):
                    model2 = random.randint(0, len(model_senjata[pilih_class]) - 1)
                    senjata2 = model_senjata[pilih_class][model2]
                    
                    clear()
                    print("=== HASIL GACHA ===")
                    print(f"Senjata 1: {senjata1} ({jenis_senjata[jenis1]})")
                    print(f"Senjata 2: {senjata2} ({jenis_senjata[pilih_class]})")
                else:
                    print("Pilihan tidak valid!")
            except ValueError:
                print("Input harus angka!")
            pause()
>>>>>>> e4931f6032d848a51c730afe515aecf187898e3e
            
        elif pilih == '4':
            break
        else:
            print("Pilihan tidak valid!")
            pause()
<<<<<<< HEAD
=======
menu_gacha()
>>>>>>> e4931f6032d848a51c730afe515aecf187898e3e
