def nod(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(a + b)
nod(int(input('Введите первое число ')),int(input('Введите второе число ')))