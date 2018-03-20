from mycolor import show

class Employee_Old:
    pass

class Manager_Old(Employee_Old):
    def __init__(self, name, id, grade):
        print('do something!')
print('-------------改造开始-----------------')


class Employee(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Manager(Employee):
    def __init__(self, name, id, grade):
        super(Manager, self).__init__(name, id)
        self.grade = grade

m = Manager('abel', '10001', 'grade 21')
print(m.name, m.id, m.grade)