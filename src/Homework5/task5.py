def dict_addition(dictionary_1,dictionary_2):
    dictionary_1.update(dictionary_2)
    return dictionary_1


print(dict_addition({'a': 300, 'b': 400},{'c': 500, 'd': 600}))