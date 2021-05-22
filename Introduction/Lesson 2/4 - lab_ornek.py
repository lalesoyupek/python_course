# örnek 1) dışarıdan alınan 2 sayının toplamıyla farkının bölümünden kalanı kaçtır

def Ornek1():
    # 1) dışarıdan alınan 2 sayı
    sayi1 = float(input("Lütfen 1. Sayıyı Giriniz : "))
    sayi2 = float(input("Lütfen 2. Sayıyı Giriniz : "))

    # 2) dışarıdan alınan 2 sayının toplamı
    toplam = sayi1 + sayi2

    # 3) dışarıdan alınan 2 sayının farkı
    fark = sayi1 - sayi2

    # 4)  bölümünden kalanı kaçtır
    mod = toplam % fark
    print("İşlem Sonucu :", mod)

# Ornek1()

# soru 1
sayi3 = input("sayi1:")
sayi4 = input("sayi2:")
print((int(sayi3)+int(sayi4))
      %
      (int(sayi3)-int(sayi4))
      )

##############################################################################
# örnek 2) dışarıdan girilen bir sayının 10 eksiğinin 20 fazlasının ikiye bölümünden kalan kaçtır

def Ornek2():
    # dışarıdan girilen bir sayı
    sayi = int(input("Lütfen Sayı Giriniz : "))

    # dışarıdan girilen bir sayının 10 eksiği
    sayi = sayi - 10

    # 20 fazlası
    sayi = sayi + 20

    # ikiye bölümünden kalan
    sayi = sayi % 2

    print("İşlem Sonucu :", sayi)

def Ornek2V2():
    print("İşlem Sonucu :", ((int(input("Lütfen Sayı Giriniz : ")) - 10) + 20) % 2)

# Ornek2()

# soru 2
sayi5 = input("sayıyı giriniz:")
print((int(sayi5) - 10 + 20) % 2)

##############################################################################
# örnek 3) dışarıdan girilen iki sayının karelerinin toplamı ile karelerinin farkı toplamı kaçtır.

def Ornek3():
    # dışarıdan girilen iki sayı
    sayi1 = int(input("Lütfen 1. Sayıyı Giriniz : "))
    sayi2 = int(input("Lütfen 2. Sayıyı Giriniz : "))

    # iki sayının kareleri
    kare1 = sayi1**2
    kare2 = sayi2**2

    # karelerinin toplamı
    toplam = kare1 + kare2

    # karelerinin farkı
    fark = kare1 - kare2

    # toplamı kaçtır.
    result = toplam + fark
    print("İşlem Sonucu :", result)

# Ornek3()

# soru 3
sayi6 = int(input("sayı 1 giriniz:"))
sayi7 = int(input("sayı 2 giriniz:"))
result = (sayi6**2 + sayi7**2) + (sayi6**2 - sayi7**2)
print(result)

##############################################################################
# örnek 4) Vize notu %30, final notu %70'ini alıp not ortalamasını hesaplayıp kullanıcıya aldığı not'u gösteriniz

def Ornek4():
    vize = float(input("Lütfen Vize Notunuzu Giriniz : "))
    final = float(input("Lütfen Final Notunuzu Giriniz : "))
    _not = (vize * 0.30) + (final * 0.70)
    print("Not Ortalamanız :", _not)

# Ornek4()

# soru 4
vize = int(input("vize giriniz:"))
final = int(input("final giriniz:"))
nott = (vize*0.3 + final*0.7)
print(nott)

##############################################################################
# örnek 5) Kullanıcı ilk olarak adını, 2 olarak ise soyismini girsin, işlem sonunda kullanıcıya   isim.soyisim@hotmail.com şeklimnde mail adersini teslim ediniz.

