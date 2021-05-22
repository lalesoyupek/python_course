# kullanıcın dışarıdan girdiğin  sayının tek veya çift olma durumunu kontrol etme, sayi tek ise, sayı tektir uyarısı çift ise, sayı çifttir uyarısı veriniz.

try:
    gelen_veri = input('lütfen sayıyı giriniz : ') 
    sayi = int(gelen_veri)
    
    if sayi % 2 == 0:
        print('girilen sayı çift sayıdır')
    else:
        print('girilen sayı tek sayıdır')
except Exception as ex:
    print(ex)
