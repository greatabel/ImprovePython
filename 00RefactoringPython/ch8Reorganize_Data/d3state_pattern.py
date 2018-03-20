import itertools
from mycolor import show


class State:
    def scan(self):
        print("Scanning... Station is",
            next(self.stations), self.name)

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = itertools.cycle(
            ['1000', '1001', '1002'])
        self.name = "AM"

    def toogle(self):
        print('switching to FM')
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = itertools.cycle(
            ['81.1', '82.2', '83.3'])
        self.name = 'FM'

    def toogle(self):
        print('switching to AM')
        self.radio.state = self.radio.amstate


class Radio:
    """
    A radio.
    It has a scan button, and an AM/FM toggle switch.
    """
    def __init__(self):
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toogle(self):
        self.state.toogle()

    def scan(self):
        self.state.scan()

def main():
    radio = Radio()
    actions = ([radio.scan] * 2 + 
                [radio.toogle] + [radio.scan] * 2) * 2
    for action in actions:
        action()

if __name__ == "__main__":
    main()