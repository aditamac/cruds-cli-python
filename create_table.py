import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="siswa_baru"
)

cursor = db.cursor()
sql = """CREATE TABLE data_siswa (
    id_siswa INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255),
    alamat VARCHAR(255),
    no_telp VARCHAR(255),
    asal_sekolah VARCHAR(255)
)
"""
cursor.execute(sql)

print("Tabel data_siswa berhasil dibuat!")