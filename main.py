import time
import os
from car_model import car_model
from conductor_model import conductor_model

def clear_screen():
    os.system('clear')


drivers =[conductor_model(1, "jose"), conductor_model(2, "juan")]
for j in range(2):
    for i in range(80):
        drivers[0].carro.mover(i)
        drivers[0].carro.car_print()
        drivers[1].carro.mover(i)
        drivers[1].carro.car_print()
        time.sleep(0.1)
        clear_screen()

print(drivers[0].get_id())
print(drivers[0].get_name())

print(drivers[1].get_id())
print(drivers[1].get_name())

