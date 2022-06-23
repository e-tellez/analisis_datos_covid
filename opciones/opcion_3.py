
from graficas.grafica_lineas import genera_grafica_lineas

from utilities.manejo_archivos import lee_archivo
from utilities.manejo_archivos import regresa_ruta_archivo

from utilities.manejo_datos import dame_indice_por_opcion
from utilities.manejo_datos import dame_contagios_por_mes
from utilities.manejo_datos import dame_meses
from utilities.manejo_datos import dame_entidades

from utilities.manejo_menus import muestra_menu_opcion_3


def series_tiempo():
    """
    1. El sistema debe solicitar el nombre del lugar, puede ser el “nombre del estado” o escribir “Nacional”.
        a. Ejemplo de captura:  Lugar -> PUEBLA
    2. El sistema debe validar que el nombre sea correcto, es decir, que pertenezca a la base de datos.
    3. En caso de escribir un nombre incorrecto, el sistema deberá mostrar el mensaje “Lugar inválido” y volver a solicitar el nombre del lugar.

    4. Solo con la información del lugar seleccionado por el usuario, el sistema debe:
        a. Obtener la lista de meses que existe en la información
            i. Por ejemplo las fechas: 18-02-2020,19-02-2020,20-02-2020... corresponden al mes: “02-2020”
        b. Calcular la suma de casos confirmados por mes (solo para el lugar seleccionado por el usuario) y dejar la información en una lista.
        c. Graficar la serie de datos correspondiente
    """

    ruta = regresa_ruta_archivo()
    datos = lee_archivo(ruta)

    estados = dame_entidades(datos)
    meses = dame_meses(datos)

    muestra_menu_opcion_3()

    while True:
        opcion = input("\nLugar -> ")

        if opcion in estados:
            # REGRESA EL INDICE -1 DEL ESTADO QUE SE DA
            indice_estado = dame_indice_por_opcion(opcion, estados)

            fechas_contagios_mes = [
                # primer valor = las fechas a partir del 3er indice para saltar: clave, poblacion y estado
                datos[0][3:],
                # segundo valor = todos los contagios del estado seleccionado
                datos[indice_estado][3:]
            ]

            contagios_por_meses = dame_contagios_por_mes(
                fechas_contagios_mes,
                meses
            )

            eje_x = []
            eje_y = []

            for i in range(len(contagios_por_meses)):
                # print(i)
                eje_x.append(contagios_por_meses[i][1])
                eje_y.append(contagios_por_meses[i][0])

            genera_grafica_lineas(
                eje_x, eje_y,
                'Serie de tiempo mensual para ' + estados[indice_estado-1],
                'Contagios'
                )
            break

        else:
            muestra_menu_opcion_3("Lugar inválido")


def main():
    pass


if __name__ == '__main__':
    main()
