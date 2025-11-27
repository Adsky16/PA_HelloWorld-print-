from fungsi import clear, pause
from data import data_user

def register():
    clear()
    print('=== REGISTER AKUN ===')
    while True:
        username = input("Masukkan username: ")

        if not username.strip():
            print("Username tidak boleh kosong!")
            continue

        if ' ' in username:
            print("Username tidak boleh mengandung spasi!")
            continue

        duplicate = False

        for user in data_user:
            if user[0] == username:
                print("Username sudah digunakan, gantii!")
                duplicate = True
                break
        
        if duplicate:
            continue
        break
                
    while True:
        password = input("Masukkan password: ")

        if not password.strip():
            print("Password tidak boleh kosong!")
            continue

        if ' ' in password:
            print("Password tidak boleh mengandung spasi!")
            continue
        break
    
    data_user.append([username, password, "user"])
    print("Akun berhasil dibuat!")
    pause()
