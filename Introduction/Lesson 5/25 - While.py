##while(True):
##    print("Bilge Adam")

# Yukarıda yer alan döngü çeşidi, sonsuz döngüdür.

##############################################################################
index = 0
while index <= 100:
    print(index)
    index = index + 1

##############################################################################
# 0 ile 100(dahil) çift sayıları ekrana yazdırınız.
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
    i = i + 1


i = 0
while i <= 100:
    print(i)
    i = i + 2

##############################################################################
# 1 ile 1000(dahil) arasındaki tek sayıla çift sayıların toplam adedini ekrana yazdırınız.
i = 1
tek_sayilar = 0
cift_sayilar = 0
while i <= 1000:
    if i % 2 == 0:
        cift_sayilar = cift_sayilar + 1
    else:
        tek_sayilar = tek_sayilar + 1
    i = i + 1

print(f"Tek sayıların toplamı : {tek_sayilar}\nÇift sayıların toplamı : {cift_sayilar}")

##############################################################################
# Kullanıcın dışarıdan girdiğimi metni alt alta yazdırınız
# Örnek => murat
# m
# u
# r
# a
# t

import os
os.system('cls')


metin = input('lütfen metin giriniz : ')
index = 0
while index < len(metin):
    print(metin[index])
    index += 1

##############################################################################
# Kullanıcın dışarıdan girdiği sayıların toplamını ekrana yazdıran bir uygulama yazınız
# 123  => 1 + 2 + 3 = 6

i = 0
sayi = input('Lütfen sayı giriniz : ')
result = 0

while i < len(sayi):
    result += int(sayi[i])
    i += 1

print(result)
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
