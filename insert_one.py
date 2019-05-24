import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="siswa_baru"
)

cursor = db.cursor()
sql = "INSERT INTO data_siswa (nama, alamat, no_telp, asal_sekolah) VALUES (%s, %s, %s, %s)"
val = ("Dian", "Jl. Balowerti, No. 3", "081216310829", "SMPN 4 Kediri")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))