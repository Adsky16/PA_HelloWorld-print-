from fungsi import clear



def menu_login():
    clear()
    print('=== LOGIN DELTA FORCE ARMORY ===')

    pertanyaan = [
        inquirer.List('pilihan',
                    message="Pilih menu",
                    choices=['1. Login', '2. Register', '3. Keluar'],
                    carousel=True),
    ]

    jawaban = inquirer.prompt(pertanyaan)
    nomor_pilihan = jawaban['pilihan']
    pilih = nomor_pilihan.split('.')[0]


    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu (1-3): ")



    return pilih