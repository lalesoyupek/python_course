#
# dizinin sonuna ekler


sehirler = []
sehirler.append('Ankara')
sehirler.append('Ankara')


# .insert() -> hangi indexe eklemek istersen oraya ekliyor
sehirler.insert()

.pop
.remove
.sort
.reverse
.len

# Bir dizi üzerinde işlem yapabilmek için kullandığımız metotlardır.

# .append() => dizi içerisine yeni bir eleman eklemek için kullanırız. (javascript içinde aynı metot kullanılır)
# .append() => içerisine verdiğiniz değeri, o dizinin en son elemanı olarak ekler. (dizinin sonuna ekleme yapar)

sehirler = []
sehirler.append('Ankara')
sehirler.append('İstanbul')
sehirler.append('Edirne')
sehirler.append('İzmir')

print(sehirler)


# -------------------------------------------


# .insert() => dizi içerisinde belirli bir pozisyona eleman eklemek için kullanılır.
sehirler.insert(0, "Trabzon")
print(sehirler)
# 1. Parametre => dizinin hangi index alanına eklenecek
# 2. Parametre => diziye eklenecek olan eleman


# -------------------------------------------

# .pop() => dizi içerisinden eleman silme işlemi yapar. parametre verilirse, verilen index değerindeki elemanı, verilmezse son elemanını siler (len -1)

print(sehirler)
silinenSehir = sehirler.pop()
print(silinenSehir)
print(sehirler)

silinenSehir = sehirler.pop(2)
print(silinenSehir)
print(sehirler)


# -------------------------------------------


arabalar = ["Mercedes", "BMW", "Bugatti", "Aston Martin",
            "Tofaş", "Mercedes", "Renault", "Pegout"]


arabalar[1] ="İstanbul"

print(arabalar)
# .remove()  => dizi içerisinden eleman silmekle mükellef diğer bir metottur. pop() metodu index bazlı eleman silerken remove() object parametre alarak işlem yapar

# dizi içerisinde birden fazla aynı değere sahip eleman var ise, soldan sağa doğru bulduğu ilk elemanı siler. pop() metodu silinen elemanı geriye teslim ederken, remove() metodu void bir metot olduğundan geriye değer dönmez.


# print(arabalar[:])

# silinenAraba = arabalar.remove("Mercedes")
# print(silinenAraba)
# print(arabalar)

# a c b 
# a b c
# c b a

# .sort()    => dizi içerisindeki elemanları sıralar A'dan Z'ye - 0'dan 9'a 
print(arabalar)
arabalar.sort()
print(arabalar)
# .reverse() => dizi içerisindeki elemanları sıralama yapmadan tersine çevirir.
arabalar.reverse()
print(arabalar)

# -------------------------------------------

# .len() => dizinin uzunluğunu teslim eder.
print(len(arabalar))

# -------------------------------------------
# del  => dizinin kendisini siler

del arabalar
print(arabalar)
