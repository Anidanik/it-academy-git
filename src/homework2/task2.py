a = input('Введите свое предложение ')
b = a.split()
print(max(b, key=len))