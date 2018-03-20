from mycolor import show

EROPEAN = 0
AFRICAN = 1
NORWEGIAN = 2

coconuts = 10
is_nailed = False
voltage = 10
def get_speed_old(type):
    if type == EROPEAN:
        return getbase_speed()
    elif type == AFRICAN:
        return getbase_speed() - get_loadfactor() * coconuts
    elif type == NORWEGIAN:
        return 0 if is_nailed else getbase_speed(voltage)
    else:
        raise Exception('error!')

def getbase_speed(p=1):
    return p * 10

def get_loadfactor():
    return 100

t = get_speed_old(2)
print(show(t))

print('- · - - · - - · - - · - ')

class CountryFactory(object):
    @staticmethod
    def create(type):

        if type == EROPEAN:
            return Eropean()
        elif type == African:
            return AFRICAN()
        elif type == NORWEGIAN:
            return Norwegian()

class Country:
    name = None
    def speed(self):
        pass

class Eropean(Country):
    name = 'EROPEAN'

    def speed(self):
        return getbase_speed()

class African(Country):
    name = 'AFRICAN'
    def speed(self):
        return getbase_speed() - get_loadfactor() * coconuts

class Norwegian(Country):
    name = 'NORWEGIAN'
    def speed(self):
        return 0 if is_nailed else getbase_speed(voltage)

def get_speed(type):
    country = CountryFactory.create(type)
    return country.speed()

n = get_speed(2)
print(show(n, 'red'))