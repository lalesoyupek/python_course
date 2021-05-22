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