try:
    sayi = int(input('Lütfen sayısal bir değer giriniz : '))
    print('Güzel sayi :)')
    sayi = sayi / 0
    print('işlem sonu') 

except ValueError as ex:
    print("[Error LOG] :",ex)

except ZeroDivisionError as ex:
    print("[Error LOG] :",ex)

except Exception as hataadi:    # Exception en genel hata yakalama tipidir, en son satırda yer almalıdır.
    print("Uygulamada Bir Hata Meydana Geldi, Lütfen Tekrar Deneyiniz.") # Kullanıcı için oluşturduk
    print("[Error LOG] :", hataadi)  # Loglama için oluşturduk, kullanıcıya sistem hata mesajları gösterilmez.
