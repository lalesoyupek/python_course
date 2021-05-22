# VARIABLE

# Number    : int - long - float - complex
# String    : 
# List      : içerisinde birden çok data
# Tuple     : Sadece okunabilir, üzerine data eklenemez
# Dictonary : JSON formatında data tutar.

# yorum satırı, bu alan derlenmeyecek

print("Hello Word")
print('Welcome to Python')
# yaptıgı işin sonucunda bana bırsey döndürüyorsa metot-fonks. pembe kutu çıkar.

print("İsmail bey'e bildirdim")

print('Welcome '  + 'to ' + 'Python')
print('Welcome '  
+ 'to ' 
+ 'Python')
print('Welcome \nto \nPython')

print("""Bilge Adam Python dersleri""")
print('''Bilge Adam''')

print("""
----------******----------
Bilge Adam Python dersleri
----------******----------
""")

# Değişken tanımlama kuralları
# 1- değişken ismi sayı ile başlayamaz. 1adim="bilge" bu olamaz. Ama sayı içerebilir. 
# 2- değişken 2 veya fazla kelimeden olaşamaz. oluşturmak istersek: 
#   benim_kullanici_adim
#   benimKullaniciAdim
# 3- değişken tanımlası yaparken kesinlikle tanımlı kelimeler kullanmayınız. mesela print değişken olarak kullanılmamalı
# 4- değişken adında türkçe veya özel (*$½§{}-?) karakter kullanılmamalı. _ hariç

# Pythonda değişken tanımlarken degiskenAdi = degiskenDegeri
# sağdaki soldakine atanır.
# veri tipi verilen değere göre otomatik atanır. Diğer diller gibi tip ataması yapılmaz.

username = "admin"
sayi = "123"
number = 123

# C#
# veriTipi degiskenAdi = degiskenDegeri; int sayi = 10;
# string username = "admin"


# javascript
# var, let, const => var username = "admin" | username = "admin"

# global alan içerisinde değişken tanımlama
firstname = "lale"
lastname = "emanet"
phone = "+901234567890"
mail = "lale.emanet@outlook.com"
#bu değişkenler globaldir. Bu sayfanın içerisinde her yerde bu değişkenler kullanılabilir.
# yukarıda tanımlanan veri tipleri string(metinsel) değerlerdir.

# {
    # bu alan global değildir.
    # firstname e burada ulaşılabilir.
    # telno = "1234"
    # telno buraya özeldir.
    # x burada kullanılamaz

    # {
        # x = "abc"
        # telno burada kullanılabılır
    # }

# }
# {} scope u belırtmek ıcın kullandık Normalde tab ile belirtiyoruz.


# elinizdeki değerin veri tipini bilmiyorsanız,
# <class 'int'>  type => içerisine verdiğiniz parametrenin(değerin) size veri tipini teslim eder.
age = 33.3
print(type(age))
print(firstname, lastname, sep="-*-", end="bilgeadam/ist")

print(firstname + " " + lastname)


print(firstname)
print(lastname)
print(mail)
print(age)

# NOT :  , ile ayrırısanız,default olarak arala bir boşluk atacaktır.
print(firstname, lastname, mail, age)

print(firstname, lastname, mail, age, sep=" - ")


# + operatörü ile birleştiriyorsanız, aralara boşluk eklemek için, haricen " " eklemeniz gerekir.
# print(firstname + " " + lastname + " - " + mail + age) hatalı kullanım (şimdilik...)


# + operatörü  => metinsel değerlerde bağlaç görevini görür, 2 veya birden fazla metni birleştirir.
# + operatörü  => sayısal değerlerde ise, toplama işelemi görür


fullname = firstname + " " + lastname
print(fullname)
print("personelin adı :", fullname)
print("personelin adı : " + fullname)


# Mantıksal veri tipi
result = True
print(result)

retVal = 10>2
print(retVal)

help(print)

# 500 kez satırı yazdırır.
print("Tatili çok seviyorum\n"*500)
