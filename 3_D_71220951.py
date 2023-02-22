awalderet = int(input("Masukkan awal deret: "))
akhirderet = int(input("Masukkan akhir deret: "))

deretnya = ' '.join([str(i) for i in range(awalderet, akhirderet) if i%6!=0 and i%8!=0])
print(deretnya)