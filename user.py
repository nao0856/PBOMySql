from db import Database

class User:
    def __init__(self, nim, nama, prodi):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi

    def save(self):
        db = Database()
        query = "INSERT INTO mahasiswa(nim, nama, prodi) VALUES(%s, %s, %s)"
        db.execute(query, (self.nim, self.nama, self.prodi))
        db.close()

    @staticmethod
    def all():
        db = Database()
        users = db.execute("SELECT * FROM mahasiswa").fetchall()
        db.close()
        return users