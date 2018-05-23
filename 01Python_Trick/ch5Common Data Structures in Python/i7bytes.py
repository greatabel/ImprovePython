arr = bytes((0, 1, 2, 3))
print(arr[1], arr)

arr = b'xx00x01x02x03'
try:
    bytes((0, 300))
except:
    print('An error occured: integers in the rangeof0<=x<=255')