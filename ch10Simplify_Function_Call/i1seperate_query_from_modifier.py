from mycolor import show

print('某个函数既返回对象状态值， 又修改对象状态'
    + '建立2个不同函数，其中一个负责查询，另一个负责修改')

def send_alert():
        print('send_alert')

def found_miscreant(people):
    for p in people:
        if p == 'Don':
            send_alert()
            return 'Don'
        if p == 'John':
            send_alert()
            return 'John'
    return ''

def somelatercode(p):
    print('somelatercode(' + p + ')')

def check_security(people):
    found = found_miscreant(people)
    somelatercode(found)

check_security(['Abel', 'Don'])

#-------------改造开始-----------------