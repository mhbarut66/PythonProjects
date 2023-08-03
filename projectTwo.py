# 1- " Hello World " karakter dizisinin baş ve sondaki boşlukları siliniz.

firstAnswer = " Hello World "
print(firstAnswer.strip())

# 2- "www.btkakademi.gov" içindeki btkakademi dışındaki her karakteri silin

print('www.btkakademi.gov'.strip("w.gov"))

# 3- "HaLiT BAruT" tüm karakterlerini küçük harf yapın.

print("HaLiT BAruT".lower())


# 4- "HaLiT BAruT" içinde kaç tane t harfi var?

print("halit barut".count("a"))

# 5- "www.btkakademi.gov" 'www' ile başlayıp 'gov' ile bitiyor mu?

print('www.btkakademi.gov'.startswith('www'))
print('www.btkakademi.gov'.endswith('gov'))

# 6- "www.btkakademi.gov" içerisinde '.com' var mı?

print("www.btkakademi.gov".find(".com"))

# 7- "Halit" içerisindeki tüm harfler alfabetik mi?

print("Halit".isalpha())

# 8- "Halit Barut" ifadesini 50 karakter içine ortalayıp kenarlarına '*' ekleyiniz

print("Halit Barut".center(50, '*'))

# 9- "Halit Barut" ifadesindeki boşlukları '-' ile değiştiriniz.

print("Halit Barut".replace(" ", "-"))

# 10- "Halit Barut" karakter dizisindeki 'Halit' karakterini 'Mehmet' olarak dağiştiriniz.

print("Halit Barut".replace("Halit", "Mehmet"))

# 11- "Mehmet Halit Barut" karakter dizisini boşluklardan ayıklayınız.

print("Mehmet Halit Barut".split(" "))
