def FizzBuzz ():
    a=[i for i in range(100)]
    for i in a:
        if i%3==0 and i%5==0:
            a[i]='FizzBuzz'
        elif i%5==0:
            a[i]='Buzz'
        elif i%3==0:
            a[i]= 'Fizz'
    print(a)
FizzBuzz()