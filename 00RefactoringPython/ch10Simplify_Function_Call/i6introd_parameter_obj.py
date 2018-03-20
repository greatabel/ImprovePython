from mycolor import show

def test(start, end):
    print('do things to ', start, end)

test(10, 100)
print('-------------改造开始-----------------')

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def test_afterRF(range):
    print(show('do things to ', 'red'), range.start, range.end)

test_afterRF(Range(10, 100))