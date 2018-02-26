from mycolor import show

class Event:
    def __init__(self):
        self.callbacks = []

    def notify(self, *args, **kwargs):
        for callback in self.callbacks:
            callback(*args, **kwargs)

    def register(self, callback):
        self.callbacks.append(callback)
        return callback

class SomeData(object):
    def __init__(self, foo):
        self.changed = Event()
        self._foo = foo
        print('#'*10, 1)

    @property
    def foo(self):
        print('#'*10, 2)
        return self._foo

    @foo.setter
    def foo(self, value):
        print('#'*10, 3)
        self._foo = value
        start, end = value
        print('length=', end - start)
        self.changed.notify(self, 'foo', value)



class SomeGUI(object):
    def redraw(self, obj, key, newvalue):
        print('redrawing %s with value %s' % (self, newvalue))

if __name__ == '__main__':
    my_data = SomeData((4, 12))
    print(my_data.foo)

    @my_data.changed.register
    def print_it(obj, key, value):
        print('Key %s changed to %s' % (key, value))

    # Register the SomeGUI element
    my_gui = SomeGUI()
    my_data.changed.register(my_gui.redraw)

    # Try changing it.
    my_data.foo = (5, 10)
    my_data.foo = (5, 11)
    my_data.foo = (2, 11)
