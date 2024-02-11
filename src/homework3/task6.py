def ordered_list(a):
    for i in a:
        if i == '0':
            a.remove('0')
            a.append('0')
    print(a)
ordered_list(['1', '2', '3', '0', '5', '0', '9', '0'])