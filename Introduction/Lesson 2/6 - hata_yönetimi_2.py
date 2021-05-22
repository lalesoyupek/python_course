try:
    sayi1 = int(input("Lütfen Birinci Sayıyı Giriniz : "))
    sayi2 = int(input("Lütfen İkinci Sayıyı Giriniz : "))

    toplam = sayi1 + sayi2
    fark   = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum  = sayi1 / sayi2
    mod    = sayi1 % sayi2
    result = 0 / 0
    print(f"Toplama İşlemi Sonucu : {toplam}\nÇıkartma İşlemi Sonucu : {fark}\nÇarpım İşlemi Sonucu : {carpim}\nBölme İşlemi Sonucu : {bolum}\nMod Alma İşlemi Sonucu : {mod}") 

except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except OverflowError:
    print("OverflowError")
except MemoryError:
    print("")
except:
    print("Lütfen 0 ile 9 aralığında olan değerleri kullanınız.")