from mycolor import show

def potential_energy(mass, height):
    return mass * 9.81 * height

old = potential_energy(10, 100)
print('magic number way:', show(old))
print(show('开始改造'),'- > -'*5)

GRAVITATIONAL_CONSTANT = 9.81 

def potential_energy_afterRF(mass, height):
    return mass * GRAVITATIONAL_CONSTANT * height

new = potential_energy_afterRF(10, 100)
print('symbolic constant way:', show(new, 'red'))