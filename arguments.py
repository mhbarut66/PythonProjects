# BTK Akademi Python Dersi 7.3_Fonksiyon Parametreleri

def changeName(n):
    n = 'Halit'

name = 'Gazi'

changeName(name)
# Değişmedi

def change(n):
    n[0] = 'İstanbul'


sehirler = ['Ankara', 'İstanbul']

change(sehirler)
# Değişti


def add(*params):
    return sum((params))


print(add(10,20))
print(add(10,20,40,12))
print(add())


def displayUser(**args):
    for key, value in args.items():
        print(f'Key: {key}, Value: {value}')


displayUser(name = "Halit", age = 18, city = 'Adana')
displayUser(name = "Gazi", age = 48, city = 'Yozgat')
displayUser(name = "Beyza", age = 43, city = 'Ankara')

# tek * (yıldız) tuple listesi ifade ederken çift yıldız (**) bir dictionary ifade eder

def myfunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunc(10,20,30,40,32, key1 = 'value 1', key2 = 'value 2')