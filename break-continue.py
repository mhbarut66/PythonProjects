# BTK Akademi Python Dersi 6.5_Break ve Continue İfadeleri

name = 'Halit Barut'

for letter in name:
    if letter == 'a':
        continue
    print(letter)


    x = 0

    while x < 5:
        x += 1
        if x == 2:
            break
        

# 1 - 100 e kadar tek sayıların toplamı

x = 0
result = 0

while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    result += x
    

print(result)