class Surtidor():
    def __init__(self):
        self.ocupado = False # Comienza el surtidor desocupado
        self.cola = [] # Como comienza desocupado, la cola está vacía --> NO se cuenta la persona que está echando la gasolina
    
    def ocupado(self):
        '''
        Función que muestra si el surtidor está ocupado
        '''
        return self.ocupado
    
    def largo_cola(self):
        '''
        Función que muestra cómo de larga es la cola del surtidor
        '''
        return len(self.cola)