
from graficas.grafica_barras import genera_grafica_barras
from graficas.grafica_tablas import genera_tabla

from utilities.manejo_archivos import lee_archivo
from utilities.manejo_archivos import regresa_ruta_archivo

from utilities.manejo_datos import dame_solo_porcentajes
from utilities.manejo_datos import dame_estados
from utilities.manejo_datos import dame_porcentaje_contagios
from utilities.manejo_datos import dame_contagios_acumulados_por_estado


def casos_confirmados_por_poblacion():
    """
    Opción: “% Casos confirmados de acuerdo a la población”
        1. Para cada estado, el sistema debe calcular:
            a. La suma acumulada de contagios confirmados
            b. El porcentaje correspondiente de acuerdo al total de la población de dicho estado.
        2. El sistema deberá mostrar una tabla con las columnas:
            a. Estado
            b. Población
            c. # Contagiados
            d. Porcentaje
        3. Ejemplo de tabla:

        5. El sistema deberá obtener una gráfica de barras tal que el eje “x” sea el estado y el eje “y”
            sea el porcentaje calculado.
            a. Ejemplo de la gráfica:
    """

    ruta_archivo = regresa_ruta_archivo()
    datos = lee_archivo(ruta_archivo)

    contagios_acumulados_por_estado = dame_contagios_acumulados_por_estado(
        datos)

    porcentaje_contagios = dame_porcentaje_contagios(
        contagios_acumulados_por_estado)

    columnas = ['Estado', 'Población', '# Contagiados', 'Porcentaje']
    genera_tabla(porcentaje_contagios, columnas)

    porcentajes = dame_solo_porcentajes(porcentaje_contagios)
    estados = dame_estados(datos)
    estados.append("Nacional")

    genera_grafica_barras(estados,
                          porcentajes,
                          "% Contagios respecto a la población",
                          "Porcentaje")


def main():
    pass


if __name__ == '__main__':
    main()
