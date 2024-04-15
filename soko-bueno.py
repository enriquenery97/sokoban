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
        
    def mover_derecha(self):
        #PERSONAJE, PISO ->  PISO, PERSONAJE
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 # Donde estaba el personaje se convierte en piso 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 # Donde estaba el piso se coloca el personaje 
            self.personaje_columna += 1 # Se actuliza el personaje 
        #PERSONAJE, CAJA, PISO -> PISO, PERSONAJE, CAJA 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa [self.personaje_fila][self.personaje_columna+ 1 ] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 # Donde estaba elpersonaje se pone un piso 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 # Donde estaba la caja se pone personaje 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1 # onde estaba el piso se coloca una caja 
            self.personaje_columna += 1 #  Se actualiza el personaje
        #PERSONAJE, META -> PISO, PERSONAJE_META
        elif self.mapa[self.personaje_fila][self.personaje_columna ] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna ] = 4 # Donde estaba el personaje se covierte en piso
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 # Donde estaba la meta se convierte en personaje_meta
            self.personaje_columna += 1 # Se actuliza el personaje
        #PERSONAJE_META, PISO -> META, PERSONAJE 
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa [self.personaje_fila][self.personaje_columna + 1] == 4: 
            self.mapa[self.personaje_fila][self.personaje_columna] = 2 # Donde estaba el personaje_meta se convierte en meta 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 # Donde estaba piso se convierte en personaje 
            self.personaje_columna += 1 # Se actuliza el personaje 
        #PERSONAJE, CAJA, META -> PISO, PERSONAJE, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1 ] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 # Donde estaba el perosonaje se convierte en piso 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 # Donde estaba la caja se convierte en personaje 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 # Donde estaba la meta se convierte en caa meta 
            self.personaje_columna += 1 # Se actuliza el perosnaje 
        #PERSONAJE, CAJA_META, PISO ->  PISO, PERSONAJE_META, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 # Donde estaba personaje se convierte en piso 
            self.mapa[self.personaje_fila][self.personaje_columna + 1 ] = 5 # Donde estaba caja_meta se convierte en personaje_meta 
            self.mapa[self.personaje_fila][self.personaje_columna + 2 ] = 1 # Donde estaba piso se covierte en caja 
            self.personaje_columna += 1 # Se actuliza el personaje 
        #PERSONAJE, CAJA_META, META -> PISO, PERSONAJE_META, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1 ] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 4 # Donde estaba el personaje se convierte en piso 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 # Donde estaba caja_meta se convierte personaje_meta 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 # Donde estaba meta se convierte en caja_meta 
            self.personaje_columna += 1 # Se actuaiza el personaje 
        #PERSONAJE_META, META -> META, PERSONAJE_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1]  == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2 # Donde estaba el perosnaje_meta se convierte en meta 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 # Donde estaba meta se convierte en personaje_meta 
            self.personaje_columna += 1 # Se actualiza el personaje 
        #PERSONAJE_META, CAJA, PISO -> META, PERSONAJE, CAJA
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2 # Donde estaba el perosnaje_meta se convierte en meta 
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 # Donde estaba la caja se convierte en caja 
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1 # Donde estaba el piso se convierte en caja 
            self.personaje_columna += 1 # Se actualiza el personaje 
        #PERSONAJE_META, CAJA, META -> META, PERSONAJE, CAJA_META
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2 ] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna] = 2 #
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 #
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 #
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


    def jugar(self):
        while True:
            self.imprimirMapa()
            movimiento = input("Selecciona el movimiento (d: derecha, a: izquierda, w: arriba, s: abajo, exit: para salir del juego): ")
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
    def nivel_finalizado(self):
        for fila in self.mapa:
         for elemento in fila:
             if elemento == 1: #si hay cajas en el mapa sigue el juego 
                 return False
        return True #si ya no hay cajas en el juego (patida) finaliza el juego 

# Crea una instancia del juego y comienzar a jugar
soko = soko()
soko.jugar()
