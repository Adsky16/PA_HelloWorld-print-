

jenis_senjata = (
    "Rifle", "SMG", "Shotgun", "LMG", "Marksman Rifle",
    "Sniper Rifle", "Pistol", "Senjata Khusus"
)

model_senjata = [
    ["M4A1", "AKM", "K416", "M7", "SG552", 'AK-12', 'SCAR-H', 'PTR-32', 'AS VAL', 'CI-19', 'K437', 'KC17'],  # Rifle
    ['MP5', 'P90', 'VECTOR', 'UZI', 'BIZON', 'SMG-45', 'SR-3M', 'VITYAZ', 'QCQ171', 'MP7'],  # SMG
    ['M1014', 'S12K', 'M870', '725 DOUBLE'],  # Shotgun
    ['PKM', 'M249', 'M250', 'QCB-201'],  # LMG
    ['MINI-14', 'VSS', 'SVD', 'M14', 'SKS', 'SR-25', 'SR-9', 'PSG-1', 'MARLIN LEVER'],  # Marksman
    ['SV-98', 'R93', 'M700', 'AWM'],  # Sniper
    ['M1911', 'DESERT EAGLE', 'QSZ-92G', 'G18', '93R', '357 REVOLVER'],  # Pistol
    ['COMPOUND BOW']  # Senjata Khusus
]

# Statistik setiap jenis
statistik_rifle = [
    {"Damage": 42, "Fire Rate": 750, "Accuracy": 70, "Mobility": 60, "Range": 60},
    {"Damage": 49, "Fire Rate": 600, "Accuracy": 65, "Mobility": 55, "Range": 55},
    {"Damage": 45, "Fire Rate": 700, "Accuracy": 68, "Mobility": 58, "Range": 58},
    {"Damage": 44, "Fire Rate": 720, "Accuracy": 69, "Mobility": 59, "Range": 59},
    {"Damage": 46, "Fire Rate": 680, "Accuracy": 67, "Mobility": 57, "Range": 57},
    {"Damage": 47, "Fire Rate": 660, "Accuracy": 66, "Mobility": 56, "Range": 56},
    {"Damage": 48, "Fire Rate": 640, "Accuracy": 64, "Mobility": 54, "Range": 54},
    {"Damage": 50, "Fire Rate": 620, "Accuracy": 63, "Mobility": 53, "Range": 53},
    {"Damage": 43, "Fire Rate": 730, "Accuracy": 71, "Mobility": 61, "Range": 61},
    {"Damage": 41, "Fire Rate": 760, "Accuracy": 72, "Mobility": 62, "Range": 62},
    {"Damage": 44, "Fire Rate": 710, "Accuracy": 68, "Mobility": 59, "Range": 59},
    {"Damage": 45, "Fire Rate": 700, "Accuracy": 67, "Mobility": 58, "Range": 58},
]

statistik_smg = [
    {"Damage": 30, "Fire Rate": 900, "Accuracy": 60, "Mobility": 80, "Range": 30},
    {"Damage": 28, "Fire Rate": 950, "Accuracy": 58, "Mobility": 82, "Range": 28},
    {"Damage": 32, "Fire Rate": 850, "Accuracy": 62, "Mobility": 78, "Range": 32},
    {"Damage": 29, "Fire Rate": 920, "Accuracy": 59, "Mobility": 81, "Range": 29},
    {"Damage": 27, "Fire Rate": 970, "Accuracy": 57, "Mobility": 83, "Range": 27},
    {"Damage": 31, "Fire Rate": 880, "Accuracy": 61, "Mobility": 79, "Range": 31},
    {"Damage": 33, "Fire Rate": 840, "Accuracy": 63, "Mobility": 77, "Range": 33},
    {"Damage": 26, "Fire Rate": 980, "Accuracy": 56, "Mobility": 84, "Range": 26},
    {"Damage": 34, "Fire Rate": 830, "Accuracy": 64, "Mobility": 76, "Range": 34},
    {"Damage": 25, "Fire Rate": 990, "Accuracy": 55, "Mobility": 85, "Range": 25},
]

