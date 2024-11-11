#Nama : Ihsan Fathin Mohammed
#NIM : 2401413
#Kelas : 1C

radius = int(input("Masukkan radius tabung : "))
tinggi = int(input("Masukkan tinggi tabung : "))

def VolumeTabung (r,t):
    #rumus volume tabung (phi x r^2 x t)
    print(22/7*r**2*t)

VolumeTabung(radius,tinggi)