import random as r

class Entity:
    '''Clase que modela una entidad como Alice o Bob.'''

    def __init__(self, name, curve, generator_point, table):
        '''Construye un nuevo personaje con un mensaje para compartir
        Una entidad tiene:
        1. name: Nombre de la entidad
        2. curve: Una curva elíptica a compartir
        3. generator_point: Un punto generador a compartir
        4. table: Una codificacion de caracteres a puntos de la curva.

        Además, debe inicializar sus llaves, públicas y privadas:
        5. private_key: Un entero aleatorio entre 1 y el orden del punto generador-1
        6. private_point: Un punto aleatorio de la curva que no sea el punto al infinito
        ## 3 llaves públicas de esta entidad
        7. public_key_1, public_key_2, public_key_3 = None
        ## 3 llaves públicas de la otra entidad
        8. another_entity_public_key_1, another_entity_public_key_2, another_entity_public_key_3 = None'''
        self.name = name
        self.curve = curve
        self.generator_point = generator_point
        self.order =
        ## Cosas privadas
        self.private_key =
        self.private_point =
        # Cosas publicas
        self.public_key_1 = None #Public key using private point
        self.public_key_2 = None #Public key using only private key
        self.public_key_3 = None

        #Public keys from another entity
        self.another_entity_public_key_1 = None
        self.another_entity_public_key_2 = None
        self.another_entity_public_key_3 = None

        self.table = table

    def __str__(self):
        '''Representacion en cadena de la entidad'''

    def descifrar(self, ciphered_msg):
        '''Descifra un conjunto de parejas de puntos (e1, e2) de una curva elíptica a un texto
        plano legible humanamente'''

        # print(f'{self.name} descifró el mensaje! Dice: "{s}"')
        return s


    def cifrar(self, message):
        '''Cifra el mensaje (self.message) a puntos de la curva elíptica. Cada caracter es 
        mapeado a una pareja de puntos (e1, e2) con e1, e2 en EC.'''
        # Se usa un random para cada símbolo
        # print(f'{self.name} cifra el mensaje "{self.message}" como: ')
        if not message:
            return []
        values = list(self.table.values())
        keys = list(self.table.keys())
        self.cipher = []

        # print(self.cipher)
        return self.cipher

    def genera_llaves_publicas(self):
        '''Hace las operaciones correspondientes para generar la primera ronda de llaves
        públicas de esta entidad PK1 y PK2.'''
        self.public_key_1 =
        self.public_key_2 =
        # print(f'{self.name} genera sus llaves públicas como \npk1{self.public_key_1}\tpk2{self.public_key_2}')
        return (self.public_key_1, self.public_key_2, None)

    def recibe_llaves_publicas(self, public_keys):
        '''Recibe la llave publica de otra entidad y las guarda. (primera ronda solo guarda 2)
        o si ya es la segunda ronda, guarda la última llave (pk1, pk2 y pk3 != None)'''
        # print(public_keys) puede ser que alguna llave sea None, pero lo evitaremos por
        # motivos didácticos, pero no pasa nada, sigue funcionando
        if public_keys[2] == None:
            # print(f'{self.name} añadió una llave pública más: {public_keys}\n')
            self.another_entity_public_key_3 =
        else:
            self.another_entity_public_key_1 =
            self.another_entity_public_key_2 =
            # print(f'{self.name} recibe las llaves públicas de otra entidad y son: {public_keys}')

    def final_keys(self):
        '''Genera la última llave pública, en combinación con otra llave pública de otra entidad
        Regresa las 3 llaves públicas de esta entidad.'''
        public_keys = (self.public_key_1, self.public_key_2, None)
        self.public_key_3 =
        public_keys[2] = self.public_key_3
        # print(f'{self.name} crea su llave final como {self.public_key_3}')
        # print(f'Todas las llaves publicas de {self.name} son: {public_keys}\n')
        return public_keys

