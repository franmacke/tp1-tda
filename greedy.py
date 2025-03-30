from utils import leer_archivo


def algoritmo(path):
    resultado = []
    timestamps, transacciones = leer_archivo(path)

    sorted_timestamps = sorted(timestamps, key=lambda x: x[1], reverse=False)     # Acá estoy ordenando por la menor ventana de error


    for i in range(len(sorted_timestamps)):
        transaccion = buscar_transaccion_mas_cercana(transacciones, sorted_timestamps[i][0])

        if dentro_de_rango(transaccion, sorted_timestamps[i]):
            resultado.append((transaccion, sorted_timestamps[i][0], sorted_timestamps[i][1]))
            transacciones.remove(transaccion)
        else:
            return []

    return resultado


def buscar_transaccion_mas_cercana(transacciones, timestamp):
    """
    :param transacciones: list, lista de transacciones ordenadas
    :param timestamp: int, timestamp a buscar
    :return: int, transaccion más cercana al timestamp
    """

    izquierda, derecha = 0, len(transacciones) - 1
    mejor_candidato = transacciones[0]

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if abs(transacciones[medio] - timestamp) < abs(mejor_candidato - timestamp):
            mejor_candidato = transacciones[medio]

        if transacciones[medio] == timestamp:
            return transacciones[medio]

        if transacciones[medio] < timestamp:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return mejor_candidato



def dentro_de_rango(transaccion, timestamp):
    """
    :param transaccion: int, transaccion a verificar
    :param timestamp: tuple, (timestamp, error)
    """
    return timestamp[0] - timestamp[1] <= transaccion <= timestamp[0] + timestamp[1]
