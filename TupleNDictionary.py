# BTK Akademi Python Dersi 3.16_Pythonda Tuple

list = [1,2,3]

tuple = (1, 'iki', 3, 4, 4, 4)

# tuple daki elemanlar değiştirilemiyor.
# tuple[0] = 9 olmaz.
# ama list[0] = 9 olur.


# tuple daki komutlar

tuple.count(4)
tuple.index('iki')

# BTK Akademi Python Dersi 3.17_Pythonda Dictionary

# key - value => kısaca sözlük.

sehirler = ['Yozgat', 'Ankara']
plakalar = [66, 6]

plakalar[sehirler.index('Yozgat')] # bunun yerine dictionary kullanabiliriz

dictionary = { 'Yozgat' : 66, 'Ankara' : 6}

dictionary['İstanbul'] = 34

# print(dictionary)

users = {
    'halitbarut' : {
        'age' : 18,
        'computer' : 'fujitsu',
        'roles' : 'admin'
    },
    'gazibarut' : {
        'age' : 48,
        'computer' : 'dell',
        'roles' : 'user'
    }
}







