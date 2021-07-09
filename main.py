import os
import time

from car_model import car_model
from conductor_model import conductor_model
from carril_model import carril_model


carril1= carril_model(1,150)
carril1.clear_screen()
carril1.set_posicion(70)
carril1.print_carril()
time.sleep(2)
carril1.clear_screen()
carril1.mover_clear(110)

print(carril1.pos)
"""for i in range(20):
    carril1.set_posicion(50+i)
    carril1.print_carril()
    time.sleep(0.1)
    if i < 19:
        carril1.clear_screen()"""



