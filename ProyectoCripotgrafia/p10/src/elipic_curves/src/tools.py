# Default alphabet
alphabet = 'ABC'

def isPrime(n):
    '''Nos dice si un número n es primo'''

def inv_add(a, mod):
    '''Nos da el inverso aditivo tal que a + i == 0 modulo n'''

def inv_mult(a, mod):
    '''Nos da el inverso multiplicativo modulo n'''

def table(elliptic_curve, alphabet = alphabet):
    '''Regesa una tabla de un abecedario mapeado a puntos de la curva elíptica e'''
    pts = elliptic_curve.points
    if len(pts) < len(alphabet):
        # print("Las letras mapeadas no caben en la definición de la curva. Se recortará el alfabeto...\n")
        l = alphabet[:len(pts)]
    else:
        # print("Faltan caracteres a relacionar, se duplicará el alfabeto")
        l = alphabet
        while len(pts) > len(l):
            l = l+l
        l = alphabet[:len(pts)]
    table = {}

    i = 0
    while i != len(pts):
        table[l[i]] = pts[i]
        i+=1
    return table
