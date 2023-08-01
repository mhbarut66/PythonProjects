print("Hello World")

a = "Selamun Aleykum"

result = len(a)

print(result)

result2 = a[0:3]

print(result2)

print(a[7:1:-1])

isim = "Halit"
soyisim = "Barut"
yas = 18
meslek = "Bilgisayar Mühendisi"

print("Adım " + isim + " Soyadım " + soyisim + " Yaşım " + str(yas) + " Mesleğim " + meslek)
print("Adım {0} Soyadım {1} Yaşım {2} Mesleğim {3}".format(isim,soyisim,yas,meslek))
print(f"Adım {isim} Soyadım {soyisim} Yaşım {yas} Mesleğim {meslek}")

# Methods

message = "Hello there. My name is Halit"

print(message.upper())

print(message.lower())

print(message.title())

print(message.capitalize())

print(message.strip())

print(message.split('.'))

print(message.find("s"))

print(message.startswith("H"))

print(message.replace("Halit",'Barut'))

print(message.center(50,'*'))
