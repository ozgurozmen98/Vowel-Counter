#MISSION2

harfler = "aeıioöuü" #harfleri tanımla

input = input("Bir kelime giriniz: ") #girdi yap

input = input.lower() #Girdiyi küçük harf yapıyorum

harf_sayisi = input.count("a") + input.count("e") + input.count("ı") + input.count("i") + input.count("o") + input.count("ö") + input.count("ö") + input.count("u") + input.count("ü")
#harfleri toplatıyorum

print(f" Giridğin metinde bulunan sesli harf sayısı: {harf_sayisi}") #"f ile sonuç çıktısı ayırıp metin haline getiriyorum