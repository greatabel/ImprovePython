def print_vector(x, y, z):
    print('here# <%s, %s, %s>' %(x, y, z))

print_vector(0, 1, 0)

tuple_vec = (1, 0, 1)
print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])

print('Function Argument Unpacking using the * operator')
print_vector(*tuple_vec)

list_vec = [1, 1, 1]
print_vector(*list_vec)