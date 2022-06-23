
from utilities.manejo_menus import muestra_menu_principal
from utilities.manejo_opciones import pide_verifica_opcion


def main():
    try:
        muestra_menu_principal()
        pide_verifica_opcion()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
