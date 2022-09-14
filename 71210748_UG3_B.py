#Angela Gracia
#UG3

user = int(input("Masukkan range data: "))
def faktorial(a):
     if a == 0 or a == 1:
       return a
   else:
       return a*faktorial(a-1)

urutan = []
for i in range (0,user):
    if i % 2 == 0:
        urutan.append(i)
    else:
        continue

urutan_faktorial =[]
for j in urutan:
    if j % 2 == 0:
       nomor = faktorial(j)
        urutan_faktorial.append(nomor)
    else:
        continue
b = dict(zip(urutan, urutan_faktorial))

print(b)

menghitung = int(input("Data Ditampilkan:"))
if menghitung in b:
    print("Data ditemukan")
    print("Data yang ditemukan bernilai: ",dikt.get(menghitung))
else:
    print("Data tidak ditemukan")
    
