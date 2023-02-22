try:
    platnomor = input("Masukkan Plat Nomor : ")
    nomorkendaraan = int(platnomor.split()[1])

    if(0 <= nomorkendaraan <= 3000):
        print("Plat nomor tersebut diperuntukan untuk mobil")
    elif(3001 <= nomorkendaraan <= 4000):
        print("Plat nomor tersebut diperuntukan untuk motor")
    elif(4001<= nomorkendaraan <= 5000):
        print("Plat nomor tersebut diperuntukan untuk angkutan umum")
    else:
        print("Plat nomor tidak terindikasi ketiga angkutan tersebut")
    
except:
    print("Plat Nomor Tidak Terindikasi, harus terdapat nomor kendaraan setelah kode daerah")