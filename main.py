import time
import os
from car_model import car_model

def clear_screen():
    os.system('clear')

carro1 = car_model()
for i in range(100):
    carro1.car_print(i)
    time.sleep(0.1)
    clear_screen()
