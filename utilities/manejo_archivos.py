
import os


def regresa_ruta_archivo():
    """Regresa la ruta del archivo elegido para este ejercicio,
    descargado de: https://datos.covid-19.conacyt.mx/#DownZCSV"""

    ruta_main = os.path.dirname(__file__)
    ruta_archivo = ruta_main + \
        '/../files/' + \
        'Casos_Diarios_Estado_Nacional_Confirmados_20220606.csv'
    return ruta_archivo


def lee_archivo(ruta_archivo: str):
    """lee el archivo de la ruta que se especifica"""

    datos = []
    with open(ruta_archivo, 'r') as f:
        lines = f.readlines()

    for line in lines:
        columnas = line.rstrip('\n').split(',')
        datos.append(columnas)
    return datos


def main():
    pass


if __name__ == '__main__':
    main()
