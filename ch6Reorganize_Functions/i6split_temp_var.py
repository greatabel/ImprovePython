from termcolor import colored
from myfinal import MyPyFinal


def show(s,color='green'):
    return colored(s, color, attrs=['reverse', 'blink'])

def get_distance_travelled(time):
    primary_force = 100
    mass = 5
    delay = 3
    secodary_force = 50

    result = None
    acc = primary_force / mass
    primary_time = min(time, delay)
    result = 0.5 * acc * primary_time * primary_time
    secondary_time = time - delay
    if secondary_time > 0:
        primary_vel = acc * delay
        acc = (primary_force + secodary_force) / mass
        result = primary_vel * secondary_time + 0.5 * acc * secondary_time \
                 * secondary_time
    return result

r = get_distance_travelled(10)
print('old way which need to refactory: get_distance_travelled=', show(r))

def get_distance_after_refactory(time):
    primary_force = 100
    mass = 5
    delay = 3
    secodary_force = 50

    result = None
    primary_acc = MyPyFinal(primary_force / mass).r()
    primary_time = min(time, delay)
    result = 0.5 * primary_acc * primary_time * primary_time
    secondary_time = time - delay
    if secondary_time > 0:
        primary_vel = primary_acc * delay
        acc = (primary_force + secodary_force) / mass
        result = primary_vel * secondary_time + 0.5 * acc * secondary_time \
                 * secondary_time
    return result

r = get_distance_after_refactory(10)
print('old way which need to refactory: get_distance_travelled=', show(r, 'red'))
