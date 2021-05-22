# kullanıcı dışarıdan not değerini girecek ve girilen not 0'dan küçükse, 0'dan küçük not giremezsiniz uyarısı, 100'den büyükse 100'den büyük not girişi yapamazsınız uyarısı, girilen no 0'a veya 100'eşit ve küçükse, kullanıcıya girdiği notu gösteriniz.


try:
    _not = int(input('Lütfen notunuzu giriniz : '))   # 0 ve > üstü bir sayı girerse?
    if _not < 0:
        print("0 'dan küçük not girişi yapamazsınız") 
    elif _not > 100:
        print("100 'den büyük not girişi yapamazsınız") 
    else:
        print("Tebrikler notunuz :", _not)

except:
    print('Hata meydana geldi değerlerinizi kontrol ediniz..')

