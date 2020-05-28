def ebob(a,b):
    carpim=1
    i=2
    while (i <= sayi1 and i <= sayi2):
        if (a%i==0 and b%i==0):
            carpim*=i
            a=a/i
            b=b/i
           
        i+=1
    print("Sayıların Ebob'u:",carpim)

def ekok(a,b):
    sayi1=a
    sayi2=b
    i = 2
    ekok = 1
    while True:
        if (sayi1 % i == 0 and sayi2 % i == 0):
            ekok *= i

            sayi1 //= i
            sayi2 //= i


        elif (sayi1 % i ==  0 and sayi2 % i != 0):
            ekok *= i

            sayi1 //= i


        elif (sayi1 % i != 0 and sayi2 % i == 0):
            ekok *= i

            sayi2 //= i
        else:
            i += 1
        if (sayi1 == 1 and sayi2 == 1):
            break
    return ekok
    
while True:           
    print("""*****************************************
    EBOB EKOK BULMA UYGULAMASINA HOŞGELDİNİZ

    1-) Ebob Hesaplamak İçin 1'i Tuşlayınız 
    2_) Ekok Hesaplamak İçin 2'yi Tuşlayınız
    3-) Çıkmak İçin 3'ü Tuşlayınız

    *****************************************
    """)

    secim=input("Seçiminizi Girin:")

    if(secim=="1"):
        sayi1=int(input("Lütfen İlk Sayıyı Girin:"))
        sayi2=int(input("Lütfen İkinci Sayıyı Girin:"))
        ebob(sayi1,sayi2)
        input("Devam etmek için Enter'a basın")

    elif(secim=="2"):
        sayi1=int(input("Lütfen İlk Sayıyı Girin:"))
        sayi2=int(input("Lütfen İkinci Sayıyı Girin:"))
        print("Sayıların Ekokları:",ekok(sayi1,sayi2))
        input("Devam etmek için Enter'a basın")

    elif (secim=="3"):
        print("Çıkış Yapılıyor")
        break

