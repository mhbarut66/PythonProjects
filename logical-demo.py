# BTK Akademi Python Dersi 4.6_Mantıksal Operatörler Uygulama

# 1- Girilen bir sayinin 0-100 arasinda olup olmadigin1 kontrol ediniz.
a = int(input('Sayı girin: '))
result = (a > 0) and (a <= 100)

# 2- Girilen bir sayinin pozitif çift sayi olup olmadigin1 kontrol ediniz.
result = (a > 0) and (a % 2 == 0)

# 3- Email ve parola bilgileri ile giris kontrolü yapiniz.

email = 'email@sadikturan'
password = 'abc123'
girilenEmail = input('email: ')
girilenPassword = input('password: ')
result = (girilenEmail == email) and (girilenPassword == password)

# 4- Girilen 3 sayiy1 büyüklük olarak karsilastiriniz.

a = int(input('a:'))
b = int(input('b: '))
c = int(input( 'c: '))
result = (a > b) and (a > c)
print(f'a en büyük sayidir : {result}')

result = (b > a) and (b > c)
print(f'b en büyük sayidir : {result}')

result = (c > a) and (c > b)
print(f'b en büyük sayidir : {result}')

# 5- Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayin1z
#   Eger ortalama 50 ve üstündeyse geçti degilse kaldi yazdirin.
#   a-) Ortamalama 50 olsa bile final notu en az 50 olmalidir.
#   b-) Finalden 70 alindiginda ortalamanin önemi olmasin.

vizel = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final : '))

ortalama = ((vizel+vize2)/2)*0.6 + (final * 0.4)
# result = (ortalama>=50) and (final>=50)
result = (ortalama >= 50) or (final >= 70) 

# 6- Kisinin ad, kilo ve boy bilgilerini alip kilo indekslerini hesaplay1n1z.
#   Formül: (Kilo / boy uzunlugunun


name = input('adiniz: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)

zayif = (index >= 0) and (index<=18.4)
normal = (index>18.4) and (index<=24.9)
kilolu = (index>24.9) and (index<=29.9)
obez = (index>=29.9) and (index<=34.9)

print(f'{name} kilo indeksin: {index} ve kilo degerlendirmen zayif: {zayif}')
print(f'{name} kilo indeksin: {index} ve kilo degerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo degerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo degerlendirmen obez: {obez}')