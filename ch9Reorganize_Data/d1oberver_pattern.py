# https://stackoverflow.com/questions/48336820/using-decorators-to-implement-observer-pattern-in-python3

class Event(object):
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

    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, value):
        self._foo = value
        self.changed.notify(self, 'foo', value)

class SomeGUI(object):
    def redraw(self, obj, key, newvalue):
        print('redrawing %s with value %s' % (self, newvalue))


if __name__ == '__main__':
    my_data = SomeData(42)

    # Register some function using decorator syntax
    @my_data.changed.register
    def print_it(obj, key, value):
        print('Key %s changed to %s' % (key, value))

    # Register the SomeGUI element
    my_gui = SomeGUI()
    my_data.changed.register(my_gui.redraw)

    # Try changing it.
    my_data.foo = 10