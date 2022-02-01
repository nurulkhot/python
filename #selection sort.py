# #!/usr/bin/python 
# import time
# start_time = time.time()

# def InsertionSort(val):
#    for index in range(1,len(val)):
       
#        valueaktif = val[index]
#        posisi = index
#        while posisi>0 and val[posisi-1]>valueaktif:
#          val[posisi]=val[posisi-1]
#          posisi = posisi-1
         
#          val[posisi]=valueaktif

# DaftarAngka = [23,7,32,99,4,15,11,20]
# InsertionSort(DaftarAngka)
# print(DaftarAngka)

# print("Process finished --- %s seconds ---" % (time.time() - start_time))

import time
start_time = time.time()

def InsertionSort(val):
    for index in range(1,len(val)):

        valueaktif = val[index]
        posisi=index
        while posisi>0 and val[posisi-1]>valueaktif:
            val[posisi]=val[posisi-1]
            posisi=posisi-1

        val[posisi]=valueaktif

DaftarAngka=[1,2,11,23,0,45,56,12]
InsertionSort(DaftarAngka)
print(DaftarAngka)

print("proses selesai---%s second--"%(time.time()-start_time))