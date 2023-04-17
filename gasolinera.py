from surtidor import Surtidor
from coche import Coche
from tienda import Tienda

surtidor = Surtidor()
tienda = Tienda()
contador = -1 # Contador de tiempo (en minutos)

# CREAMOS COLA DE COCHES ORDENADA POR TIEMPO DE LLEGADA
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

while True:
    contador = contador + 1
    if contador == cola_coches[0].t_llegada: # En este if manejamos la entrada de coches
        print('Entra un coche a la gasolinera.')
        if surtidor.ocupado == False:
            contador_gasolina = -1
            contador_pago = -1
            surtidor.cliente = cola_coches[0]
            surtidor.ocupado = True
        else:
            surtidor.cola.append(cola_coches[0])
        cola_coches.remove(cola_coches[0]) # Borramos el coche de la cola de coches
        
    if surtidor.ocupado == True:
        contador_gasolina = contador_gasolina + 1
        if contador_gasolina == surtidor.cliente.t_surtidor:
            print('Entra cliente a la tienda.')
            tienda.pagando = True
            
    if tienda.cliente_pagando == True:
        contador_pago = contador_pago + 1
        if contador_pago == 3:
                print('El cliente ya ha pagado, se va.')
                surtidor.cliente = surtidor.cola[0]
                surtidor.cola.remove(surtidor.cola[0])
                contador_gasolina = -1
                contador_pago = -1