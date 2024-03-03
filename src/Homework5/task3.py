def count_it(sequence):
    my_dict = {int(item): sequence.count(item) for item in sequence}
    sorted_dict = sorted(my_dict.items(), key=lambda element: element[1])
    return sorted_dict[-3:]


print(count_it('16942296'))
