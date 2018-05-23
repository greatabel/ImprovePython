arr = 'abcd'

print(arr[1])

try:
    arr[1] = 'e'
    del arr[1]
except:
    print('An error occured.')

print("list('abcd')=", list('abcd'))
