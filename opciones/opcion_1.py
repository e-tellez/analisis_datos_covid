
from graficas.grafica_lineas import genera_grafica_lineas
from graficas.grafica_tablas import genera_tabla

from utilities.manejo_datos import dame_contagios_maximo_estado
from utilities.manejo_datos import dame_estados
from utilities.manejo_datos import dame_estado_fecha_dias_maximos_contagios

from utilities.manejo_archivos import lee_archivo
from utilities.manejo_archivos import regresa_ruta_archivo


def mas_casos_nivel_nacional():
    """
        Opción 1: “Día con más casos a nivel nacional”

    1. Para cada estado, el sistema debe obtener la fecha en la que se tuvo el máximo de contagios confirmados.

    2. El sistema deberá mostrar una tabla con las columnas:
        a. Estado
        b. Fecha
            i. Día en el cual se encuentra el máximo
        c. Máximo
            i. Número de contagios máximo en todo el periodo
        d. Ejemplo

    3. El sistema deberá mostrar una gráfica de líneas, tal que el eje “x” sea el estado y el eje “y” el máximo de cada estado.
        a. Solo en la parte de la gráfica, se deberá eliminar de los datos el registro “Nacional”, ya que el número es el acumulado de todos los estados y no tiene sentido de comparación contra los estados.
        b. Ejemplo de la gráfica:

    4. Una vez que el usuario cierre la gráfica y tabla de datos, el sistema lo deberá regresar al “Menú de opciones”
    """

    ruta_archivo = regresa_ruta_archivo()

    nombre_columnas = ['Estado', 'Fecha', 'Máximo']

    datos = lee_archivo(ruta_archivo)
    dias_maximos_contagios = dame_estado_fecha_dias_maximos_contagios(datos)

    genera_tabla(dias_maximos_contagios, nombre_columnas)

    eje_x = dame_estados(datos)
    eje_y = dame_contagios_maximo_estado(dias_maximos_contagios)

    genera_grafica_lineas(
        eje_x, eje_y,
        "Máximo # de contagios por Estado",
        "Contagios")


def main():
    pass


if __name__ == '__main__':
    main()
