EROPEAN = 0
AFRICAN = 1
NORWEGIAN = 2

def getbase_speed(p=1):
    return p * 10

def get_loadfactor():
    return 100

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
        return getbase_speed() - get_loadfactor()

class Norwegian(Country):
    name = 'NORWEGIAN'
    def speed(self):
        return  2 * getbase_speed()


if __name__ == "__main__":
    country = CountryFactory.create(2)
    print(country.speed())


