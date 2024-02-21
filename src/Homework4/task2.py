def cities(n,m):
    cities = dict()
    for i in range(n):
        info = input('Введите названия страны и городов ').split()
        for city in info[1:]:
            cities[city] = info[0]
    res = []
    for i in range(m):
        city = input('Введите нужный вам город ')
        res.append(cities[city])
    print(*res, sep='\n')
cities(int(input('Введите число стран ')),int(input('Введите число нужных городов ')))