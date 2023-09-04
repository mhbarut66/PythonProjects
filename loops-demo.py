# BTK Akademi Python Dersleri 6.8_Uygulama - Sayı Tahmin Uygulaması

import random

'''
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
    ** 'random modülü' için 'python random' şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''

sayi = random.randint(1,10)



sayac = 0
can = int(input('Kaç hak kullanmak istersiniz: '))
hak = can


while hak > 0:
    hak -= 1
    sayac += 1

    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler Doğru, {sayac} denemede bildiniz. Puanınız : {100 - (100/can) * (sayac-1)}')
    else:
        if sayi>tahmin:
            print("Yukarı")
        else:
            print('Aşağı')

    if hak == 0:
        print(f'Hakkınız bitti, Sayı : {sayi}')