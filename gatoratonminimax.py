import random
import time

filas = 5
columnas = 5

tablero = [[0] * columnas for _ in range(filas)]


gato_fila = gato_columna = raton_fila = raton_columna = None 

def colocar_gato_y_raton():
    
    global gato_fila, gato_columna, raton_fila, raton_columna
    while True:

        gato_fila = random.randint(0, filas - 1)
        gato_columna = random.randint(0, columnas - 1)
        raton_fila = random.randint(0, filas - 1)
        raton_columna = random.randint(0, columnas - 1)

        if (gato_fila != raton_fila) or (gato_columna != raton_columna):
            break

    tablero[gato_fila][gato_columna] = 1
    tablero[raton_fila][raton_columna] = 2

def imprimir_tablero():
    simbolos = {0:".", 1: "G", 2:"R"}
    for fila in tablero:
        print(" ".join(simbolos[c] for c in fila))

def imprimir_tablero_con_delay():
    simbolos = {0: ".", 1: "G", 2: "R"}
    for fila in tablero:
        print(" ".join(simbolos[c] for c in fila))
        time.sleep(1.5)

def evaluar_tablero():
    global gato_fila, gato_columna, raton_fila, raton_columna
    
    distancia = abs(gato_fila - raton_fila) + abs(gato_columna - raton_columna)
    
    if distancia == 0:
        return -1000
    
    return distancia

def minimax(profundidad, maximizando_raton):
    global gato_fila, gato_columna, raton_fila, raton_columna


    if profundidad == 0 or evaluar_tablero() == -1000:

        return evaluar_tablero()

    if maximizando_raton:

        mejor_puntuacion = float('-inf') 

        for mov in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nueva_fila = raton_fila + mov[0]
            nueva_columna = raton_columna + mov[1]

            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:

                raton_fila_original, raton_columna_original = raton_fila, raton_columna
                tablero[raton_fila][raton_columna] = 0
                raton_fila, raton_columna = nueva_fila, nueva_columna
                tablero[raton_fila][raton_columna] = 2
                puntuacion = minimax(profundidad - 1, False)
                tablero[raton_fila][raton_columna] = 0
                raton_fila, raton_columna = raton_fila_original, raton_columna_original
                tablero[raton_fila][raton_columna] = 2
                mejor_puntuacion = max(mejor_puntuacion, puntuacion)
        return mejor_puntuacion
    else:

        mejor_puntuacion = float('inf')

        for mov in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nueva_fila = gato_fila + mov[0]
            nueva_columna = gato_columna + mov[1]
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                gato_fila_original, gato_columna_original = gato_fila, gato_columna
                tablero[gato_fila][gato_columna] = 0
                gato_fila, gato_columna = nueva_fila, nueva_columna
                tablero[gato_fila][gato_columna] = 1
                puntuacion = minimax(profundidad - 1, True)
                tablero[gato_fila][gato_columna] = 0
                gato_fila, gato_columna = gato_fila_original, gato_columna_original
                tablero[gato_fila][gato_columna] = 1
                mejor_puntuacion = min(mejor_puntuacion, puntuacion)
        return mejor_puntuacion


def mover_raton_inteligente():


    global raton_fila, raton_columna
    mejor_movimiento = None
    mejor_puntuacion = float('-inf')

    for mov in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nueva_fila = raton_fila + mov[0]
        nueva_columna = raton_columna + mov[1]
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
            raton_fila_original, raton_columna_original = raton_fila, raton_columna
            tablero[raton_fila][raton_columna] = 0
            raton_fila, raton_columna = nueva_fila, nueva_columna
            tablero[raton_fila][raton_columna] = 2
            puntuacion = minimax(3, False)
            tablero[raton_fila][raton_columna] = 0
            raton_fila, raton_columna = raton_fila_original, raton_columna_original
            tablero[raton_fila][raton_columna] = 2
        
            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_movimiento = mov


    if mejor_movimiento:
        nueva_fila = raton_fila + mejor_movimiento[0]
        nueva_columna = raton_columna + mejor_movimiento[1]
        tablero[raton_fila][raton_columna] = 0
        raton_fila, raton_columna = nueva_fila, nueva_columna
        tablero[raton_fila][raton_columna] = 2

def mover_gato_inteligente():

    global gato_fila, gato_columna
    mejor_movimiento = None
    mejor_puntuacion = float('inf')

    for mov in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nueva_fila = gato_fila + mov[0]
        nueva_columna = gato_columna + mov[1]
        if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:

            gato_fila_original, gato_columna_original = gato_fila, gato_columna
            tablero[gato_fila][gato_columna] = 0
            gato_fila, gato_columna = nueva_fila, nueva_columna
            tablero[gato_fila][gato_columna] = 1

            puntuacion = minimax(3, True)

            tablero[gato_fila][gato_columna] = 0
            gato_fila, gato_columna = gato_fila_original, gato_columna_original
            tablero[gato_fila][gato_columna] = 1

            if puntuacion < mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_movimiento = mov


    if mejor_movimiento:
        nueva_fila = gato_fila + mejor_movimiento[0]
        nueva_columna = gato_columna + mejor_movimiento[1]
        tablero[gato_fila][gato_columna] = 0
        gato_fila, gato_columna = nueva_fila, nueva_columna
        tablero[gato_fila][gato_columna] = 1

def jugar():
    turnos_maximos = 10
    turnos = 0
    victoria = None

    while turnos < turnos_maximos:
        print(f"\n Turnos{turnos + 1}")
        print("Turno del Raton:")
        mover_raton_inteligente()
        imprimir_tablero()
        time.sleep(1)

        if gato_fila == raton_fila and gato_columna == raton_columna:
            victoria = "Gato"
            break
        print("Turno del Gato:")
        mover_gato_inteligente()
        imprimir_tablero()
        time.sleep(1)

        if gato_fila == raton_fila and gato_columna == raton_columna:
            victoria= "Gato"
            break 
        turnos +=1
    
    if not victoria and turnos == turnos_maximos:
            victoria = "Raton"

    if victoria == "Raton":
            print("\n¡El ratón ha ganado!")
    else:
            print("\n¡El gato ha ganado!")
        

colocar_gato_y_raton()
imprimir_tablero()

jugar()



    