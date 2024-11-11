#Nama : Ihsan Fathin Mohammed
#NIM : 2401413
#Kelas : 1C

angka = input("Input angka (contoh= 1,2,3,4):")

def RataRataAngka (angka):
    #split untuk memisahkan input selanjutnya dengan (,) lalu diubah ke integer
    angka = [int(i) for i in angka.split(",")] 

    count = len(angka) #acuan berapa angka yang di input untuk pembagi
    total = sum(angka) #penjumlahan angka yang di input
    RataRata = total / count
    print(f"totalnya adalah {total}")
    return RataRata

print(f"rata-ratanya adalah {RataRataAngka(angka)}")

