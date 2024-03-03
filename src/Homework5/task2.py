def biggest_dict(**kwargs):
    my_dict = {'first_one': 'we can do it'}
    my_dict.update(**kwargs)
    return my_dict


print(biggest_dict(Second='A', Third='B'))
