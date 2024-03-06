def identical(a,b):
    print(len(set.intersection(set(a),set(b))))
identical([1, 2, 3, 4, 5, 8],[6, 4, 2, 1, 5])