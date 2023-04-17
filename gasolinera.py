import random
from surtidor import Surtidor

surtidor = Surtidor()

while True:
    t = random.randint(0, 15) # Se escoge aleatoriamente el tiempo en el que viene el siguiente coche
    for i in range(16): # Pasa el tiempo por cada vez que se ejecuta bucle for
        if i == t: # Sólo entramos si ha pasado el tiempo en el que llega el siguiente coche
            print('Entra un coche a la gasolinera')

            

