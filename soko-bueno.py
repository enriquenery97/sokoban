import os
class soko:
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
            [3, 4, 4, 4, 2, 4, 4, 4, 3],
            [3, 4, 4, 4, 1, 4, 4, 4, 3],
            [3, 4, 4, 4, 0, 4, 4, 4, 3],
            [3, 4, 4, 4, 4, 4, 4, 4, 3],
            [3, 4, 4, 4, 4, 4, 4, 4, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3],
        ]

        # Definimos la posicion inicial del personaje
        self.personaje_columna = 4
        self.personaje_fila = 3


    def imprimirMapa(self):
        #Limpiar pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        for filas in self.mapa:
            print(filas)

    def mover_izquierda(self):
        #PERSONAJE, PISO - PISO, PERSONAJE 
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1
        #PERSONAJE, META - PISO, PERSONAJE_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna -= 1
        #PERSOANJE, CAJA, PISO - PISO, PERSONAJE, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1
        #PERSONAJE, CAJA, META - PISO, PERSONAJE, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1]  = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2]  = 6
            self.personaje_columna -= 1
        #PERSONAJE, CAJA_META, PISO - PISO, PERSONAJE_META, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1
        
        #PERSONAJE, CAJA_META, META - PISO PERSONAJE_META, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
        #PERSONAJE_META, PISO - META, PERSONAJE
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1
        #PERSONAJE_META, META - META, PERSONAJE_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna -= 1
        #PERSONAJE_META, CAJA, PISO - META, PERSONAJE, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1
        #PERSONAJE_META, CAJA, META - META, PERSONAJE, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
        #PERSONAJE_META, CAJA_META, PISO - META, PERSONAJE_META, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.personaje_columna -= 1
        #PERSONAJE_META, CAJA_META, META - META, PERSONAJE_META, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
    def mover_arriba(self):
        #PERSONAJE, PISO - PISO, PERSONAJE
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] =0
            self.personaje_fila -=1
        #PERSONAJE, META - PISO, PERSONAJE_META 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna ] = 5
            self.personaje_fila -=1
        #PERSONAJE, CAJA, PISO - PISO, PERSONAJE, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -=1
        #PERSONAJE, CAJA, META - PISO, PERSONAJE, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -=1
        #PERSONAJE, CAJA_META, META - PISO, PERSONAJE_META, CAJA_META   
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -=1
        #PERSONAJE, CAJA_META, META - PISO, PERSONAJE_META, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -=1
        #PERSONAJE_META, PISO - META, PERSONAJE
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.personaje_fila -=1
        #PERSONAJE_META, META - META, PERSNAJE_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.personaje_fila -=1
        #PERSONAJE_META, CAJA, PISO - META, PERSONAJE, CAJA 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -=1
        #PERONAJE_META, CAJA, META - META, PERSONAJE, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -=1
        #PERSONAJE_META, CAJA_META, PISO - META, PERSONAJE_META, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.personaje_fila -=1
        #PERSONAJE_META, CAJA_META, META - META, PERSONAJE_META, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -=1
        
    def mover_derecha(self):
        #PERSONAJE, PISO ->  PISO, PERSONAJE
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0  
            self.personaje_columna += 1 
        #PERSONAJE, CAJA, PISO -> PISO, PERSONAJE, CAJA 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa [self.personaje_fila][self.personaje_columna+ 1 ] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4  
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1 
            self.personaje_columna += 1 
        #PERSONAJE, META -> PISO, PERSONAJE_META
        elif self.mapa[self.personaje_fila][self.personaje_columna ] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna ] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 
            self.personaje_columna += 1 
        #PERSONAJE_META, PISO -> META, PERSONAJE 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa [self.personaje_fila][self.personaje_columna + 1] == 4: 
            self.mapa[self.personaje_fila][self.personaje_columna] = 2  
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
            self.personaje_columna += 1  
        #PERSONAJE, CAJA, META -> PISO, PERSONAJE, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1 ] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 
            self.personaje_columna += 1 
        #PERSONAJE, CAJA_META, PISO ->  PISO, PERSONAJE_META, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 5 
            self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 1 
            self.personaje_columna += 1 
        #PERSONAJE, CAJA_META, META -> PISO, PERSONAJE_META, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1 ] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 
            self.personaje_columna += 1 
        #PERSONAJE_META, META -> META, PERSONAJE_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1]  == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 
            self.personaje_columna += 1 
        #PERSONAJE_META, CAJA, PISO -> META, PERSONAJE, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna += 1  
        #PERSONAJE_META, CAJA, META -> META, PERSONAJE, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1 #
        #PERSONAJE_META, CAJA_META, PISO -> META, PERSONAJE_META, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.personaje_columna += 1
        #PERSONAJE_META, CAJA_META, META -> META, PERSONAJE_META, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1    
        
    def mover_abajo(self):
        #PERSONAJE, PISO - PISO, PERSONAJE
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] =0
            self.personaje_fila +=1
        #PERSONAJE, META - PISO, PERSONAJE_META 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna ] = 5
            self.personaje_fila +=1
        #PERSONAJE, CAJA, PISO - PISO, PERSONAJE, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila +=1
        #PERSONAJE, CAJA, META - PISO, PERSONAJE, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila +=1
        #PERSONAJE, CAJA_META, PISO - PISO, PERSONAJE_META, CAJA   
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila +=1
        #PERSONAJE, CAJA_META, META - PISO, PERSONAJE_META, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila +=1
        #PERSONAJE_META, PISO - META, PERSONAJE
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.personaje_fila +=1
        #PERSONAJE_META, META - META, PERSNAJE_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.personaje_fila +=1
        #PERSONAJE_META, CAJA, PISO - META, PERSONAJE, CAJA 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila +=1
        #PERONAJE_META, CAJA, META - META, PERSONAJE, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila +=1
        #PERSONAJE_META, CAJA_META, PISO - META, PERSONAJE_META, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.personaje_fila +=1
        #PERSONAJE_META, CAJA_META, META - META, PERSONAJE_META, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila +=1

    def verificar_nivel_completado(self):
        for fila in self.mapa:
            for elemento in fila:
                if elemento == 1:
                    return False
        


    def jugar(self):
        while True:
            self.imprimirMapa()
            movimiento = input("Selecciona un movimiento (w:arriba, s:abajo, d:derecha y a:izquierda): ")
            if movimiento == 'd':
                self.mover_derecha()
            elif movimiento == 'a':
                self.mover_izquierda()
            elif movimiento == 'w':
                self.mover_arriba()
            elif movimiento == 's':
                self.mover_abajo()
            elif movimiento == 'exit':
                exit()
            if self.verificar_nivel_completado():
                print("¡Felicidades! ¡Has terminado el nivel!")
                break
# Crea una instancia del juego
soko = soko()
soko.jugar()
