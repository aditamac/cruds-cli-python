import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="siswa_baru"
)


def insert_data(db):
  nama = input("Masukan nama: ")
  alamat = input("Masukan alamat: ")
  no_telp = input("Masukan no telepon: ")
  asal_sekolah = input("Masukan asal sekolah: ")
  val = (nama, alamat, no_telp, asal_sekolah)
  cursor = db.cursor()
  sql = "INSERT INTO data_siswa (nama, alamat, no_telp, asal_sekolah) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM data_siswa"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  id_siswa = input("pilih id siswa> ")
  nama = input("Nama baru: ")
  alamat = input("Alamat baru: ")
  no_telp = input("No telepon baru: ")
  asal_sekolah = input("Asal sekolah baru: ")

  sql = "UPDATE data_siswa SET nama=%s, alamat=%s, no_telp=%s, asal_sekolah=%s WHERE id_siswa=%s"
  val = (nama, alamat, no_telp, asal_sekolah, id_siswa)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  id_siswa = input("pilih id siswa> ")
  sql = "DELETE FROM data_siswa WHERE id_siswa=%s"
  val = (id_siswa,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM data_siswa WHERE nama LIKE %s OR alamat LIKE %s OR no_telp LIKE %s OR asal_sekolah LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI DATA SISWA BARU ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)