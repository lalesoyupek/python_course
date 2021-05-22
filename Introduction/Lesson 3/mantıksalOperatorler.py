# and
# or
# not

# try:
#     nott = float(input("notunuzu giriniz: "))              
# except Exception as ex:
#     print(ex)
# else: # try true olursa
#     if nott >= 0 and nott <= 30:
#         print("FF")
#     elif nott > 30 and nott <= 50:
#         print("DD") 
#     elif nott > 50 and nott <= 70:
#         print("CC") 
#     elif nott > 70 and nott <= 84:
#         print("BB")
#     elif nott > 84 and nott <= 100:
#         print("AA")  
#     else:
#         print("Böyle bir not yoktur") 

#--------------------------------------------------

# try:
#     nott = float(input("notunuzu giriniz: "))              
# except Exception as ex:
#     print(ex)
# else: # try true olursa
#     result = "Harf notunuz: "
#     if nott >= 0 and nott <= 30:
#         result += "FF"
#     elif nott > 30 and nott <= 50:
#         result += "DD" 
#     elif nott > 50 and nott <= 70:
#         result += "CC"
#     elif nott > 70 and nott <= 84:
#         result += "BB"
#     elif nott > 84 and nott <= 100:
#         result += "AA"
#     else:
#         result = "Böyle bir not yoktur"
    
#     print(result)
#--------------------------------------------------

# try:
#     nott = float(input("notunuzu giriniz: "))              
# except Exception as ex:
#     print(ex)
# else: # try true olursa
#     result = "Harf notunuz: {0}"
#     if nott >= 0 and nott <= 100:
#         result = result.format("FF")
#     elif nott > 30 and nott <= 50:
#         result += "DD" 
#     elif nott > 50 and nott <= 70:
#         result += "CC"
#     elif nott > 70 and nott <= 84:
#         result += "BB"
#     elif nott > 84 and nott <= 100:
#         result += "AA"
#     else:
#         result = "Böyle bir not yoktur"
    
#     print(result)


#--------------------------------------------------
try:
    urunad = input("ürün adını giriniz: ").lower().replace('ş','s').replace('ı','i').replace('ü','u').replace(' ','')
except Exception as ex:
    print(ex)
else:
    result = "{0} reyonu"
    if urunad == "domates" or urunad == "biber" or urunad == "patlican":
        result = result.format("sebze")
    elif urunad == "sampuan" or urunad == "parfum" or urunad == "deodorant":
        result = result.format("kozmetik")
    elif urunad == "ceptelefonu" or urunad == "televizyon" or urunad == "kulaklık":
        result = result.format("teknoloji")
    else:
        result = "Bu ürün bizde bulunmamaktadır."
    
    print(result)


# uipath
# regexr.com
# opencv kutuphanesı gorsel takıp