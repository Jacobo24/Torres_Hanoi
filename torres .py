def torres():
    print("Torres de Hanoi")
    print("1. Mover un disco")
    print("2. Mover todos los discos")
    print("3. Salir")
    print("")

    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        mover_disco()
    elif opcion == 2:
        mover_todos()
    elif opcion == 3:
        return
    else:
        print("Opcion invalida")
        torres()