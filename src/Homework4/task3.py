def identical(a,b):
    c=0
    for i in set(a):
        for j in set(b):
            if i == j:
                c += 1
    print(c)
identical([1, 2, 3, 4, 5],[6, 4, 2, 1])