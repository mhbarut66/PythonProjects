# BTK Akademi Python Dersleri 3.14_Pythonda Liste Metodları

numbers = [1, 7, 11, 66, 54]
letters = ["h","g","m","f","b"]

valmin = min(numbers) # en küçük değeri alır
valmax = max(numbers) # en büyük değeri alır

val = numbers[3:6] # 3. indexten 6. indexe kadar alır
val = numbers[:6:-1] # ilk indexten 6. indexe kadar tersten alır

numbers[4] = 41

numbers.append(49) # en sona belirtilen elemanı ekler
numbers.insert(3, 78) # belirtilen indexe belirtilen rakamı ekler.
print(numbers)

numbers.pop(2) # belirtilen yerdeki elemanı siler

numbers.sort() # elemanlar harf ya da küçükten büyüğe olarak sıralanır.
letters.sort() # elemanlar harf ya da küçükten büyüğe olarak sıralanır.

numbers.reverse() # elemanların sırası tam tersine döner.

uzunluk = len(numbers) # dizideki eleman sayısı.

count = numbers.count(1) # dizideki 1 sayısının kaç tane olduğunu belirtir

numbers.clear() # tüm elemanları siler.

print(numbers)


