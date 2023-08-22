# BTK Akademi Python Dersi 6.2_Pythonda for Döngüleri Uygulama

sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır
for sayi in sayilar:
    if (sayi%3 == 0):
        print(sayi)

# 2- Sayilar listesinde sayıların toplamı kaçtır?
toplam = 0
for i in sayilar:
    toplam += i
print(toplam)

# 3- Sayilar listesindeki tek sayıların karesini alınız
for a in sayilar:
    if (a % 2 == 1):
        print(a ** 2)

sehirler = ['kocaeli', 'istanbul', 'ankara','izmir', 'rize']
# 4- Şehirlerden hangileri en fazla 5 karakterlidir
for sehir in sehirler:
    if(len(sehir)):
        print(sehir)


#*******************************************************

urunler = [
    {'name': 'samsung S6', 'price': '3000' },
    {'name': 'samsung S7', 'price': '4000' },
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'Samsung S9', 'price': '6000'},
    {'name': 'Samsung S10', 'price': '7000'}
]

# 5- Ürünlerin fiyatları toplamı nedir
toplam2 = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print('Toplam ürün fiyatı: ', toplam2)



# 6- Ürünlerden fiyatı en fazla 5000 olan ürünler hangileridir
for i in urunler:
    fiyatlar = i['price']
    if (int(fiyatlar) <= 5000):
        print(i['name'])

