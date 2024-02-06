a = int(input('Введите n '))
fib1 = fib2 = 1
n = a-2
while n>0:
    fib1,fib2 = fib2,fib1 + fib2
    n-=1
if a == 0:
    print(0)
else:
    print(fib2)