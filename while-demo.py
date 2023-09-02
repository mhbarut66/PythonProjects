# BTK Akademi Python Dersi 6.4_Pythonda While Döngüleri Uygulama

sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayılar listesini while ile ekrana yazdırın.
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları yazdırın.

baslangic = int(input('başlangıç: '))
bitis = int(input('bitiş: '))

i = baslangic
while i < bitis:
    i += 1
    if i % 2 == 1:
        print(i)

# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

a = 100
while a > 0:
    print(a)
    a -= 1


# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
numbers = []

i = 0
while i < 5:
    sayi = int(input('Sayı: '))
    numbers.append(sayi)
    i += 1

numbers.sort()
print(numbers)

# 5- Kullanıcıdan alacağınız ürün bilgisini ürünler listesi içinde saklayınız.
# ** ürün sayısını kullanıcıya sorun.
# ** dictionary listesi yapısı (name, price) şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []

adet = int(input('Kaç ürün ekleyeceksiniz? : '))

i = 0

while i < adet:
    name = input('İsim: ')
    price = input('Fiyat: ')
    urunler.append({
        'name' : name,
        'price' : price
    })
    i += 1

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')