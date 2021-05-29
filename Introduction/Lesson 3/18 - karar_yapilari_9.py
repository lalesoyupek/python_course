# Kullanıcı dışarıdan sipariş alınacak kitap adedi girilecek,
# birim fiyat 5 tl
# sipariş sayısı : 0 veya altı ise uyarı verdiriniz
# sipariş sayısı : 1  ile 20(dahil)   ise  %5  indirim uygulayınız
# sipariş sayısı : 21 ile 50(dahil)   ise, %10 indirim uygulayınız
# sipariş sayısı : 51 ile 80(dahil)   ise, %15 indirim uygulayınız
# sipariş sayısı : 81 ile 100(dahil)  ise, %20 indirim uygulayınız
# sipariş sayısı : 100'den büyük      ise, %25 indirim uygulayınız


# Kullanıcıya işlem sonunda, toplam ödemesi gereken tutar, verdiği sipariş adedi yapılan indirim oranı vs. bir mesaj verilecek...



# Verilen Sipariş Adedi         :
# Adet Birim Fiyatı             :
# Toplam Tutar                   :
# Yapılan İndirim Oranı         :
# Toplam Ödemeniz Gereken Tutar : 



siparis_adedi   = int(input("Sipariş Adedini giriniz: "))
birim_fiyat     = 5
indirim_orani   = 0

try:
    if siparis_adedi <= 0:
        print("Sipariş adedi 0 veya daha az girilmiştir.")
    elif siparis_adedi < 20:
        indirim_orani = 0.05
    elif siparis_adedi <= 50:
        indirim_orani = 0.1
    elif siparis_adedi <= 80:
        indirim_orani = 0.15 
    elif siparis_adedi <= 100:
        indirim_orani = 0.2
    elif siparis_adedi > 100:
        indirim_orani = 0.25
    
    print("Girilen Sipariş Adedi: ", siparis_adedi)
    print("Toplam tutar:" , siparis_adedi * birim_fiyat)
    print("İndirim Oranı Yüzde: ", indirim_orani*100)  
    print("Yapılan indirim sonrası ödenecek tutar: " , siparis_adedi * birim_fiyat * (1 - indirim_orani))  
except Exception as ex:
    print(ex)


import os ## operation system kütüphanesi
os.system('clear') # ekrandaki sistem yazılarını siler



################################################

import os
os.system('cls')  # mac kullanıcıları os.system('clear') yazmaları yeterlidir

print("""
********************************************* Kitap Otomasyonu Sistemine Hoşgeldiniz *******************************************
*                                                                                                                              *
*                                                                                                                              *
*                                                                                                                              *
*                                                                                                                              *
*                                                  Bilge Adam Python Dersleri                                                  *
*                                                                                                                              *
*                                                                                                                              *
*                                                                                                                              *
*                                                                                                                              *
******************************************************************************************************************************** """)


try:
    adet = int(input('lütfen sipariş adedi giriniz : '))
    if adet > 0:
        birim_fiyat = 5
        toplam = 0
        indirim = ""
        result = """
Verilen Sipariş Adedi         : {0}
Adet Birim Fiyatı             : {1}$
Tolam Tutar                   : {2}$
Yapılan İndirim Oranı         : %{3}
Toplam Ödemeniz Gereken Tutar : {4}$ 
        """
        if adet <= 10:
            indirim = "0"
            toplam = birim_fiyat * adet
        elif adet <= 20:
            indirim = "5"
            toplam = (birim_fiyat * adet) * 0.95
        elif adet <= 50:
            indirim = "10"
            toplam = (birim_fiyat * adet) * 0.90
        elif adet <= 80:
            indirim = "15"
            toplam = (birim_fiyat * adet) * 0.85
        elif adet <= 100:
            indirim = "20"
            toplam = (birim_fiyat * adet) * 0.80
        else:
            indirim = "25"
            toplam = (birim_fiyat * adet) * 0.75
        result = result.format(
            adet, birim_fiyat, (birim_fiyat * adet), indirim, toplam)
    else:
        result = 'Minimum Sipariş Adedi 1 Olmalıdır.'
    print(result)
except Exception as err: 
    os.system('cls') 
    print("\033[1;31;40m", err) 
