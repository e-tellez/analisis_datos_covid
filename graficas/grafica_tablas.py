
from matplotlib import pyplot as plt


def genera_tabla(datos: list, nombre_columnas: list):
    """
    Se genera una tabla a partir de:
            Datos = matriz
            nombre_columna = nombres de las columnas
    """

    fig, ax = plt.subplots(figsize=(10, 15))
    ax.table(
        cellText=datos,
        colLabels=nombre_columnas,
        loc='best'
    )

    ax.axis('tight')
    ax.axis('off')

    plt.show()


def main():
    pass


if __name__ == '__main__':
    main()
