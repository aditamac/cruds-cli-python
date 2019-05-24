import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="siswa_baru"
)

cursor = db.cursor()
sql = "DELETE FROM data_siswa WHERE id_siswa=%s"
val = (1, )
cursor.execute(sql, val)

db.commit()

print("{} data dihapus".format(cursor.rowcount))