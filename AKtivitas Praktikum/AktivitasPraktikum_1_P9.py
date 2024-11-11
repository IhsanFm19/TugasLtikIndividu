#Nama : Ihsan Fathin Mohammed
#NIM : 2401413
#Kelas : 1C

phi = 22/7
radius = int(input("Masukkan radius tabung : "))
tinggi = int(input("Masukkan tinggi tabung : "))

def VolumeTabung (r,t):
    #rumus volume tabung (phi x r^2 x t)
    print(phi*r**2*t)

VolumeTabung(radius,tinggi)

def LuasAlas (r):
    print(phi*r**2)

LuasAlas(radius)