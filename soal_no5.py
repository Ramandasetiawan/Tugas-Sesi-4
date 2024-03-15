#menetukan ganjil genap, positif, negatif atau 0

nilai = int(input("Masukan bilangan :"))
if nilai > 0:
    if nilai % 2 == 0:
        print(nilai," Bilangan positif genap")
    else:
        print("Bilangan positif ganjil")
elif nilai < 0:
    if nilai % 2 == 0:
        print(nilai," Bilangan negatif genap")
    else:
        print(nilai," Bilangan negatif ganjil")
else:
    print(nilai,"Bilangan netral")