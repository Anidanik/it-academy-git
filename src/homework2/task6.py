a = int(input('Введите число '))
b = 0
if a==0:
    print('Это число является палиндромом')
elif a<0 or a//10 == 0:
    print('Это число не является палиндромом')
else:
    while a>b:
        d = a%10
        c = a
        print('d ',d)
        a = a//10
        print('a ',a)
        b = b*10+d
        print ('b ',b)
    if c==b:
        print('Это число является палиндромом')
    else:
        print('Это число не является палиндромом')
