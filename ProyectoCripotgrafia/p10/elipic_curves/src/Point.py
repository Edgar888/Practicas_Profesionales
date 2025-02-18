class Point:
    '''Clase que representa un punto en un plano 2D'''

    #Punto al infinito
    infinite_point = None

    def __init__(self, x = 0, y = 0):
        '''Constructor: Construye un punto en un plano 2D con coordenadas (x,y)'''
        try:
            self.x, self.y = int(float(x)), int(float(y))
        except (ValueError, TypeError):
            self.x, self.y = 0, 0

    def __str__(self):
        '''Representación en cadena. Usamos str(p)'''
        return "Punto al infinito" if self == Point.infinite_point else f"({self.x}, {self.y})"

    def __repr__(self):
        '''Representación en cadena x2. Usamos print(p)'''
        return self.__str__()

    def __eq__(self, another_point):
        '''Comparación entre 2 puntos. Usamos ==
        another_point debe ser instancia de Point'''
        if not isinstance(another_point, Point) and another_point is not None:
            return False
        if self is Point.infinite_point or another_point is Point.infinite_point:
            return self is another_point
        return self.x == another_point.x and self.y == another_point.y

    def set(self, x, y):
        '''Reescribe los valores de x y y a este punto.
        @raise ValueError si x o y no son números enteros'''
        try:
            nuevo_punto_x = int(float(x))
            nuevo_punto_y = int(float(y))
            self.x = nuevo_punto_x
            self.y = nuevo_punto_y
        except (ValueError, TypeError):
            pass

