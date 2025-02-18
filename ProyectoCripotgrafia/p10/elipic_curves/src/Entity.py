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
        self.order = self.curve.order(generator_point)
        ## Cosas privadas
        self.private_key = r.randint(1, self.order - 1)
        # Punto privado
        while True:
            self.private_point = r.choice(self.curve.points[1:])
            if self.curve.sum(generator_point, self.private_point) is not None:
                break
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
        return f"{self.name}:\nEC: {self.curve}\nG: {self.generator_point}\nPrivate Key: {self.private_key}\nPrivate Point: {self.private_point}\n"

    def descifrar(self, ciphered_msg):
        '''Descifra un conjunto de parejas de puntos (e1, e2) de una curva elíptica a un texto
        plano legible humanamente'''

        if not ciphered_msg:
            return ""

        plain = ""
        for e1_char, e2_char in ciphered_msg:
            try:
                e1 = self.table[e1_char]
                e2 = self.table[e2_char]

                # Inversión de operaciones para obtener P
                temp1 = self.curve.mult(self.private_key, e1)
                temp2 = self.curve.mult(self.private_key, self.another_entity_public_key_1)
                sum_temp = self.curve.sum(temp1, temp2)
                sum_temp = self.curve.sum(sum_temp, self.another_entity_public_key_3)
                sum_temp = self.curve.inv(sum_temp)

                # Recuperar el punto original del mensaje
                P = self.curve.sum(e2, sum_temp)

                # Mapeo del punto a un carácter en la tabla
                found = False
                for k, v in self.table.items():
                    if v == P:
                        plain += k
                        found = True
                        break

                # Si el punto P no tiene mapeo, agrega un espacio
                if not found:
                    plain += " "

            except Exception as e:
                plain += " "

        return plain


    def cifrar(self, message):
        '''Cifra el mensaje (self.message) a puntos de la curva elíptica. Cada caracter es 
        mapeado a una pareja de puntos (e1, e2) con e1, e2 en EC.'''
        # Se usa un random para cada símbolo
        if not message:
            return []

        cipher = []
        for char in message:
            # Asegúrate de que el carácter está en la tabla
            if char not in self.table:
                print(f"Advertencia: carácter '{char}' no encontrado en la tabla")
                continue

            # Mapeo de caracteres a puntos
            M = self.table[char]
            r_value = r.randint(1, self.order - 1)

            # Genera el primer punto del cifrado
            e1 = self.curve.mult(r_value, self.generator_point)

            # Genera el segundo punto del cifrado
            temp1 = self.curve.mult(self.private_key + r_value, self.another_entity_public_key_1)
            temp2 = self.curve.mult(r_value, self.another_entity_public_key_2)
            temp2 = self.curve.inv(temp2)

            e2 = self.curve.sum(M, temp1)
            e2 = self.curve.sum(e2, temp2)
            e2 = self.curve.sum(e2, self.another_entity_public_key_3)

            # Mapeo de puntos de cifrado a caracteres
            e1_char = e2_char = None
            for k, v in self.table.items():
                if v == e1:
                    e1_char = k
                if v == e2:
                    e2_char = k
                if e1_char and e2_char:
                    break

            # Manejo de espacios como caracteres de respaldo
            first_char = next(iter(self.table))
            cipher.append((e1_char or first_char, e2_char or first_char))

        return cipher

    def genera_llaves_publicas(self):
        '''Hace las operaciones correspondientes para generar la primera ronda de llaves
        públicas de esta entidad PK1 y PK2.'''
        sum_point = self.curve.sum(self.generator_point, self.private_point)
        self.public_key_1 = self.curve.mult(self.private_key, sum_point)
        self.public_key_2 = self.curve.mult(self.private_key, self.private_point)

        if not self.public_key_1 or not self.public_key_2:
            raise ValueError("Error al generar llaves públicas")

        return [self.public_key_1, self.public_key_2]

    def recibe_llaves_publicas(self, public_keys):
        '''Recibe la llave publica de otra entidad y las guarda. (primera ronda solo guarda 2)
        o si ya es la segunda ronda, guarda la última llave (pk1, pk2 y pk3 != None)'''
        # print(public_keys) puede ser que alguna llave sea None, pero lo evitaremos por
        # motivos didácticos, pero no pasa nada, sigue funcionando
        if len(public_keys) == 2:
            self.another_entity_public_key_1, self.another_entity_public_key_2 = public_keys
        else:
            self.another_entity_public_key_3 = public_keys[2]

    def final_keys(self):
        '''Genera la última llave pública, en combinación con otra llave pública de otra entidad
        Regresa las 3 llaves públicas de esta entidad.'''
        self.public_key_3 = self.curve.mult(self.private_key, self.another_entity_public_key_2)
        return (self.public_key_1, self.public_key_2, self.public_key_3)

