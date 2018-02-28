from mycolor import show

print('某个函数既返回对象状态值， 又修改对象状态'
    + '建立2个不同函数，其中一个负责查询，另一个负责修改')

def send_alert_old():
        print('send_alert_old')

def found_miscreant_old(people):
    for p in people:
        if p == 'Don':
            send_alert_old()
            return 'Don'
        if p == 'John':
            send_alert_old()
            return 'John'
    return ''

def somelatercode(p):
    print('somelatercode(' + p + ')')

def check_security_old(people):
    found = found_miscreant_old(people)
    somelatercode(found)

check_security_old(['Abel', 'Don'])

print('-------------改造开始-----------------')

def found_person(people):
    for p in people:
        if p == 'Don':
            return 'Don'
        if p == 'John':
            return 'John'
    return ''

def send_alert(people):
    if found_person(people) != '':
        send_alert_old()


def check_security(people):
    send_alert(people)
    found = found_person(people)
    somelatercode(found)

check_security(['Abel', 'Don'])