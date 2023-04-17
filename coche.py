import random

class Coche():
    def __init__(self):
        self.t_llegada = random.randint(0, 15) # Tiempo que tarda en llegar a la gasolinera.
        self.t_surtidor = random.randint(5, 10) # Tiempo que tarda en echar gasolina.
    
    def get_llegada(self):
        '''
        Devuelve el tiempo de llegada a la gasolinera del coche.
        '''
        return self.t_llegada
    
    def get_echar_gas(self):
        '''
        Devuelve el tiempo que el coche tarda en echar gasolina.
        '''
        return self.t_surtidor