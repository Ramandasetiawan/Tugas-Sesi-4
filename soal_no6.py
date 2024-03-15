#segita

sisi_A = float(input("Tentukan sisi pertama_A : "))
sisi_B = float(input("Tentukan sisi ke-dua_B : "))
sisi_C = float(input("Tentukan sisi ke-tiga_C : "))

P = sisi_A + sisi_B + sisi_C
S = P / 2
L = (S*(S-sisi_A)*(S-sisi_B)*(S-sisi_C))**0.5

print("Keliling segitiga adalah ", P, "dan  luas segitiga adalah ", L)