# Örnek : Dışarıdan girilen kelimenin uzunluğu, 8 karaktere eşit veya uzunsa, parola onaylandı, kısa ise, daha uzun bir şifre seçiniz uyarısı verdiriniz
# len() => içerisine verdiğiniz değerin size uzunluğunu teslim eder.

try:
    password = "bubenimyenişifrem"
    # password = input('lütfen şifrenizi giriniz : ')
    if(len(password) < 8):
        print('şifreniz yetersiz uzunlukta')
    else:
        print('tebrikler şifreniz onaylandı')
except:
    print('lütfen bilgileri kontrol ediniz.')
