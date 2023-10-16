from torres import Torre

def getTablero(n):
    torre_A = Torre()
    torre_B = Torre()
    torre_C = Torre()

    for disco in range(n, 0, -1):
        torre_A.push(disco)

    return (torre_A, torre_B, torre_C)

def solve(tablero, n, origen, destino, auxiliar):
    movimientos = []

    def torres_hanoi(n, origen, destino, auxiliar):
        if n == 1:
            disco = origen.pop()
            destino.push(disco)
            movimiento = f"D{disco} from T{origen} to T{destino}"
            movimientos.append(movimiento)
        else:
            torres_hanoi(n - 1, origen, auxiliar, destino)
            disco = origen.pop()
            destino.push(disco)
            movimiento = f"D{disco} from T{origen} to T{destino}"
            movimientos.append(movimiento)
            torres_hanoi(n - 1, auxiliar, destino, origen)

    torres_hanoi(n, tablero[0], destino, auxiliar)
    return movimientos

if __name__ == "__main__":
    n = 3  # Número de discos
    tablero = getTablero(n)
    origen, destino, auxiliar = tablero

    print("Estado inicial del tablero:")
    print("Torre A:", origen)
    print("Torre B:", destino)
    print("Torre C:", auxiliar)

    movimientos = solve(tablero, n, origen, destino, auxiliar)

    print("\nLista de movimientos:")
    for movimiento in movimientos:
        print(movimiento)

    print("\nEstado final del tablero:")
    print("Torre A:", origen)
    print("Torre B:", destino)
    print("Torre C:", auxiliar)