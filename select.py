import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="siswa_baru"
)

cursor = db.cursor()
sql = "SELECT * FROM data_siswa"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)