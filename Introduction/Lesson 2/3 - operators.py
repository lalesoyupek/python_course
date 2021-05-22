# Aritmetik Operatorler

# +(toplama) , -(cikartma) , /(bolme) , *(carpma) , %(mod)

sayi1 = 120
sayi2 = 50

toplam = sayi1 + sayi2
print("Toplama İşlemi Sonucu :", toplam)


# Kullanıcıdan değer almak istiyorsak,
# input metodu

number1 = input('Lütfen 1. Sayıyı Giriniz : ')
print(number1)
print(type(number1))

# input üzerinden aldığınız her değer mutlak suretle (str) metinsel olarak gelecektir.

fark = sayi1 - sayi2
print("Çıkartma İşlemi Sonucu :", fark)

carpim = sayi1 * sayi2
print("Çarpma İşlemi Sonucu   :", carpim)

bolme = sayi1 / sayi2
print("Bölme İşlemi Sonucu    :", bolme)

mod = sayi1 % sayi2
print("Mod Alma İşlemi Sonucu :", mod)
