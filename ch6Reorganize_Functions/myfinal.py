# python 没有final， 自己造一个只读的
class MyPyFinal( object ):
    def __init__(self, value):
        self.value= value

    def __str__(self):
        return str(self.value)

    def r(self):
        # return result
        return self.value

    def set(self, value):
        if self.value is not None:
            raise Exception( "Read Only var.")
        self.value= value
