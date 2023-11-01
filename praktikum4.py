# soal 1
nilai = int(13)
if nilai % 2 == 0:
    print(f" adalah angka genap")
else:
    print(f" adalah angka ganjil")

#soal 2
nilai = int(5)
if nilai == 0:
    print("Angka nol")
elif nilai % 2 == 0:
    print(f" bilangan ini adalah bilangan positif")
else:
    print(f" bilangan ini adalah bilangan negatif")

#soal 3

pemain_1 = input("gunting")
pemain_2 = input("kertas")
print(f"pemain_1 memilih gunting")
if pemain_1 == pemain_2:
    print("Hasil: Seri!")
elif pemain_2 == 'kertas':
    if pemain_2 == 'gunting':
        print("Hasil: Anda menang!")
    else:
        print("Hasil: Anda kalah!")
elif pemain_1 == 'gunting':
    if pemain_2 == 'kertas':
        print("Hasil: Anda menang!")
    else:
        print("Hasil: Anda kalah!")
elif pemain_1 == 'kertas':
    if pemain_2 == 'guntung':
        print("Hasil: Anda menang!")
    else:
        print("Hasil: Anda kalah!")
else:
    print("Masukkan tidak valid. Pastikan Anda memilih 'batu', 'gunting', atau 'kertas'.")
