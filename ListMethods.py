# BTK Akademi Python Dersleri 3.14_Pythonda Liste Metodları

numbers = [1, 7, 11, 66, 54]
letters = ["h","g","m","f","b"]

valmin = min(numbers) # en küçük değeri alır
valmax = max(numbers) # en büyük değeri alır

val = numbers[3:6] # 3. indexten 6. indexe kadar alır
val = numbers[:6:-1] # ilk indexten 6. indexe kadar tersten alır

numbers[4] = 41

numbers.append(49) # en sona belirtilen elemanı ekler
numbers.insert(3, 78) # belirtilen indexe belirtilen elemanı ekler.
print(numbers)

numbers.pop(2) # belirtilen yerdeki elemanı siler

numbers.sort() # elemanlar harf ya da küçükten büyüğe olarak sıralanır.
letters.sort() # elemanlar harf ya da küçükten büyüğe olarak sıralanır.

numbers.reverse() # elemanların sırası tam tersine döner.

uzunluk = len(numbers) # dizideki eleman sayısı.

count = numbers.count(1) # dizideki 1 sayısının kaç tane olduğunu belirtir

numbers.clear() # tüm elemanları siler.

print(numbers)


# BTK Akademi Python Dersleri 3.15_Uygulama Pythonda Liste Metodları

names = ['Ali', 'Yagmur' , 'Hakan', 'Deniz']
Degisennames = ['Ali', 'Yagmur' , 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
Degisennames = names
Degisennames.append('Cenk')

# 2- "Sena"' degerini listenin basina ekleyiniz.
Degisennames = names

Degisennames.insert(0,'Sena')

# 3- "Deniz" ismini listeden siliniz.
Degisennames = names

Degisennames.pop(3)

# 4- "Deniz" isminin indeksi nedir ?
print(names.index('Deniz'))

# 5- "Ali" listenin bir elemani midir ?
result = 'Ali' in names
print(result)

# 6- Liste elemanlarina ters çevirin.
names.reverse()

# 7- Liste elemanlarin alfabetik olarak siralayinaz.
names.sort()

# 8- years listesini rakamsal büyüklüge göre siralayiniz.
years.sort()

# 9- str = "Chevrolet, Dacia" karakter dizisini listeye ceviriniz.
str = "Chevrolet, Dacia"
str.split(',') # değişkenimiz belirtilen karakter ile ayrılarak bir diziye dönüşür

# 10- years dizisinin en büyük ve en küçük elemani nedir ?
min = min(years)
max = max(years)

# 11- years dizisinde kaç tane 1998 degeri vardir?
result = years.count(1998)

# 12- years dizisinin tüm elemanlarina siliniz.
years.clear()

# 13- Kullanicidan alacaginiz 3 tane marka bilgisini bir listede saklayiniz.
markalar = []
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
marka = input("marka: ")
markalar.append(marka)
print(markalar)
print(names)