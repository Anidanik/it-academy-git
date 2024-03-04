def puthonist(a):
    my_dict={i:a.count(i) for i in a}
    return my_dict
print(puthonist('pythonist'))