def bar(requried, *args, **kwargs):
    print('0 requried=', requried)
    if args:
        print('1 args=', args)
    if kwargs:
        print('2 kwargs=', kwargs)


def foo(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra',)
    bar(x, *new_args , **kwargs)


foo('hello', 1, 2, 3, key1='value1', key2=999, name='test')