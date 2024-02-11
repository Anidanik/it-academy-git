def sum_of_pairs(a):
    b=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                    b+=1
    print('Количество пар ', b)
sum_of_pairs([1, 2, 1, 5, 1, 6, 1, 1])