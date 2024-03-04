def cities(number_of_countries,number_of_cities):
    cities = dict()
    for i in range(number_of_countries):
        info = input('Введите названия страны и городов ').split()
        for city in info[1:]:
            cities[city] = info[0]
    res = []
    for i in range(number_of_cities):
        city = input('Введите нужный вам город ')
        res.append(cities[city])
    print(*res, sep='\n')
cities(2,3)