#Nama : Ihsan Fathin Mohammed
#NIM : 2401413
#Kelas : 1C

def Login():
    username = "Daspro2023"
    password = "Latihan"

    maksimalPercobaan = 3
    percobaan = 0

    while percobaan < maksimalPercobaan:
        if str(input("username : ")) == username:
            if str(input("password : ")) == password:
                print("Login Berhasil !!")
                break
            else :
                percobaan += 1
                print(f"Password Salah, kesempatan anda {3 - percobaan}kali lagi")
        else :
            percobaan += 1
            print(f"Username Salah, kesempatan anda {3 - percobaan}kali lagi ")
    else:
        print("Anda diblokir !!")

Login()
            
            