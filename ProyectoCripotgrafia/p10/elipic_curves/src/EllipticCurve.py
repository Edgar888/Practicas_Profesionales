from Point import Point
from tools import *

class EllipticCurve:
    '''Clase que crea una curva elíptica usando un campo finito modulo p > 3'''

    # Punto al infinito siempre será None. Ignorar esta prueba unitaria
    inf_p = None

    def __init__(self, prime = 3, a = 1, b = 1):
        '''Construimos la curva elíptica a partir de los parámetros a, b modulo p'''
        self.original_a, self.original_b = a, b
        self.a, self.b = a % prime, b % prime
        self.prime = prime
        self.points = self.get_points()

    def __str__(self):
        '''La curva debe ser representada como: y^2 = x^3 + ax + b mod p'''
        return f"y^2 = x^3 + {self.original_a}x + {self.original_b} mod {self.prime}"

    def isInCurve(self, point):
        '''Nos dice si un punto "point" pertenece a esta curva'''
        if point is None:
            return True
        if not isinstance(point, Point):
            return False
        return (point.y ** 2) % self.prime == (point.x ** 3 + self.a * point.x + self.b) % self.prime

    def get_points(self):
        '''Nos da todos los puntos que pertenecen a la curva elíptica'''
        points = [None]
        for x in range(self.prime):
            right = (x ** 3 + self.a * x + self.b) % self.prime
            for y in range(self.prime):
                if (y * y) % self.prime == right:
                    points.append(Point(x, y))
        return points

    def sum(self, p, q):
        '''Suma p + q  regresando un nuevo punto modulo prime
        como está definido en las curvas elípticas. Recuerda que el punto al
        infinito funciona como neutro aditivo'''
        if p is None:
            return q
        if q is None:
            return p

        if p.x == q.x and p.y == inv_add(q.y, self.prime):
            return None

        if p == q:
            if p.y == 0:
                return None
            m = ((3 * p.x ** 2 + self.a) * inv_mult(2 * p.y, self.prime)) % self.prime
        else:
            if p.x == q.x:
                return None
            m = ((q.y - p.y) * inv_mult(q.x - p.x, self.prime)) % self.prime

        x3 = (m ** 2 - p.x - q.x) % self.prime
        y3 = (m * (p.x - x3) - p.y) % self.prime

        return Point(x3, y3)

    def mult(self, k, p):
        '''Suma  k veces el punto p (o k(P)).
        Si k < 0 entonces se suma el inverso de P k veces'''
        if k < 0:
            k, p = -k, self.inv(p)

        result, current = None, p
        while k > 0:
            if k & 1:
                result = self.sum(result, current)
            current = self.sum(current, current)
            k >>= 1

        return result

    def order(self, p):
        '''Dado el punto p que pertenece a la curva elíptica, nos regresa el mínimo entero k 
        tal que  k(P) = punto al infinito.'''
        k, current = 1, p
        while current is not None and k <= len(self.points):
            current = self.sum(current, p)
            k += 1

        return k

    def cofactor(self, p):
        '''Dado el punto p de la curva, regresa el total de puntos de la curva entre el orden
        de ese punto'''
        return len(self.points) / self.order(p)

    def inv(self, p):
        '''Regresa el inverso aditivo de este punto. Recuerda que es el mismo punto reflejado
        en el eje x'''
        if p is None:
            return None

        return Point(p.x, inv_add(p.y, self.prime))

