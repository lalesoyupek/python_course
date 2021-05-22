# Kullanıcı dışarıdan kullanıcı adını ve şifresini girecek.
# 1) kullanıcı adı doğru ise, içeride şifreyi kontrol edecek, şifre doğru ise, giriş yaptınız, yanlış ise, kullanıcı adınız doğru fakat şifreniz yanlış uyarısı versin
# 2) kullanıcı adını yanlış girerse, kullanıcı adınız yanlış şifreyi kontrol etmedim uyarısı verdiriniz..

# username = admin, password = 123


# try:
#     username = input('lütfen kullanıcı adınızı giriniz : ').lower().replace('ş','s').replace(' ','')
#     if username == 'admin':
#         password = input('lütfen şifrenizi giriniz : ')
#         if(password == "123"):
#             print('tebrikler giriş yaptınız')
#         else:
#             print('kullanıcı adınız doğru fakat şifreniz yanlış')
#     else:
#         print('kullanıcı adınız yanlış şifreyi kontrol etmedim.')

# except:
#     print('işlem hatası')


# Mantıksal operatörler

# and : sorguya katılan her bir koşulun istisnasız sağlanması durumu
# or  : sorguya katılan koşullardan birtanesinin sağlanması durumu
# not : sorguya olumsuzluk katar, değilse
username = input('lütfen kullanıcı adınızı giriniz : ').lower().replace('ş','s').replace(' ','')
password = input('lütfen şifrenizi giriniz : ')

if(username == "admin" and password == "123"):
    print('tebrikler giriş yaptınız')
else:
    print('kullanıcı bilgileriniz hatalı, lütfen kontrol ediniz.')