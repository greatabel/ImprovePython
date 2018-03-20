from mycolor import show


def send_alert():
    print('send_alert')

def check_security_old(people):
    found = False
    for p in people:
        if not found:
            if p == 'Don':
                send_alert()
                found = True
            if p == 'John':
                send_alert()
                found = True

check_security_old(['Abel', 'Bob', 'Don'])

print('某个变量带哟 控制标记 [control flag] ' + 
      '以break 或者return 取代 控制标记')
print('- · - - · - - · - - · - ')

def check_security(people):
    found = False
    for p in people:

        if p == 'Don':
            send_alert()
            break
        if p == 'John':
            send_alert()
            break

check_security(['Abel', 'Bob', 'Don'])