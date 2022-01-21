import mysql.connector
import os

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_akademik_0581"
)

def show_data(db):
    cursor = db.cursor()
    sql = "SELECT * FROM tbl_students_0581"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print("No = ", row[0], )
        print("NIM = ", row[1])
        print("Nama = ", row[2])
        print("JK = ", row[3])
        print("Jurusan = ", row[4])
        print("Alamat = ", row[5])
        print("\n")

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            cursor.close()

def show_limit(size):
    cursor = db.cursor()
    sql = "SELECT * FROM tbl_students_0581"
    cursor.execute(sql)
    results = cursor.fetchmany(size)
    
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for row in results:
            print("No = ", row[0], )
            print("NIM = ", row[1])
            print("Nama = ", row[2])
            print("JK = ", row[3])
            print("Jurusan = ", row[4])
            print("Alamat = ", row[5])
            print("\n")

def search_data(db):
    cursor = db.cursor()
    keyword = input("Masukkan NIM: ")
    sql = "SELECT * FROM tbl_students_0581 WHERE NIM LIKE %s"
    val = ["%{}%".format(keyword)]
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for row in results:
            print("No = ", row[0], )
            print("NIM = ", row[1])
            print("Nama = ", row[2])
            print("JK = ", row[3])
            print("Jurusan = ", row[4])
            print("Alamat = ", row[5])
            print("\n")


def show_menu(db):
    print("1. Tampilkan semua data")
    print("2. Tampilkan data berdasarkan limit")
    print("3. Cari data berdasarkan NIM")
    print("0. Keluar")
    menu = input("Pilih Menu : ")

    if menu == "1":
        show_data(db)

    elif menu == "2":
        show_limit(int(input("Masukkan Limit : ")))

    elif menu == "3":
        search_data(db)

    elif menu == "0":
        exit()

    else:
        print("Menu Salah!") 

if __name__ == "__main__":
    while(True):
        show_menu(db)