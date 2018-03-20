from mycolor import show

class DemoClass:
    def __init__(self):
        self.balance = 0

    def withdraw_old(self, amount):
        if amount > self.balance:
            return -1
        else:
            self.balance -= amount
            return 0

d = DemoClass()
r = d.withdraw_old(10)
print(show(r))

print('程序种发现错误的地方，并不一定知道如何处理错误，需要让调用者知道错误'
    + ' 清楚的将 普通程序 和 错误处理 分开，让程序更容易理解，代码可读性是我们虔诚追求的目标🏆')
print('-------------改造开始-----------------')
class DemoClass_AfterRF:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception('Balance Exception!')
        self.balance -= amount

d1 = DemoClass_AfterRF()
d1.withdraw(10)