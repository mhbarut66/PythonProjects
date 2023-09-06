# BTK Akademi Python Dersi 7.2 Fonksiyon Kullanımı

def sayHello(name = 'user'):
    return 'Hello ' + name

message = sayHello("Halit")

print(message)

def total(num1, num2):
    return num1 + num2

print(total(2,5))


def yasHesapla (dogumYili):
    return 2023 - dogumYili

ageHalit = yasHesapla(2005)
ageGazi = yasHesapla(1975)

print(ageGazi, " " , ageHalit)

def emekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum yili ve yas
    OUTPUT: Kalan yil bilgisi
    '''


    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'{isim} emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print(f"{isim} Emeklilik yaşınız gelmiş.")

emekliligeKacYilKaldi(2005, "Halit")

print(help(emekliligeKacYilKaldi))

list = [1,2,3]

print(help(list.append))


