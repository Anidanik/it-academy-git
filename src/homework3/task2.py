def list_practice():
    import itertools
    a=tuple((itertools.product('ab','bcd')))
    c,d,e=a[::2]
    print(c,d,e)
    b=[str(i)+'a' for i in range(1, 5)]
    print(b)
    print(b.pop(1))
    c=b.copy()
    c.append('2a')
    print(c)
list_practice()