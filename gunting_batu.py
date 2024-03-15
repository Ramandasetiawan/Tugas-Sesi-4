#Gunting Batu

pilihan1 = str(input("Masukan pilihan anda : "))
pilihan2 = str(input("Masukan pilihan anda : "))

X= "kertas"
Y= "gunting"
Z= "batu"

if pilihan1 == X and pilihan2 == Y:
    print(b, " menang dari ", X)
elif pilihan1 == Y and pilihan2 == Z:
    print(Z, " menang dari ", Y)
elif pilihan1 == Z and pilihan2 == X:
    print(X, " menang dari ", Z)
elif pilihan1 == Y and pilihan2 == X:
    print(X, " menang dari ", Y)
elif pilihan1 == Z and pilihan2 == Y:
    print(Y, " menang dari ", Z)
elif pilihan1 == X and pilihan2 == Z:
    print(Z, " menang dari ", X)
else:
    print("seri")