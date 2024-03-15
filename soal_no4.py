#program untuk menentukan balangan positif,negatif,atau 0

bilangan =int(input("masukan nilai :"))
if bilangan >0 :
    hasil = "bilangan %i adalah bilangan positif"%(bilangan)
elif bilangan <0 :
    hasil = "bilangan %i adalah bilangan negatif"%(bilangan)
else :
    hasil ="bilangan netral netral=0 "
print(hasil)