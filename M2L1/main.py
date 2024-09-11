#‘w’ - write - bir dosyayı yazma modunda açar fakat içindeki her şeyi siler;
#‘r’ - read - bir dosyayı salt okunur modda açar;
#‘a’ - append - dosyadan hiçbir şey çıkarmadan dosyanın sonuna veri kaydeder;
#‘rb’ - okumak için metin olmayan bir dosya açar;
#'wb’ - yazmak için metin olmayan bir dosya açar.

# Bu kod parçacığı bir metin dosyasının tamamını okumamızı sağlar
f = open('M2L1/text.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

# Daha kısa bir versiyonu:
# with open('M2L!/text.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

# Ve işte bir metin dosyasının tamamını nasıl yeniden yazabileceğimiz:
# f = open('M2L1/metinbelgesi.txt', 'w', encoding='utf-8')
# text = 'Merhaba \n'
# f.write(text)
# f.close()


# f = open('M2L1/metinbelgesi.txt', 'a', encoding='utf-8')
# text = 'Yeni bir satır \n'
# f.write(text)
# f.close()


import os
import random

resim_listesi = os.listdir('M2L1/images')
print(f"images/{random.choice(resim_listesi)}")