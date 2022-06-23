
from matplotlib import pyplot as plt


def genera_grafica_lineas(eje_x: list, eje_y: list, titulo: str = "", titulo_eje_y: str = ""):
    """
    genera una grafica de lineas a partir de datos dados

    se puede especificar el titulo del eje y el titulo general de la tabla
    """

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(eje_x, eje_y)

    plt.xticks(eje_x, rotation=90)  # Sobre el eje de las X, rota los nombres
    plt.margins(0.1)

    plt.subplots_adjust(bottom=.25)
    plt.grid(True)
    plt.title(titulo)
    ax.set_ylabel(titulo_eje_y)

    plt.show()


def main():
    pass


if __name__ == '__main__':
    main()
