try:
    namalengkap = input("Masukkan Nama Lengkap Anda: ")
    prodianda = input("Masukkan Prodi Anda: ")
    nilaihuruf = input("Masukkan Nilai (dalam huruf) yang Anda Dapat: ").upper()

    if(nilaihuruf == "A"):
        print("Nilai anda adalah 4.0, tbl tbl serem bgtlohh")
    elif(nilaihuruf == "A-"):
        print("Nilai Anda adalah 3.75, kamu keren!")
    elif(nilaihuruf == "B+"):
        print("Nilai Anda adalah 3.25, okelah not bad")
    elif(nilaihuruf == "B"):
        print("Nilai Anda adalah 3.0, oke lah naikin lagi dong nilainya")
    elif(nilaihuruf == "B-"):
        print("Nilai Anda adalah 2.75, kurang semangat belajar nihh")
    elif(nilaihuruf == "C+"):
        print("Nilai Anda adalah 2.25, ayo dong belajar lebih giat lagii")
    elif(nilaihuruf == "C"):
        print("Nilai Anda adalah 2.0, yaa at least Anda harus ada + nya sih")
    elif(nilaihuruf == "D"):
        print("Nilai Anda adalah 1.0, apakah sudah ada pikiran untuk pindah jurusan?")
    elif(nilaihuruf == "E"):
        print("Nilai Anda adalah 0, niat kuliah nggak sih???")
    else:
        print("Inputan nilai yang Anda masukkan tidak valid")

except:
    pass
        