def dict_sort(*args):
    my_dict = {k: v for v, k in args}
    return my_dict


print(dict_sort(*dict.items({1: '1', 2: '2', 3: '3'})))
