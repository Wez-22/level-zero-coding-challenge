def find_the_largest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


print(find_the_largest_number(22, 55, 3))
