#input 3 buah bilangan dan tentukan bilangan mana yang lebih kecil

bilangan_1 =int(input("masukan bilangan 1 :"))
bilangan_2 =int(input("masukan bilangan 2 :"))
bilangan_3 =int(input("masukan bilangan 3 :"))

if bilangan_1 < bilangan_2 and bilangan_1 < bilangan_3 :
    hasil ="bilangan 1 adalah bilangan paling kecil dari bilangan 2 dan 3 :"
elif bilangan_2 < bilangan_1 and bilangan_2 < bilangan_3 :
    hasil ="bilangan 2 adalah bilangan paling kecil dari bilangan 1 dan 3 :"
elif bilangan_3 < bilangan_1 and bilangan_3 < bilangan_2 :
    hasil ="bilangan 3 adalah bilangan paling kecil dari bilangan 1 dan 2 :"
else :
    hasil = ("semua bilanagan sama :")
print(hasil)