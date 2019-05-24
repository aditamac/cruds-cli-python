import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="siswa_baru"
)

cursor = db.cursor()
sql = "UPDATE data_siswa SET nama=%s, alamat=%s, no_telp=%s, asal_sekolah=%s WHERE id_siswa=%s"
val = ("Dani", "Jl. Mataram, No. 2", "088192618281", "SMPN 7 Mataram", 1)
cursor.execute(sql, val)

db.commit()

print("{} data diubah".format(cursor.rowcount))