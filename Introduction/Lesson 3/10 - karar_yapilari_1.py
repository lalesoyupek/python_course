# Karar Yapıları
# Karşılaştırma Operatörleri

# == (eşit eşittir) => Soldaki değerin, sağdaki değere eşit olma durumu
# 1 == 1 => true  (if)
# 1 == 2 => false (else)

# -------------------------------------------------------------

# != (eşit değilse) => soldaki değerin, sağdaki değere eşit olmama durumu
# 1 != 2 => true  (if)
# 1 != 1 => false (else)

# -------------------------------------------------------------

# >  (büyüktür) soldaki değerin, sağdaki değerden büyük olma durumu
# 2 > 1  => true  (if)
# 1 > 2  => false (else)

# -------------------------------------------------------------

# <  (küçüktür) soldaki değerin, sağdaki değerden küçük olma durumu
# 1 < 2   => true  (if)
# 2 < 1   => false (else)

# -------------------------------------------------------------

# >= (büyük veya eşitse) soldaki değerin, sağdaki değerden büyük veya eşit olma durumu
# 2 >= 1  => true  (if) (büyük olma durumu)
# 1 >= 1  => true  (if) (eşit olma durumu)
# 1 >= 2  => false (else)


# -------------------------------------------------------------

# <= (küçük veya eşitse) soldaki değerin, sağdaki değerden küçük veya eşit olma durumu
# 1 <= 2 => true  (if) (küçük olma durumu)
# 1 <= 1 => true  (if) (eşit olma durumu)
# 2 <= 1 => false (else)

username = input('lütfen kullanıcı adınızı giriniz : ')
username = username.lower().replace('ı','i').replace('ç','c').replace('ğ','g').replace('ö','o').replace('ş','s').replace('ü','u').replace(' ','').replace('$','').replace('^','').replace('+','')
 
# lower()  => tamamı küçük harfe çevirir.  ÇÖpğüş+++^^^^+++$$$  => copgus
# replace() => içerisine verdiğiniz 1. parametrede yer alan datayı, 2. parametrede verdiğiniz değer ile değiştirir.

if(username == 'admin'):
    print('ana sayfaya yönlendiriliyorsunuz\nGiriş İşlemi Başarılı')
else:
    print('Kullanıcı Adınız Yanlış')

