
def dame_contagios_maximo_estado(datos: list):
    """
    Retornará solamente el número máximo de contagios por estado y se
    quita el último valor que corresponde a los contagios nacionales
    """

    contagios_maximos_estado = []
    for i in range(len(datos)-2):
        contagios_maximos_estado.append(datos[i][2])
    return contagios_maximos_estado


def dame_estados(datos: list):
    """
    Se obtienen solamente los estados del set de datos y se les quitan las comillas que venían
    se quita el último valor que corresponde a contagios nacionales
    """

    estados = []
    for i in range(1, len(datos)-1):
        dato = datos[i][2].replace('"', "")
        estados.append(dato)
    return estados


def dame_meses(datos: list):
    """
    Regresa los meses de acuerdo a los datos entregdos
    """

    dias = []
    meses_repetidos = []
    meses = []

    for i in range(3, len(datos[0])):
        dias.append(datos[0][i].split('-'))

    for i in range(0, len(dias)):
        fraccion = []
        for j in range(0, len(dias[i])):
            if j == 1 or j == 2:
                fraccion.append(dias[i][j])

        meses_repetidos.append('-'.join(fraccion))

    for i in range(len(meses_repetidos)):
        if meses_repetidos[i] != meses_repetidos[i-1]:
            meses.append(meses_repetidos[i])
    return meses


def dame_indice_por_opcion(opcion: str, meses: list):
    """
    regresa el indice de la opcion dada para poder identificar el estado
    """

    for i in range(len(meses)):
        if opcion == meses[i]:
            index = i+1
    return index


def dame_contagios_por_mes(fechas_contagios_mes: list, meses: list) -> list:
    """
    Calcula la cantidad de contagios por mes

    Recibe un array con [[fechas], [contagios]] y otro con los meses transcurridos
    para poder comprobar si las fechas pertenecen al mes y asi sumarlas
    """
    contagios_por_meses = []

    for i in range(len(meses)):  # recorre los meses (como 29)
        contagios_del_mes = 0

        # recorre todos los dias (832)
        for k in range(len(fechas_contagios_mes[1])):

            fecha_corriente = fechas_contagios_mes[0][k].split('-')
            mes_corriente = ('-').join([
                fecha_corriente[1],
                fecha_corriente[2]
            ])

            if meses[i] == mes_corriente:
                contagios_del_mes += int(fechas_contagios_mes[1][k])

        contagios_por_meses.append([
            contagios_del_mes,
            meses[i]]
        )
    return contagios_por_meses


def dame_entidades(datos: list):
    """
    Se obtienen solamente los estados del set de datos y se les quitan las comillas que venían
    se quita el último valor que corresponde a contagios nacionales
    """

    estados = []
    for i in range(1, len(datos)):
        dato = datos[i][2].replace('"', "")
        estados.append(dato)
    return estados


def quita_clave_poblacion(datos: list):
    """
    Se quita la clave y la población de cada entidad, también se cambia a int los valores de contagios sin contar el
    primer renglón que es el de las fechas
    """

    datos_sin_clave_poblacion = [datos[0][2:]]

    for i in range(1, len(datos)):
        renglon = []
        for j in range(len(datos[i])):
            if i > 0 and j > 1:
                if j == 2:
                    renglon.append(datos[i][j])
                else:
                    renglon.append(int(datos[i][j]))

        datos_sin_clave_poblacion.append(renglon)

    return datos_sin_clave_poblacion


def quita_clave_fecha(datos: list):
    """
    Se quita la clave y la fecha del set de datos
    """

    datos_sin_clave_fecha = []
    for i in range(1, len(datos)):
        renglon = []
        for j in range(len(datos[i])):
            if j > 0:
                if j == 2:
                    renglon.append(datos[i][j])
                else:
                    renglon.append(int(datos[i][j]))
        datos_sin_clave_fecha.append(renglon)

    return datos_sin_clave_fecha


def dame_estado_fecha_dias_maximos_contagios(datos: list):
    """
    En esta funcion se manda llamar quita_clave_poblacion para poder quitar la clave de entidad y el # de poblacion
    En el ciclo for se saca el máximo de contagios según la entidad y después se identifica el día donde se registró
        esa cantidad de contagios para añadirla al arreglo dias_mayor_contagio
    """

    datos_sin_clave_poblacion = quita_clave_poblacion(datos)

    dias_mayor_contagio = []

    for i in range(1, len(datos_sin_clave_poblacion)):
        cantidad_mayor_contagios = max(datos_sin_clave_poblacion[i][1:])

        for j in range(1, len(datos_sin_clave_poblacion[i])):

            if str(datos_sin_clave_poblacion[i][j]) == str(cantidad_mayor_contagios):

                dia_mas_contagios = datos_sin_clave_poblacion[0][j]

                dias_mayor_contagio.append([
                    datos_sin_clave_poblacion[i][0],  # agrega el estado
                    dia_mas_contagios,  # agrega el día
                    cantidad_mayor_contagios  # agrega el numero de contagios
                ])

    return dias_mayor_contagio


def dame_contagios_acumulados_por_estado(datos: list):
    """
    se arrojan los contagios acumulados en un array que devuelve estado/acumulacion/poblacion
    """

    datos_sin_clave_fecha = quita_clave_fecha(datos)

    contagios_acumulados_por_estado = []

    for i in range(len(datos_sin_clave_fecha)):
        acumulacion = 0
        renglon = []
        for j in range(2, len(datos_sin_clave_fecha[i])):
            if j > 0:
                acumulacion += datos_sin_clave_fecha[i][j]

        contagios_acumulados_por_estado.append([
            datos_sin_clave_fecha[i][1],  # estado
            datos_sin_clave_fecha[i][0],  # poblacion
            acumulacion  # numero de contagiados
        ])

    return contagios_acumulados_por_estado


def dame_porcentaje_contagios(datos: list):
    """
    Esta funcion saca el porcentaje de poblacion infectada y la añade al array ya existente
    """

    porcentaje = 0
    for i in range(len(datos)):
        porcentaje = round(datos[i][2]/datos[i][1] * 100, 2)
        datos[i].append(porcentaje)

    return datos


def dame_solo_porcentajes(datos: list):
    """devuelve una lista de solo el porcentaje de contagios vs poblacion"""

    porcentajes = []
    for i in range(len(datos)):
        porcentajes.append(datos[i][3])

    return porcentajes


def main():
    pass


if __name__ == '__main__':
    main()
