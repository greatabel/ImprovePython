def foo(requried, *args, **kwargs):
    print('0 requried=', requried)
    if args:
        print('1 args=', args)
    if kwargs:
        print('2 kwargs=', kwargs)



foo('hello')
foo('hello', 1, 2, 3)
foo('hello', 1, 2, 3, key1='value1', key2=999)