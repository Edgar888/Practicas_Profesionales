from Point import Point
from tools import *

class EllipticCurve:
    '''Clase que crea una curva elíptica usando un campo finito modulo p > 3'''

    # Punto al infinito siempre será None. Ignorar esta prueba unitaria
    inf_p = None

    def __init__(self, prime = 3, a = 1, b = 1):
        '''Construimos la curva elíptica a partir de los parámetros a, b modulo p'''

    def __str__(self):
        '''La curva debe ser representada como: y^2 = x^3 + ax + b mod p'''

    def isInCurve(self, point):
        '''Nos dice si un punto "point" pertenece a esta curva'''

    def get_points(self):
        '''Nos da todos los puntos que pertenecen a la curva elíptica'''

    def sum(self, p, q):
        '''Suma p + q  regresando un nuevo punto modulo prime
        como está definido en las curvas elípticas. Recuerda que el punto al
        infinito funciona como neutro aditivo'''

    def mult(self, k, p):
        '''Suma  k veces el punto p (o k(P)).
        Si k < 0 entonces se suma el inverso de P k veces'''

    def order(self, p):
        '''Dado el punto p que pertenece a la curva elíptica, nos regresa el mínimo entero k 
        tal que  k(P) = punto al infinito.'''

    def cofactor(self, p):
        '''Dado el punto p de la curva, regresa el total de puntos de la curva entre el orden
        de ese punto'''

    def inv(self, p):
        '''Regresa el inverso aditivo de este punto. Recuerda que es el mismo punto reflejado
        en el eje x'''

