def bark(text):
    return (text.upper() + "!!!")

funcs = [bark, str.lower, str.capitalize]

print('funcs = ', funcs)

for f in funcs:
    print(f, f('hey there'))
