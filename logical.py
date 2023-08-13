# BTK Akademi Python Dersi 4.5_Mantıksal Operatörler

x = 5
hak = 5
devam = 'e'

# and (matematikteki mantık dersindeki 've')
result = x > 5 and x < 10
result = (hak > 0) and (devam == 'e')

# or (matematikteki mantık dersindeki 'veya')
result = (x > 0) or  (x % 2 == 0)


# not (doğruluk değerinin değilini alır)
result = not(x > 0)

#****************************

# x, 5-10 arasında olan bir çift sayı mı?

result = ((x > 5) and (x < 10) and (x % 2 == 0))

