#Nama : Ihsan Fathin Mohammed
#NIM : 2401413
#Kelas : 1C

#deret fibonacci adalah  deret angka yang diperoleh dengan menjumlahkan dua angka sebelumnya
def fibonacci(n):
    n1,n2 = 0,1
    #awalan yang harus ada dalam deret fibonacci
    hasil=[]
    #variable kosong untuk menampung deret
    for i in range(n):
        hasil.append(n1)
        total = n1+n2
        n1 = n2
        n2 = total
    return hasil

n= int(input("masukan jumlah deret: "))
print(fibonacci(n))