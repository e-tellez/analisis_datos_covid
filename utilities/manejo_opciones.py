from utilities.manejo_menus import muestra_menu_principal

from opciones.opcion_1 import mas_casos_nivel_nacional as opcion_1
from opciones.opcion_2 import casos_confirmados_por_poblacion as opcion_2
from opciones.opcion_3 import series_tiempo as opcion_3


def pide_verifica_opcion():
    """
    Desc:
        Pedira una opcion del menu y en caso de que sea incorrecta,
        sarrojara mensaje y vuelve a pedir opcion valida
    """

    opciones = ["1", "2", "3", "4"]

    while True:
        opcion = input("\nOpcion: ")

        if opcion in opciones:
            if opcion == "1":
                opcion_1()
                muestra_menu_principal()

            elif opcion == "2":
                opcion_2()
                muestra_menu_principal()

            elif opcion == "3":
                opcion_3()
                muestra_menu_principal()

            elif opcion == "4":
                print("Salida")
                break

        else:
            muestra_menu_principal("Opción inválida")


def main():
    pass


if __name__ == "__main__":
    main()
