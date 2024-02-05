a=input('Введите строку ')
s = 0
l = 0
for i in a:
    if 'a'<= i<= 'z':
        s=s+1
    elif 'A'<=i<='Z':
        l = l+1
print('Строчных букв ',s,'','Заглавных букв ',l)