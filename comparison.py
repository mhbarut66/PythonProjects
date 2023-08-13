# BTK Akademi Python Dersleri 4.3_Karşılaştırma Operatörleri

a, b, c, d = 5, 5, 10, 4

password = '1234'
username = 'mhbarut66'


result = a == b # true
result = a != b # false

result = a == c # false

result = ('mhbarut06' == username) # false

result = (a < c) # true
result = (a <= b) # true


# BTK Akademi Python Dersleri 4.4_Karşılaştırma Operatörleri Uygulama

# 1- Girilen 2 sayidan hangisi büyüktür ?
a = int(input('a = '))
b = int(input('b = '))

result = a > b
print(f'a: {a}, b: {b} den büyüktür: {result}')


# 2- Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayin1z
# Eger ortalama 50 ve üstündeyse geçti degilse kaldi yazdirin.
vize1 = float(input('1. vize : '))
vize2 = float(input('2. vize : '))
final = float(input('final : '))

ort = (((vize1 + vize2) / 2 )* 0.6) + (final * 0.4)
print(f'Ortalamanız {ort}, Geçme durumu: {ort >= 50}')

# 3- Girilen bir sayinin tek mi çift mi oldugunu yazdirin.
sayi = int(input('sayı : '))

tekcift = (sayi % 2 == 0)

print(f'Çift olma durumu = {tekcift}')

# 4- Girilen bir sayinin negatif pozitif durumunu yazdirin.
sayi2 = int(input('sayı : '))
pozitifmi = (sayi2 > 0)

print(f'pozitif olma durumu : {pozitifmi}')

# 5- Parola ve email bilgisini isteyip dogrulugunu kontrol ediniz.
# (email: email@sadikturan.com parola:abc123)

email, parola = 'email@sadikturan.com', 'abc123'

girilenmail = input('email: ')
girilensifre = input('parola: ')

isemail = email == girilenmail
issifre = parola == girilensifre

print(f'Email bilgisi dogrumu: {isemail} ve Parola dogru mu: {issifre}')



