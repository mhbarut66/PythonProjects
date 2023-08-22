# BTK Akademi Python Dersi 6.3_Pythonda While Döngüleri

x = 1

while x <= 100:
    if (x % 2 == 0):
        print(x)
    x += 1
    

print('bitti.')

name = ''

while not name.strip():
    name = input('isminizi giriniz: ')

print('Merhaba ', name)