def Ornek5():
    firstName = input("Lütfen Adınızı Giriniz : ")
    lastName = input("Lütfen Soyadınızı Giriniz : ")
    mail1 = firstName + "."+lastName + "@hotmail.com"
    # placeholder => yer tutucu , formatlı yazım
    mail2 = "{}.{}@hotmail.com".format(firstName, lastName)
    # => murat.murat@hotmail.com
    mail3 = "{0}.{0}@hotmail.com".format(firstName, lastName)
    # => vuranok.vuranok@hotmail.com
    mail4 = "{1}.{1}@hotmail.com".format(firstName, lastName)
    # => murat.vuranok@hotmail.com
    mail4 = "{0}.{1}@hotmail.com".format(firstName, lastName)
    # => vuranok.murat@hotmail.com
    mail4 = "{1}.{0}@hotmail.com".format(firstName, lastName)

    result = "{} derslerinde Müfredat {} tarafından hazırlanır ve dersler {} binasında verilir. Dersinizin İçeriği {} Olarak Belirlenmiştir. Eğitmen Olarak {} Gelecektir. {} X firmasında tam zamanlı çalışmaktadır. Ayrıca {} yarı zamanlı {}  personelidir.".format(
        "BilgeAdam", "BilgeAdam", "BilgeAdam", "Python", "Murat Vuranok", "Murat Vuranok", "Murat Vuranok", "BilgeAdam")

    retVal = "{0} derslerinde Müfredat {0} tarafından hazırlanır ve dersler {0} binasında verilir. Dersinizin İçeriği {1} Olarak Belirlenmiştir. Eğitmen Olarak {2} Gelecektir. {2} X firmasında tam zamanlı çalışmaktadır. Ayrıca {2} yarı zamanlı {0}  personelidir.".format(
        "BilgeAdam", "Python", "Murat Vuranok")

    # print(retVal)
    # print(result)
    # print(mail1)
    # print(mail2)
    # print(mail3)

    mail = "{}.{}@hotmail.com".format(firstName, lastName)
    mail = f"{firstName}.{lastName}@hotmail.com"
    print(mail)

Ornek5()

# soru 5 
adi = input("adınızı giriniz:")
soyadi = input("soyadınızı giriniz:")
print(adi+'.'+soyadi+'@hotmail.com')
print(adi, soyadi, sep='.', end='@hotmail.com\n' )

##############################################################################
# NOT : Dışarıdan gelen değer mutlak suretle string (metinsel) değerdir. İşlem yaparken göz önünde bulundurunuz.

# placeholder -> yer tutucu, formatlı yazım
mail = "{}.{}@hotmail.com".format(adi, soyadi)
print(mail) # lale.emanet@hotmail.com

mail2 = "{0}.{1}@hotmail.com".format(adi, soyadi)
print(mail2) # lale.emanet@hotmail.com

mail3 = "{0}.{0}@hotmail.com".format(adi, soyadi)
print(mail3) # lale.lale@hotmail.com

mail4 = "{1}.{0}@hotmail.com".format(adi, soyadi)
print(mail4) # emanet.lale@hotmail.com

mail5 = "{x}.{y}@hotmail.com".format(x=adi, y=soyadi)
print(mail5) # lale.emanet@hotmail.com

mail6 = f"{adi}.{soyadi}@hotmail.com"
print(mail6) # lale.emanet@hotmail.com

print("%s.%s@hotmail.com" % (adi, soyadi)) # lale.emanet@hotmail.com
# int bir değer varsa %i olacak


##############################################################################
retval = "{0} derslerinde müfredat {0} tarafından hazırlanır ve dersler {0} binasında verilir. Dersinizin içeriği {2} olarak belirlenmiştir. Eğitmen olarak {1} gelecektir. {0} X firmasında tam zamanlı çalışmaktadır. Ayrıca {1} yarı zamanlı {2} personelidir. ".format("BilgeAdam", "Python", "Murat Vuranok")

print(retval)

#  [ 1 , 2 , 3 , 4 , 5 , 6 ]
#    0   1   2   3   4   5    => max index değeri, eleman sayısı -1 