def languages(number_of_students):
    students = [{input('Введите язык ')
                for j in range(int(input(f'Введите количество языков {i+1} студента ')))}
                for i in range(number_of_students)]
    known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
    print('Знают все ',len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
    print('Знает хотя бы один ',len(known_by_someone), *sorted(known_by_someone), sep='\n')
languages(2)
