from auxiliares import submenu_dnis, submenu_anios


def main():
    while True:
        print('\n#############################################')
        print('Bienvenido al TP integrador de matemáticas')
        print('Integrantes: Gaspar Inacio, Francisco Gutierrez')
        print('#############################################')
        print('\nA. Operaciones con DNIs\nB. Operaciones con años de nacimiento')
        opc = input('\nIngrese una opción o "X" para salir: ').lower()

        if opc == 'x':
            print('\nSaliendo...')
            break
        elif opc == 'a':
            submenu_dnis()
        elif opc == 'b':
            submenu_anios()
        else:
            print('\nOpcion incorrecta, reintente nuevamente')
            continue


if __name__ == '__main__':
    main()
