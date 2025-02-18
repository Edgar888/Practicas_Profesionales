# Default alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.!¡?¿#_'

def isPrime(n):
    '''Nos dice si un número n es primo'''
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def inv_add(a, mod):
    '''Nos da el inverso aditivo tal que a + i == 0 modulo n'''
    return (-a) % mod


def inv_mult(a, mod):
    '''Nos da el inverso multiplicativo modulo n'''
    for i in range(1, mod):
        if (a * i) % mod == 1:
            return i
    raise ValueError(f"El inverso multiplicativo de {a} mod {mod} no existe")

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
