#input 3 buah bilangan dan tentukan bilangan mana yang lebih besar, 2 bilangan lebih besar dari yang lain atau semua bilangan sama besar

X = int(input("Masukan nilai 1 :"))
Y = int(input("Masukan nilai 2 :"))
Z = int(input("Masukan nilai 3 :"))

if X > Y and Z > Y:
    print(X," dan ", Z, " Lebih besar dari ",Y)
elif Y > X and Z > X:
    print(Y, " dan ", Z, " lebih besar dari ", X)
elif Y > Z and X > Z:
    print(X , " dan ", Y , " lebih besar dari ", Z)
elif X == Y and X > Z:
    print(X, " dan ",Y, " lebih besar dari ", Z)
elif X == Z and X > Y:
    print(X, " dan ",Z, " lebih besar dari ", Y)
elif Y == Z and Y > X:
    print(Y, " dan ",Z, " lebih besar dari ", X)
elif X == Y and X < Z:
    print(Z, " lebih besar dari ",X, " dan ", Y)
elif X == Z and X < Y:
    print(Y, " lebih besar dari ",X, " dan ", Z)
elif Y == Z and Y < X:
    print(X, " Lebih besar dari ",Y, " dan ", Z)
else:
    print(X, Y, Z, " sama besar")