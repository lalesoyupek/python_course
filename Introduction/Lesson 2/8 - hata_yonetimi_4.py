try:
    sayi1 = int(input('1.sayıyı giriniz'))
    sayi2 = int(input('2.sayıyı giriniz'))
    sonuc = sayi1 / sayi2
    print('işlem sonucu: ', sonuc)

except:
    pass # hatayı pas gec. try exceptsiz kullanılmayacagı için. sonra belkı hata mesajı gırmke ıstersın dıye

except ValueError as ex:
    print(ex)
else: #kullanıcının gırdıgı sayının hatası value eror degılse
    try:
        print()
        print()
    except ZeroDivisionError as zeroer:
        print(zeroer)

############################################################################
try:
    sayi1 = int(input('lütfen 1. sayıyı giriniz : '))
    sayi2 = int(input('lütfen 2. sayıyı giriniz : '))
    # sonuc = sayi1 / sayi2
    # print('İşlem sonucu :', sonuc)

except ValueError as ex:
    print("[Error Log] ",ex)
else:
    try:
        print(sayi1/sayi2)
        print("İşlem Sonu")
    except ZeroDivisionError as error:
        print(error)