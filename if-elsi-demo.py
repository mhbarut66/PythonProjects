# BTK Akademi Python Dersi 5.3_If-Else Uygulama

# 1- Kullanicidan isim, yas ve egitim bilgilerini isteyip ehliyet alabilme
# durumunu kontrol ediniz. Ehliyet alma kosulu en az 18 ve egitim durumu lise ya da üniversite olmalıdır.

import datetime

isim = input('isminiz : ')
yas = int(input('yaşınız : '))
egitim = input('eğitim : ')

if (yas >= 18):
    if (egitim == 'lise' or egitim == 'üniversite'):
        print('ehliyet alabilirsiniz')
    else:
        print('ehliyet alamazsınız eğitim durumunuz yetersiz.')
else:
    print('ehliyet alamazsınız yaşınız tutmuyor.')


# 2- Bir ögrencinin 2 yazili bir sözlü notunu alip hesaplanan ortalamaya gore not araligina karsilik gelen not bilgisini yazdiriniz.

# 0-24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5

yazili1 = float(input("1. yazılı: "))
yazili2 = float(input("2. yazılı: "))
sozlu = float(input("Sözlü: "))

ortalama = (yazili1 + yazili2 + sozlu)/3

if (ortalama >= 0) and (ortalama < 25):
    print(f'ortalamnız {ortalama}, notunuz 0')
elif  (ortalama >= 25) and (ortalama < 45):
    print(f'ortalamnız {ortalama}, notunuz 1')
elif  (ortalama >= 45) and (ortalama < 55):
    print(f'ortalamnız {ortalama}, notunuz 2')
elif  (ortalama >= 55) and (ortalama < 69):
    print(f'ortalamnız {ortalama}, notunuz 3')
elif  (ortalama >= 70) and (ortalama < 85):
    print(f'ortalamnız {ortalama}, notunuz 4')
elif  (ortalama >= 85) and (ortalama <= 100):
    print(f'ortalamnız {ortalama}, notunuz 5')
else:
    print('yanlış bilgi girdiniz.')
    
# 3- Trafige çikis tarihi (05/08/2022) alinan bir aracin servis zamanini asagidaki bilgilere
# gore hesaplayiniz.
# 1. Bakim => 1. yil
# 2. Bakim => 2. yil
# 3. Bakim => 3. yil
# Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
# tarih alırsanız datetime modülünü kullanmanız gerekiyor.

days = int(input('Aracınız kaç gündür trafikte: '))

if days <= 365:
    print('1. servis aralığı')
elif days > 365 and days <= 365*2:
    print('2. servis aralığı')
elif days > 365*2 and days <= 365*3:
    print('3. servis aralığı')
else:
    print('Hatalı süre.')

# datetime ile yapılan versiyonu

tarih = input('Aracınız hangi tarihte trafiğe çıktı (yyyy/aa/gg): ')
tarih = tarih.split('/')

trafigeCikis = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))

simdi = datetime.datetime.now()

fark = simdi - trafigeCikis

days = fark.days

if days <= 365:
    print('1. servis aralığı')
elif days > 365 and days <= 365*2:
    print('2. servis aralığı')
elif days > 365*2 and days <= 365*3:
    print('3. servis aralığı')
else:
    print('Hatalı süre.')
