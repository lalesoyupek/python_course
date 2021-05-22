try:
    pass
except:
    pass
finally: #isteğe bağlıdır.
    pass


try:
    # DB connection open
    # C(reate)-R(ead)-U(pdate)-D(elete) - crud işlemlerinden birisini yaparız.
    # DB connection close
    sayi = int(input('sayı giriniz'))
    print('teşekkürler..')
except:
    # DB connetion close
    pass
finally: 
    # DB connetion close -> try ve excepte tekrar tekrar yazmamak için sadece buraya yazıyoruz. hata oldu olmadı vs bittikten sonra connectıonı kapatır.

################################################################
try:
    # DbConnection => database'e bağlanma işlemi
    # Connection Open()
    # C(reate)-R(ead)-U(pdate)-D(elete) 
    sayi  = int(input('lütfen sayı giriniz : '))
    print('teşekkürler..')

except: 
    print("Hata meydana geldi")
finally:
    # Connection Close()
    print("Her zaman ben çalışırım, istisnasız...")