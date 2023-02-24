def sum_of_squares(values, ls=[]):
    for value in values:
        ls.append(value ** 2)
    return sum(ls)

print(1, 2, 3, sum_of_squares([1, 2, 3]))
print(3, 2, 1, sum_of_squares([3, 2, 1]))
