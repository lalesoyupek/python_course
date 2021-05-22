# and sorguya katılan her bir koşulun sağlanması durumu
# or  sorguya katılan herhangi bir koşulun sağlanması durumu
# not sorguya olumsuzluk katar, değil ise


# örnek : Dışarıdan kullanıcı not girişi sağlayacak
# 0  - 30 => FF
# 31 - 50 => DD
# 51 - 70 => CC
# 71 - 84 => BB
# 85 - 100 => AA harf notunu aldınız uyarısı veriniz.

try:
    _not = int(input('lütfen notunuzu giriniz : '))
except:
    print('Geçersiz Değer Girişi')
else:
    result = "Harf Notunuz : "
    if _not >= 0 and _not <= 30:
        result += "FF"
    elif _not >= 31 and _not <= 50:
        result += "DD"
    elif _not >= 51 and _not <= 70:
        result += "CC"
    elif _not >= 71 and _not <= 84:
        result += "BB"
    elif _not >= 85 and _not <= 100:
        result += "AA"
    else:
        result = "Geçersiz Not Girişi"

    print(result) 
