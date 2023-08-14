# BTK Akademi Python Dersi 5.1_Koşullu Durum Blokları

username = 'mhbarut66'
password = '1234'

if (username == 'mhbarut66'):

    if (password == '12345'):
        print('Hos geldiniz')
    else:
        print('parola yanlis')
else:
    print('username yanlis')
    
# BTK Akademi Python Dersi 5.2_Koşullu Durum Blokları (elif)

x = int(input('x: '))
y = int(input("y: "))

if x > y:
    print('x y den büyük ')
    
elif x == y:
    print('x y ye eşit')
else:
    print("x yden küçük")
    
    
    
num = int(input('sayı : '))

if num > 0:
    print('Sayı pozitif')
elif num < 0:
    print('Sayı negatif')
else:
    print('Sayı sıfır')
    