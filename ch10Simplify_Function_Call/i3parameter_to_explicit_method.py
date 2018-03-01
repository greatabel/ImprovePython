from mycolor import show

def set_value(name, value):
    if name == 'height':
        _height = value
        return 
    if name == 'width':
        _width = value
        return
    assert False, 'should never be here'

set_value('height', 10)
print('-------------改造开始-----------------')

def set_height(arg):
    _height = arg

def set_width(arg):
    _width = arg

set_height(10)