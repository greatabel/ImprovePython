def print_vector(x, y, z):
    print('here# <%s, %s, %s>' %(x, y, z))

print_vector(0, 1, 0)

tuple_vec = (1, 0, 1)
print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])

print('Function Argument Unpacking using the * operator')
print_vector(*tuple_vec)

list_vec = [1, 1, 1]
print_vector(*list_vec)

genexpr = (x * x for x in range(10, 13))

print_vector(*genexpr)

dict_vec = {'x': 10, 'y': 20, 'z': 30}
print('** operator for unpacking keyword arguments from dictionaries.')
print_vector(**dict_vec)