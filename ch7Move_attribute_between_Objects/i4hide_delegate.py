from mycolor import show

class Person:
    def __init__(self, name, dpmt):
        self.name = name
        self.department = dpmt


    def __str__(self):
        return 'name:' + self.name
class Department:
    def __init__(self, chargecode, manager):
        self.chargecode = chargecode
        self.manager = manager

john = Person('john1', Department('01', Person('bob', None)))
old_way_manager = john.department.manager
print(old_way_manager)