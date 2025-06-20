from mhs import mhs

# Menambahkan user baru
u = mhs("20230040201", "Septian Adiwiguna", "Teknik Informatika")
u.save()

# Menampilkan semua user
users = mhs.all()
for mhs in users:
    print(f"{mhs['nim']} {mhs['nama']} - {mhs['prodi']}")