def dict_from_list(keys,values):
    return {k:v for k,v in zip(keys,values)}
print(dict_from_list([1, 2, 3],[4, 5, 6]))