statistik_shotgun = [
    {"Damage": 70, "Fire Rate": 300, "Accuracy": 50, "Mobility": 40, "Range": 10},
    {"Damage": 75, "Fire Rate": 280, "Accuracy": 48, "Mobility": 38, "Range": 90},
    {"Damage": 80, "Fire Rate": 260, "Accuracy": 46, "Mobility": 36, "Range": 80},
    {"Damage": 85, "Fire Rate": 240, "Accuracy": 44, "Mobility": 34, "Range": 70},
]

statistik_lmg = [
    {"Damage": 55, "Fire Rate": 600, "Accuracy": 60, "Mobility": 50, "Range": 40},
    {"Damage": 50, "Fire Rate": 650, "Accuracy": 58, "Mobility": 52, "Range": 38},
    {"Damage": 52, "Fire Rate": 620, "Accuracy": 59, "Mobility": 51, "Range": 39},
    {"Damage": 54, "Fire Rate": 610, "Accuracy": 57, "Mobility": 53, "Range": 37},
]

statistik_marksman = [
    {"Damage": 60, "Fire Rate": 500, "Accuracy": 75, "Mobility": 45, "Range": 50},
    {"Damage": 58, "Fire Rate": 520, "Accuracy": 77, "Mobility": 44, "Range": 52},
    {"Damage": 65, "Fire Rate": 480, "Accuracy": 80, "Mobility": 43, "Range": 55},
    {"Damage": 62, "Fire Rate": 510, "Accuracy": 76, "Mobility": 46, "Range": 51},
    {"Damage": 59, "Fire Rate": 530, "Accuracy": 78, "Mobility": 44, "Range": 53},
    {"Damage": 64, "Fire Rate": 490, "Accuracy": 79, "Mobility": 45, "Range": 54},
    {"Damage": 61, "Fire Rate": 505, "Accuracy": 74, "Mobility": 46, "Range": 55},
    {"Damage": 66, "Fire Rate": 475, "Accuracy": 81, "Mobility": 42, "Range": 56},
    {"Damage": 63, "Fire Rate": 495, "Accuracy": 73, "Mobility": 47, "Range": 49},
]

statistik_sniper = [
    {"Damage": 90, "Fire Rate": 200, "Accuracy": 90, "Mobility": 30, "Range": 80},
    {"Damage": 95, "Fire Rate": 180, "Accuracy": 92, "Mobility": 28, "Range": 85},
    {"Damage": 100, "Fire Rate": 160, "Accuracy": 94, "Mobility": 27, "Range": 90},
    {"Damage": 110, "Fire Rate": 150, "Accuracy": 95, "Mobility": 25, "Range": 95},
]

statistik_pistol = [
    {"Damage": 35, "Fire Rate": 400, "Accuracy": 65, "Mobility": 70, "Range": 20},
    {"Damage": 45, "Fire Rate": 350, "Accuracy": 60, "Mobility": 68, "Range": 18},
    {"Damage": 33, "Fire Rate": 420, "Accuracy": 66, "Mobility": 72, "Range": 21},
    {"Damage": 30, "Fire Rate": 450, "Accuracy": 67, "Mobility": 73, "Range": 22},
    {"Damage": 28, "Fire Rate": 480, "Accuracy": 68, "Mobility": 74, "Range": 23},
    {"Damage": 50, "Fire Rate": 300, "Accuracy": 55, "Mobility": 65, "Range": 17},
]

statistik_khusus = [
    {"Damage": 25, "Fire Rate": 100, "Accuracy": 85, "Mobility": 90, "Range": 15},
]

semua_statistik = [statistik_rifle, statistik_smg, statistik_shotgun, statistik_lmg, statistik_marksman, statistik_sniper, statistik_pistol, statistik_khusus]

# Rekomendasi
rekomendasi_list = [
    ['M4A1', 'AKM', 'K416'],
    ['MP5', 'P90', 'VECTOR'],
    ['M1014', 'S12K'],
    ['PKM', 'M249'],
    ['MINI-14', 'VSS'],
    ['SV-98', 'R93'],
    ['M1911', 'DESERT EAGLE'],
    ['COMPOUND BOW']
]

data_user = [
    ["admin", "1234", "admin"],
    ["user", "4321", "user"],
]
