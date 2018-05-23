import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))

print('arr[1], arr[2]=', arr[1], arr[2])
print(arr)
arr[1] = 111
print(arr)

del arr[1]
print(arr)

arr.append(333)
print(arr)

try:
    arr[1] = 'hello'
except:
    print('An error occured.')
