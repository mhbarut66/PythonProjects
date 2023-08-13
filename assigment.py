# BTK Akademi Python Dersleri 4.1_Atama Operatörleri

x = 5
y = 10
z = 20

x, y, z = 5, 10, 20

x += 5 # x = x + 5

values = 1,2,4

x, y, z = values
# values içindeki değerler sırasıyla x, y ve z'ye atandı.


# BTK Akademi Python Dersleri 4.2_Atama Operatörleri Uygulama

x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6


# 1- Kullanicidan aldiganiz 2 sayinin çarpima ile x,y,z toplaminin farka nedir
a = int(input('1. sayı : '))
b = int(input('2. sayı : '))

result = (a*b) - (x+y+z)

# 2- y' nin x' e kalansiz bölümünü hesaplayin1z.
result = y // x

# 3- (x, y,z) toplaminin mod 3' ü nedir ?
toplam = (x+y+z)
result = toplam % 3


# 4- y' nin x. kuvvetini hesaplayiniz.
result = y ** x

# 5- x, *y, z = numbers islemine göre z' nin küpü kaçtir ?
x, *y, z = numbers

result = z ** 3

# 6- x, *y, z = numbers islemine göre y nin degerleri toplami kaçtir?
x, *y, z = numbers
result = y[0] + y[1] + y[2]

print(result)