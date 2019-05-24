import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="siswa_baru"
)

cursor = db.cursor()
sql = "INSERT INTO data_siswa (nama, alamat, no_telp, asal_sekolah) VALUES (%s, %s, %s, %s)"
values = [
    ("Doni", "Jl. Gatot S., No. 2", "089123712837", "SMPN 5 Kediri"),
    ("Ginanjar", "Jl.Sudirman, No. 5", "087653471521", "SMPS 2 Kediri"),
    ("Sukma", "Jl. Dr. Saharjo, No. 3", "089765654786", "SMPN 1 Kediri"),
    ("Ali", "Jl. Basuki Rahmat, No. 1", "087621625511", "SMPN 7 Kediri")
]

for val in values:
    cursor.execute(sql, val)
    db.commit()

print("{} data ditambahkan".format(len(values)))