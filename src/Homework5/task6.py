def dict_multiplication(my_dict):
    res=my_dict[1]
    for i in my_dict.values():
        res*=i
    return res
print(dict_multiplication({1:1,2:2,3:3,4:4}))