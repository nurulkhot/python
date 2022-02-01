kkunci= input("pasword: ")
if(kkunci=="123"):
    print ("pasword benar")
else:
    print("sayang sekali pasword salah!")

bil= int(input("masukkan angka: "))
if bil < 0:
    print ("masukkan salah")
else: 
    if bil%2 == 0 :
        print("%d genap" % bil)
    else:
        print("%d ganjil" % bil)