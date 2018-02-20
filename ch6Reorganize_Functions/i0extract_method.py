def printBanner():
    print('printBanner()')

def printOwing(amount):
    printBanner()
    name = 'abel'
    print("name:" + name)
    print("amount:" + amount)

print("Etract Method ：当我看到一个过长的函数或者一段需要注释才能理解的代码，我们放入独立函数")
def print_detail(amount, name):
    print("name:" + name)
    print("amount:" + amount)

def printOwing_afterRefactory(amount):
    printBanner()
    name = 'abel'
    print_detail(amount, name)
