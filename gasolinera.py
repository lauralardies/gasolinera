from surtidor import Surtidor
from coche import Coche

t_pagar = 3
surtidor = Surtidor()
i = 0 # contador de tiempo (en minutos)

# CREAMOS COLA DE COCHES ORDENADAS POR TIEMPO DE LLEGADA
cola_coches = []
for i in range(0, 50):
    coche = Coche()
    if len(cola_coches) == 0:
        cola_coches.append(coche)
    else:
        i = -1
        for coche_delante in cola_coches:
            i = i + 1 # Para obtener la posicion del coche en la cola
            if coche_delante.t_llegada > coche.t_llegada:
                cola_coches.insert(i, coche)
                break


