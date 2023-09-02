# BTK Akademi Python Dersi 6.6_Döngü Metotları - range() enumerate() zip()

# range ----------------------------

for item in range(30,100,10):
    print(item)

print(list(range(5,100,10)))

# enumerate ----------------------------

greeting = 'Hello There'

for index, letter in enumerate(greeting):
    print(f'index : {index}, letter: {letter}')


# zip ----------------------------

list1 = [1,2,3,4,5]

list2 = ['a', 'b', 'c', 'd', 'e']

list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))

for a,b,c in zip(list1, list2, list3):
    print(a,b,c)