import os

class Soko:
    # 0 = Personaje
    # 1 = Caja 
    # 2 = Meta
    # 3 = Pared 
    # 4 = Espacio 
    # 5 = Caja_Meta 
    # 6 = Personaje_meta

    mapa = [] # mapa del juego
    # Identifica al personaje
    personaje_columna = 0
    personaje_fila = 0 

    def __init__(self):
        # Define el mapa de juego
        
        self.mapa = [
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 4, 4, 4, 4, 4, 4, 4, 3],
            [3, 4, 4, 4, 4, 4, 4, 4, 3],
            [3, 4, 4, 4, 0, 1, 3, 4, 3],
            [3, 4, 4, 4, 4, 4, 4, 4, 3],
            [3, 4, 4, 4, 4, 4, 4, 2, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]

        # Definimos la posicion inicial del personaje
        self.personaje_columna = 4
        self.personaje_fila = 3

    def imprimirMapa(self):
        #Limpiar pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        for filas in self.mapa:
            print(filas)

    def movimiento(self, nueva_fila, nueva_columna):
        # Verifica si la nueva posición es válida
        if 0 <= nueva_fila < len(self.mapa) and 0 <= nueva_columna < len(self.mapa[0]):
            # Si la nueva posición es un espacio o una meta, mueve al personaje
            if self.mapa[nueva_fila][nueva_columna] in [4, 2]:
                self.mapa[self.personaje_fila][self.personaje_columna] = 4
                self.personaje_fila = nueva_fila
                self.personaje_columna = nueva_columna
                if self.mapa[nueva_fila][nueva_columna] == 2:  # Si la nueva posición es Meta, convierte al personaje en Personaje_Meta
                    self.mapa[nueva_fila][nueva_columna] = 5
                else:
                    self.mapa[nueva_fila][nueva_columna] = 0
            # Si la nueva posición es una caja y la siguiente casilla es un espacio o una meta, mueve la caja y al personaje
            elif self.mapa[nueva_fila][nueva_columna] == 1:
                siguiente_fila = nueva_fila + (nueva_fila - self.personaje_fila)
                siguiente_columna = nueva_columna + (nueva_columna - self.personaje_columna)
                if 0 <= siguiente_fila < len(self.mapa) and 0 <= siguiente_columna < len(self.mapa[0]) and self.mapa[siguiente_fila][siguiente_columna] in [4, 2]:
                    self.mapa[self.personaje_fila][self.personaje_columna] = 4
                    self.mapa[nueva_fila][nueva_columna] = 0
                    if self.mapa[siguiente_fila][siguiente_columna] == 2:  # Si la siguiente posición de la caja es Meta, convierte al personaje en Personaje_Meta
                        self.mapa[siguiente_fila][siguiente_columna] = 6
                    else:
                        self.mapa[siguiente_fila][siguiente_columna] = 1
                    self.personaje_fila = nueva_fila
                    self.personaje_columna = nueva_columna

    def derecha(self):
        self.movimiento(self.personaje_fila, self.personaje_columna + 1)

    def izquierda(self):
        self.movimiento(self.personaje_fila, self.personaje_columna - 1)

    def arriba(self):
        self.movimiento(self.personaje_fila - 1, self.personaje_columna)

    def abajo(self):
        self.movimiento(self.personaje_fila + 1, self.personaje_columna)

    def jugar(self):
        while True:
            # Imprime el mapa
            self.imprimirMapa()
            # Pide al usuario el movimiento
            movimiento = input("(a: izquierda, d: derecha, w: arriba, s: abajo): ")
            # Moverse a la derecha
            if movimiento == 'd':
                self.derecha()
            # Moverse a la izquierda
            elif movimiento == 'a':
                self.izquierda()
            # Moverse arriba
            elif movimiento == 'w':
                self.arriba()
            # Moverse abajo
            elif movimiento == 's':
                self.abajo()

soko = Soko()
soko.jugar()
