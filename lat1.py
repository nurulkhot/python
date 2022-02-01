# suhu= int(input("suhu: "))
# if(suhu<=23):
#     print("cuaca berawan")
# elif(suhu>23):
#     print("cuaca cerah")

# #FOR 
# for x in range(9,100):
#     print(x, end=" ")
# #rentang
# bawah= int(input("masukkan batas: "))
# atas= int(input("masukkan batas atas: "))
# for x in range (bawah, atas+1):
#     if (x%2)=0:
#         print(x, end=" ")

# #def untuk mendefinisikan fungsi buatan
# def hai(nama, panggilan):
#     print("Hai, %s,ini dari %s, Selamat ulang tahun ya, semoga panjang umur sehat selalu" % (nama, panggilan))

# hai("arfan","nurulk ")

# def luaspersegi(sisi):
#     return sisi*sisi

# sisi=int(input("masukkan panjang sisi: "))
# print("Luas persegi adalah: ", luaspersegi(sisi))

# def luassgtg(a,t):
#     return 1/2 *a*t
# a=int(input("alas: "))
# t= int(input("tinggi: "))
# print("luas segitiga adalah: ", luassgtg(a,t))

# #kasir jika beli diatas 50k dapat diskon 5k
# jumlah=int(input("jumlah: "))
# hrgsat=int (input("harga: "))
# def hitungtot(jumlah,hrgsat):
#     return jumlah*hrgsat
# def hitungNet (jumlah,hrgsat) :
#     return hitungtot(jumlah,hrgsat)-5000

# if (hitungtot(jumlah,hrgsat)>=50000):
#     print(hitungNet(jumlah,hrgsat))
# else:
#     print(hitungtot(jumlah,hrgsat))


# #untuk hitung faktorial
# angka=int(input("masukkan angka: "))
# def faktorial(angka):
#     if angka==0:
#         return 1
#     else :
#         return(angka*faktorial(angka-1))
# print ("faktorial",angka," = ",faktorial(angka) )




# mylist= [1,2,3,4,5,6,7,5,6]
# cari=int(input("masukkan angka: "))

# #fungsi
# def cariangka(list,search):
#     counter= 0
#     while counter !=len(mylist):
#         if mylist[counter]==search:
#              result = counter
#         counter +=1
#     return result

# #pemanggilan fungsi
# try: 
#     hasil= cariangka(mylist,cari)
#     if cari in mylist:
#         print("nomor %s ada di daftar %s" % (cari, hasil))
# except:
#     print("nomor tidak terdaftar")

# #binary search tanpa fungsi
# mylist=[1,2,3,4,5,8,6,10]
# mynumber= int(input("masukkan nomor yang dicar: "))
# firstindex=0
# lastindex= len(mylist)-1
# foundnumber=False
# mylist.sort() #binary search diurutkan
# while firstindex<= lastindex and not foundnumber:
#     middleindex=(firstindex +lastindex)//2 #cari index tengah
#     if mylist[middleindex]==mynumber:
#         foundnumber=True
#     else:
#         if mynumber< mylist[middleindex]:
#             lastindex=middleindex-1
#         else:
#             firstindex=middleindex+1
# if foundnumber:
#     print("nomor %s ada di list" % mynumber)
# else:
#     print("nomor %s tidak ada di list" % mynumber)





# #binary search dengan fungsi
# mylist=[1,2,3,4,5,8,6,10]
# mynumber= int(input("masukkan nomor yang dicar: "))

# #fungsi
# def searchnumb(mynumber,mylist):
#     foundnumber=False
#     mylist.sort()
#     firstindex=0
#     lastindex= len(mylist)-1
 
#     while firstindex<= lastindex and not foundnumber:
#         middleindex=(firstindex +lastindex)//2 #cari index tengah
#         if mylist[middleindex]==mynumber:
#             foundnumber=True
#         else:
#             if mynumber< mylist[middleindex]:
#                  lastindex=middleindex-1
#             else:
#                 firstindex=middleindex+1
#     return foundnumber

# #pemanggilan fungsi
# result=searchnumb(mynumber, mylist)
# if result:
#     print("nomor %s ada di list" % mynumber)
# else:
#     print("nomor %s tidak ada di list" % mynumber)


# #buble sort
# import time
# start_time=time.time()

# def urut(val):
#     for passnum in range(len(val)-1,0,-1):
#         for i in range(passnum):
#             if val[i]<val[i+1]: #mau lebih besar apa kecil
#                 temp=val[i]
#                 val[i]=val[i+1]
#                 val[i+1]=temp

# daftarangka=[23,60,80,1,2,3,4,5,6,76]
# urut(daftarangka)
# print(daftarangka)

# print("proses selesai---%s seconds---"%(time.time()-start_time))

#insetion sort
import time
start_time=time.time()

def InsertionSort(val):
    for index in range(1,len(val)):

        valueaktif=val[index]
        posisi=index
        while posisi>0 and val[posisi-1]>valueaktif:
         val[posisi]=val[posisi-1]
         posisi=posisi-1
        val[posisi]=valueaktif

daftarangka=[23,90,60,80,1,2,3,4,5,6,76]
InsertionSort(daftarangka)
print(daftarangka)

print("proses selesai---%s seconds---"%(time.time()-start_time))

