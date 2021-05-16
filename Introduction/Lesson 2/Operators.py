# Aritmetik Operatorler

# + - * / % //

sayi1 = 100
sayi2 = 20

toplama = sayi1 + sayi2
print(toplama)

# Kullanıcıdan değer almak istiyorsak,
# input metodu

number1 = input('Lütfen 1.sayıyı giriniz: ')
print(number1)
type(number1)  # Dışardan aldığın değer her zaman string gelecektir.

mod = sayi1 % sayi2
print("Mod işlemi sonucu: ", mod)

# Convert işlemi veri tipleri arasında birbirine çevirme işlemidir.

# str -> int X
# int -> str √

# cmd + k + c       => yorum satırı yapar
# cmd + k + u       => yorum satırı kaldırır
# opt + shift + f   => kodları düzenler
# opt + z           => wordwrap ekranın sonundaki satırı bir alt satıra alır

# int() : tam sayı veri tipine çevirir
# str() : stringe veri tipine çevirir
# float() : ondalıklı veri tipine çevirir
# chr() : verdiğiniz sayısal değerin metinsel değerini teslim eder
# ord() : verdiğiniz karakter değerinin ascii yani sayısal değerini teslim eder

# soru 1
sayi3 = input("sayi1:")
sayi4 = input("sayi2:")
print((int(sayi3)+int(sayi4))
      %
      (int(sayi3)-int(sayi4))
      )

# soru 2
sayi5 = input("sayıyı giriniz:")
print((int(sayi5) - 10 + 20) % 2)

# soru 3
sayi6 = int(input("sayı 1 giriniz:"))
sayi7 = int(input("sayı 2 giriniz:"))
result = (sayi6**2 + sayi7**2) + (sayi6**2 - sayi7**2)
print(result)

# soru 4
vize = int(input("vize giriniz:"))
final = int(input("final giriniz:"))
nott = (vize*0.3 + final*0.7)
print(nott)

# soru 5 
adi = input("adınızı giriniz:")
soyadi = input("soyadınızı giriniz:")
print(adi+'.'+soyadi+'@hotmail.com')
print(adi, soyadi, sep='.', end='@hotmail.com\n' )

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

