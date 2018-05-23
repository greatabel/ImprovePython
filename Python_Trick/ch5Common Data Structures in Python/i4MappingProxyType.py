from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

writable['one'] = 10
print('writable=', writable)

print(read_only['one'])
try:
    read_only['one'] = 23
except Exception:
    print('Exception happened')
    pass