from fungsi import keluar, pause
from tampil_model import tampil_model
from tampil_rekom import tampil_rekomendasi
from update_rekom import update_rekomendasi
from kelola_model_stat import kelola_model_statistik
from ulang_login import ulang_login
from register import register
from menu_login import menu_login
from menu_utama import menu_utama
from gacha import menu_gacha

def utama():
    while True:
        pilih = menu_login()
        if pilih == '1':
            status = ulang_login()
            while True:
                menu = menu_utama(status)
                if menu == '1':
                    tampil_model()
                elif menu == '2':
                    tampil_rekomendasi()
                elif menu == '3':
                    menu_gacha()
                elif status == "admin" and menu == '4':
                    update_rekomendasi()
                elif status == "admin" and menu == '5':
                    kelola_model_statistik()
                elif (status == "admin" and menu == '6') or (status == "user" and menu == '4'):
                    break
                else:
                    print("Pilihan tidak valid!")
                    pause()
        elif pilih == '2':
            register()
        elif pilih == '3':
            print("Keluar dari program.")
            keluar()

utama()