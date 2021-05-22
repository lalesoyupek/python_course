# Kullanıcı dışarıdan ürün adı girecek,
# domates - biber - patlıcan  => sebze reyonu
# şampuan - parfüm - deodorant => kozmetik reyonu
# cep telefonu -  televizyon - bilgisayar - kulaklık => teknoloji reyonu

# farklı bir ürün girerse, bu ürün bizde bulunmamaktadır uyarısı veriniz.


urun = input("Lütfen ürün adını giriniz : ").lower().replace(
    'ş', 's').replace('ü', 'u').replace('ı', 'i').replace(' ', '')

if urun:
    result = "Aradığınız Ürün {} Reyonundadır"
    if urun == "domates" or urun == "biber" or urun == "patlican":
        result = result.format("Sebze")
    elif urun == "sampuan" or urun == "parfum" or urun == "deodorant":
        result = result.format("Kozmetik")
    elif urun == "ceptelefonu" or urun == "televizyon" or urun == "bilgisayar" or urun == "kulaklik":
        result = result.format("Teknoloji")
    else:
        result = "Aradığınız Ürün Bizde Bulunmamaktadır."
    print(result)
else:
    print('Lütfen ürün adı giriniz')
