from mycolor import show

EROPEAN = 0
AFRICAN = 1
NORWEGIAN = 2

def get_speed(type, coconuts, is_nailed, voltage):
    if type == EROPEAN:
        return getbase_speed()
    elif type == AFRICAN:
        return getbase_speed() - get_loadfactor() * coconuts
    elif type == NORWEGIAN:
        return 0 if is_nailed else getbase_speed(voltage)
    else:
        raise Exception('error!')

def getbase_speed(p=1):
    return p * 10

def get_loadfactor():
    return 100
    
t = get_speed(2, 10, False, 10)
print(show(t))