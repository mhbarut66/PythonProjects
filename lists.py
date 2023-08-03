# BTK Akademi Python Dersi 3.12_Pythonda Listeler

message = 'Hello there. My name is Halit Barut.'.split()
# print(message)

myList = [1,2,3]

list1 = ['one','two','three']
list2 = ['four','five','six']

numbers = list1 + list2

print(len(numbers))
print(len(numbers[0]))

userA = ['Halit', 18]
userB = ['Barut', 17]

# BTK Akademi Python Dersi 3.13_Uygulama - Pythonda Listeler

# 1- "Bmw, Mercedes, Opel, Skoda" elemanlarina sahip bir liste olusturunuz.
arabalar = ['BMW', 'Mercedes', 'Opel', 'Skoda']

# 2- Liste Kaç elemanlidir ?
print(len(arabalar))

# 3- Listenin ilk ve son elemani nedir ?
print(f"İlk eleman: {arabalar[0]}, Son eleman {arabalar[-1]}.")

# 4- Skoda degerini Peugeout ile degistirin.
arabalar[-1] = "Peugeout"

# 5- Mercedes listenin bir eleman midir ?
print('Mercedes' in arabalar)

# 6- Listenin -2 indeksindeki deger nedir ?
print(arabalar[-2])

# 7- Listenin ilk 3 elemanini alin.
print(arabalar[0:3])

# 8- Listenin son 2 elemani yerine "Peugeout" ve "Renault" degerlerini ekleyin.
arabalar[-2:] = ['Peugeout','Renault']

# 9- Listenin üzerine "Audi" ve "Nissan" degerlerini ekleyin.
result = arabalar + ['Audi', 'Nissan']

# 10- Listenin son elemanini silin.
del arabalar[-1]
result = arabalar

# 11 - Liste elemanlarina tersten yazdiriniz.
print(arabalar[::-1])

# 12 - Asagidaki verileri bir liste içinde saklayiniz.

    # studentA: Vigit Bilgi 2010, (70, 60, 70)
    # studentB: Sena Turan 1999, (80,80,70)
    # student: Ahmet Turan 1998, (80, 70, 90)

studentA = ['Yiğit', 'Bilgi', 2010, [70, 60, 70]]
studentB = ['Sena', 'Turan', 1999, [80, 80, 70]]
studentC = ['Ahmet', 'Turan', 1998, [80, 70, 90]]


# 13 - Liste elemanlarini ekrana yazdirin.

result = studentB[1]

result = f"{studentA[0]} {studentA[1]} {2023 - studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2]) / len(studentA[3])}"

print(result)