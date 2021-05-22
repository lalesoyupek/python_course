# Ornek 1
# username = input('kullanıcı adı:')
# username = username.lower().replace('ı','i').replace('ç','c')
# print(username)
# if(username == 'admin'):
#     print('ana sayfaya giriş başarılı')
# else:
#     print('kullanıcı adınız yanlış')


# Ornek 2
# try:
#     nott = int(input('notu giriniz:'))
#     if(nott < 0):
#         print('0 dan küçük not giremezsiniz!')
#     else:
#         if(nott > 100):
#             print('100den büyük sayı giremezsiniz.')
#         else:
#             print(nott)
# except:
#     print('girdiğiniz bir sayı değildir.')


# # elif = else if
# try:
#     nott = int(input('notu giriniz:'))
#     if(nott < 0):
#         print('0 dan küçük not giremezsiniz!')
#     elif(nott > 100):
#         print('100den büyük sayı giremezsiniz.')
#     else:
#         print(nott)
# except:
#     print('girdiğiniz bir sayı değildir.')


# ornek 3
# try:
#     sayi3 = int(input('sayı giriniz:'))
#     if sayi3 % 2 == 0:
#         print("çift sayı girdiniz")
#     else:
#         print("Tek sayı girdiniz.")
# except Exception as ex:
#     print(ex)

# Ornek 4
# try:
#     password = input('password:')
#     if len(password) >= 8:
#         print("password onaylandı")
#     else:
#         print("Daha uzun bir şifre giriniz")

# except Exception as ex:
#     print(ex)

# Ornek 5
# try:
#     user = input("kullanıcı adını giriniz: ").lower().replace('ş','s')
#     if user == 'lale':
#         passw = input("şifre giriniz: ")
#         if passw == '123':
#             print("giriş yaptınız.")
#         else:
#             print("Kullanıcı adınız doğru şifreniz yanlış")
#     else:
#         print("Kullanıcı adınız yanlış. Şifreyi kontrol etmedim.")
# except Exception as ex:
#     print(ex)

