import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def keluar():
    print("Terima kasih dan sampai jumpa!")
    sys.exit()

def pause():
    input('\nEnter untuk lanjut')