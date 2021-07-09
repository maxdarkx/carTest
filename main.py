from time import sleep
from pista_model import pista_model


pista = pista_model()
print("imprimir pista")
pista.print_pista()
sleep(2)
pista.clear_screen()


pista.mover_carril(3,10)
sleep(2)
pista.clear_screen()

pista.mover_carril(2,10)
sleep(2)
pista.clear_screen()

pista.mover_carril(2,100)
sleep(2)
pista.clear_screen()
pista.mover_carril(1,120)







