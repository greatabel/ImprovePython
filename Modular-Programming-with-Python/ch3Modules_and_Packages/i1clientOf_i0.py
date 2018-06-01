import i0test_module

print('-'*10)
i0test_module.foo()
i0test_module.bar()

print(i0test_module.my_var)
i0test_module.my_var = 111
print(i0test_module.my_var)