
import os


def muestra_menu_principal(mensaje="") -> str:
    """
    Desc:
        Muestra el menu principal y limpia la pantalla

    Arg:
        Un string en caso de que quieras imprimir
    """

    os.system('clear')
    if mensaje:
        print(mensaje)

    print("*"*65)
    print("**" + "**".rjust(63, " "))
    print("**  " + "1. Dia con mas casos a nivel nacional" + "**".rjust(24, " "))
    print("**  " + "2. % Casos confirmados de acuerdo a la población" +
          "**".rjust(13, " "))
    print("**  " + "3. Series de tiempo" + "**".rjust(42, " "))
    print("**  " + "4. Salir" + "**".rjust(53, " "))
    print("**" + "**".rjust(63, " "))
    print("*"*65)


def muestra_menu_opcion_3(mensaje="") -> str:
    """
    Desc:
        Muestra el menu principal y limpia la pantalla

    Arg:
        Un string en caso de que quieras imprimir
    """

    os.system('clear')
    if mensaje:
        print(mensaje)

    print("*"*65)
    print("**" + "**".rjust(63, " "))
    print("**En lugar puedes teclear el nombre de algun estado o Nacional **")
    print("**" + "**".rjust(63, " "))
    print("*"*65)


def main():
    pass


if __name__ == '__main__':
    main()
