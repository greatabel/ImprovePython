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

print('建立子类的目的，是为了增加新特性或者变化其行为' +
      '但若子类种只有常量函数，是在没有足够的价值' +
      '你可以在超类种设计敞亮函数返回相应字段，从而去除这样的子类' + 
      '这样你就避免因继承而带来的额外的复杂性')
print(show('开始改造'),'- > '*5)

class Person:
    def create(self, is_male, code):
        self.is_male = is_male
        self.code = code
        return self

    @staticmethod
    def create_male():
        # return New_Male()
        return Person().create(True, 'M')

    @staticmethod
    def create_female():
        # return New_Female()
        return Person().create(False, 'F')

# class New_Male(Person):
#     def __init__(self):
#         super(New_Male, self).create(True, 'M')


# class New_Female(Person):
#     def __init__(self):
#         super(New_Female, self).create(False, 'F')

m = Person.create_male()
f = Person.create_female()
# print(m.is_male(), m.get_code())
# print(f.is_male(), f.get_code())
print(m.is_male, m.code)
print(f.is_male, f.code)


