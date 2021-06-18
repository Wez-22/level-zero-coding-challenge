def area_of_a_triangle(x, y, z):
    s = 1/2*(x + y + z)
    area = (s)*(s-x)*(s-y)*(s-z)
    area = area**0.5
    return area

print(area_of_a_triangle(3,4,5))
