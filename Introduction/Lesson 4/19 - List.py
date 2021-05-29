# Birden fazla elem


print(sehirler.index("Adana"))-> indexini döner

# birden fazla elemanla çalışacaksak, tekk tek değişken tanımlama yerine dizi kullanmalıyız.
# dizi tanımla şekli

sehirler = ["ankara - 0", "edirne - 1",
            "istanbul - 2", "bursa - 3", "Malatya", "Trabzon", "Adana"]

# dizinin eleman sayısı     => 4
# dizinin max indexn değeri => 3 (max index = eleman sayısı -1)
# dizi üzerinde işlem yaparken kesinlikle içerisinde yer alan eleman baz alınmaz. Index değeri üzerinden işlem yapılır.

# 1 2 3 4 5 6
# 0 1 2 3 4 5

if len(sehirler) > 0:
    print(sehirler[len(sehirler) - 1])
else:
    print('dizi içerisinde eleman yer almamaktadır.')

print(sehirler)
print(sehirler[:])
# index değeri 3'e kadar olan elemanları yazıdr (3 dahil değil)
print(sehirler[:3])
# 1. index değerinden başlayarak (1 dahil), 3. index'e kadar olan elemanları listeler (3 dahil değildir)
print(sehirler[1:3])


# => adana şehirler dizisi içerisinde var ise true, yok ise false teslim eder
print('Adana' in sehirler)

if 'Adana' in sehirler:
    print("Adana şehri şehirler içerisinde vardır")
else:
    print("Adana şehirler dizisi içerisinde yer almamaktadır.")

print(sehirler.index('Adana'))


# Ternary If Nedir ?

# MessageBox.Show(db.SaveChanges() > 0 ? "Kayıt Ekleme İşlemi Başarılı" : "Kayıt Ekleme İşlemi Başarısız")
# MessageBox.Show($"Kayıt Ekleme İşlemi Başarı{(db.SaveChanges() > 0 ? "lı":"sız")}")
sehir = input("Lütfen şehir adı giriniz : ")

result = f'Parameterede gönderdiğiniz "{sehir}" şehri dizi içerisinde yer alma{("" if sehir in sehirler else "ma")}ktadır'
print(result)


myList1 = ["sehirler"]
myList2 = ["arabalar"]
myList3 = ["renkler"]


print(myList1)
print(myList2)
print(myList3)


retVal = list(zip(myList1, myList2, myList3))
print(retVal)
