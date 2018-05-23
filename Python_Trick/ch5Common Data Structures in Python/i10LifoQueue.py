from queue import LifoQueue

s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')

print(s)

print(s.get())
print(s.get())
print(s.get())

print(s.get_nowait())
print(s.get())