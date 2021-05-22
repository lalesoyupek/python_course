# örnek : Dışarıdan kullanıcı not girişi sağlayacak
# 0  - 30 => FF
# 31 - 50 => DD
# 51 - 70 => CC
# 71 - 84 => BB
# 85 - 100 => AA harf notunu aldınız uyarısı veriniz.


try:
    _not = int(input('Lütfen notunuzu giriniz : '))
except:
    print('Geçersiz Değer Girişi')
else:
    result = "Harf Notunuz : {0}"
    if _not >= 0 and _not <= 100:
        if _not <= 30:
            result = result.format("FF")
        elif _not <= 50:
            result = result.format("DD")
        elif _not <= 70:
            result = result.format("CC")
        elif _not <= 84:
            result = result.format("BB")
        else:
            result = result.format("AA")
        print(result)
    else:
        print('Lütfen 0 ile 100 aralığında bir değer giriniz')
