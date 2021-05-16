# yorum satırı, bu alan derlenmeyecek
# 

# alt + z -> wordwarp -> satırı alta kaydır.

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
# 2- değişne 2 veya fazla kelimeden olaşamaz. oluşturmak istersek: 
#   benim_kullanici_adim
#   benimKullaniciAdim
# 3- değişken tanımlası yaparken kesinlikle tanımlı kelimeler kullanmayınız. mesela print değişken olarak kullanılmamalı
# 4- değişken adında türkçe veya özel (*$½§{}-?) karakter kullanılmamalı. _ hariç

# Pythonda değişken tanımlarken isim = değeri
# sağdaki soldakine atanır.
# veri tipi verilen değere göre otomatik atanır. Diğer diller gibi tip ataması yapılmaz.


# global alan içerisinde değişken tanımlama
firstname = "lale"
lastname = "emanet"
#bu değişkenler globaldir. Bu sayfanın içerisinde her yerde bu değişkenler kullanılabilir.

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

age = 33.3
print(type(age))
print(firstname, lastname, sep="-*-", end="bilgeadam/ist")

print(firstname + " " + lastname)

# Mantıksal veri tipi
result = True
print(result)

retVal = 10>2
print(retVal)

# /n -> alt satıra geçirir

help(print)

# 500 kez satırı yazdırır.
print("Tatili çok seviyorum\n"*500)
