print("""
==============================================
    
        Program Untuk Mengetahui
            Klasifikasi Iklim
             Schmid Ferguson 

==============================================
==============================================
""")

daerah=(input("Masukkan nama daerah/stasiun: "))

bb=int(input("jumlah bulan basah: "))
bk=int(input("jumlah bulan kering: "))

hasil=(bb/bk)
indeks=""
if hasil>=7:
    indeks="LUAR BIASA KERING"
elif hasil >=3:
    indeks="SANGAT KERING"
elif hasil >=1.67:
    indeks="KERING"   
elif hasil >=1.0:
    indeks="AGAK KERING"
elif hasil >=0.60:
    indeks="SEDANG"  
elif hasil >=0.33:
    indeks="AGAK BASAH"  
elif hasil >=0.143:
    indeks="BASAH"  
else:
    indeks="SANGAT BASAH"

print("Hasil hitung rasio penggolongan iklim:  %s"%hasil)
print("Daerah %s memiliki klasifikasi iklim:  %s" % (daerah, indeks))