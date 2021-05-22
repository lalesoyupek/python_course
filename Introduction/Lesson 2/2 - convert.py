# Convert işlemi veri tipleri arasında birbirine çevirme işlemidir.

# str -> int X
# int -> str √


# int()    : tam sayı veri tipine çevirir
# str()    : string (metinsel) veri tipine çevirir
# float()  : ondalikli sayi tipine çevirir
# chr()    : verdiğiniz sayısal değerin, metinsel değerini teslim eder
# ord()    : verdiğiniz karakter değerinin, ascii(sayısal) değerini teslim eder.

sayi1 = "123"  # metinsel değer
sayi2 = "123"

print(sayi1 + sayi2)  # => 123123
# + operatörü, metinsel değerlerde kullanıyorsanız bağlaç(birleştirme) görevi görür.


s1 = int(sayi1)
s2 = int(sayi2)
# print("İşlem Sonucu : " + s1 + s2) # Hatalı senaryo => veri tipleri uyuşmadığından, hata verecektir. metin ile sayıyı toplayamaz


print("İşlem Sonucu :" , s1 + s2) 



print("İşlem Sonucu : " + str(s1 + s2)) 
# C# => Console.WritLine("İşlem Sonucu : " + s1 + s2) => İşlem Sonucu : 123123

toplam = float(sayi1) + float(sayi2)
print(toplam)


print(chr(65), ord('A'))  # => A 65
print(chr(90), ord('Z'))  # => Z 90
print(chr(97), ord('a'))  # => a 97
print(chr(122), ord('z')) # => z 122

print(ord('0')) # 48
print(ord('9')) # 57     => kullanıcının bastığı tuş değerinin ascii değeri >= 48 and <= 57 (48 ve 57 dahil) bu değer aralığında ise, işlem yap
 
