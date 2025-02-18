class Point:
    '''Clase que representa un punto en un plano 2D'''

    #Punto al infinito
    infinite_point = None

    def __init__(self, x = 0, y = 0):
        '''Constructor: Construye un punto en un plano 2D con coordenadas (x,y)'''

    def __str__(self):
        '''Representación en cadena. Usamos str(p)'''

    def __repr__(self):
        '''Representación en cadena x2. Usamos print(p)'''

    def __eq__(self, another_point):
        '''Comparación entre 2 puntos. Usamos ==
        another_point debe ser instancia de Point'''

    def set(self, x, y):
        '''Reescribe los valores de x y y a este punto.
        @raise ValueError si x o y no son números enteros'''

