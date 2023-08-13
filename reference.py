# BTK Akademi Python Dersi 3.20_Pythonda Value ve Reference

x = 5
y = 25

x = y

y = 10

# x değişkeni ynin yeni değerinden etkilenmez.

# *************************

a = ["apple", "banana"]
b = ["apple", "banana"]

a = b

b[0] = "grape"

# a listesi bnin yeni değerinden etkilenir.

print(a, b)