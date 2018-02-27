from mycolor import show

class Old_Person:
    def is_male(self):
        pass

    def get_code(self):
        pass

class Male(Old_Person):
    def is_male(self):
        return True

    def get_code(self):
        return 'M'

class Female(Old_Person):
    def is_male(self):
        return False

    def get_code(self):
        return 'F'

m = Male()
f = Female()
print(m.is_male(), m.get_code())
print(f.is_male(), f.get_code())

print(show('开始改造'),'- > -'*5)