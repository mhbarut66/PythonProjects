# BTK Akademi Python Dersleri 3.18_Uygulama Pythonda Dictionary

'''

ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yilmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    },
}

1- Bilgileri verilen ögrencileri kullanicidan aldiginiz bilgilerle
dictionary içinde saklay1n1z.

2- Ögrenci numarasin1 kullanicidan alip ilgili ögrenci bilgisini gösterin.

'''

ogrenciler = {}

number = input("Öğrenci No: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyadı: ")
phone = input("Öğrenci Telefon: ")

ogrenciler[number] = {
    'ad' : name,
    'soyad' : surname,
    'telefon' : phone,

}


# aşağıdaki update metodu ile üstte yaptığımız işlemin aynısını yapabiliriz.
ogrenciler.update({
    number: {
    'ad': name,
    'soyad': surname,
    'telefon' :phone
    }
})

# öğrenci 2
number = input("Öğrenci No: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyadı: ")
phone = input("Öğrenci Telefon: ")

ogrenciler.update({
    number: {
    'ad': name,
    'soyad': surname,
    'telefon' :phone
    }
})

# öğrenci 3
number = input("Öğrenci No: ")
name = input("Öğrenci Adı: ")
surname = input("Öğrenci Soyadı: ")
phone = input("Öğrenci Telefon: ")

ogrenciler.update({
    number: {
    'ad': name,
    'soyad': surname,
    'telefon' :phone
    }
})


print(ogrenciler)

ogrno = input('Öğrenci No: ')
ogrenci = ogrenciler

print(ogrenci)


