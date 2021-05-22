# programci hatalari => çözülmesi en kolay hatalardır. hangi sayfada ve hangi satırda hata yaptığınız terminal üzerinde yer alır.
# istisnai  hatalar  => bu gibi hataların kesin çözümü yoktur. örn (internet gitmesi, elektrik kesintisi, server kapanması vs. )
# mantikal  hatalar  => çözümü en zor hata tipleri.   

# print("abc") # printten önce boşluk olduğu için hata verir

# sayi = 10 
# isim = "lale"
# mail = "lale.emanet@outlook.com" 
# print("Hello World") 

# sayi = int(input("Lütfen Sayı Giriniz : "))
# print("Tebrikler, hayattaki en büyük başarın...")

 
# phonenummer = int(input("Lütfen Telefon Numaranızı Giriniz : "))
# print("Tebrikler Sisteme Telefon Numaranız {} olarak Kaydedilmiştir".format(phonenummer))


try:
    phonenummer = int(input("Lütfen Telefon Numaranızı Giriniz : "))
    print("Tebrikler Sisteme Telefon Numaranız {} olarak Kaydedilmiştir".format(phonenummer))
except:
    print("Beceriksiz :)")

print("Telefon Rehberi Sistemi")