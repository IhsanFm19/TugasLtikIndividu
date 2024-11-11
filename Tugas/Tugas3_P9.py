#Nama : Ihsan Fathin Mohammed
#NIM : 2401413
#Kelas : 1C

def selisih (jamMulai, menitMulai, detikMulai, jamSelesai, menitSelesai, detikSelesai):
    waktuMulai = jamMulai*3600 + menitMulai*60 + detikMulai
    waktuSelesai = jamSelesai*3600 + menitSelesai*60 + detikSelesai

    selisihWaktu = waktuSelesai - waktuMulai

    jam = selisihWaktu//3600
    menit = (selisihWaktu%3600)//60
    detik = selisihWaktu % 60
    return (f"Selisih waktunya yaitu {jam} jam - {menit} menit - {detik} detik")

print("Masukkan Waktu Mulai berlari")
jamMulai = int(input("Jam:"))
menitMulai = int(input("Menit:"))
detikMulai = int(input("Detik:"))
print("Masukkan Waktu Akhir berlari")
jamSelesai = int(input("Jam:"))
menitSelesai = int(input("Menit:"))
detikSelesai = int(input("Detik:"))

print(selisih(jamMulai, menitMulai, detikMulai, jamSelesai, menitSelesai, detikSelesai))
