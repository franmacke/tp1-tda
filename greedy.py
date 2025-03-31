from utils import leer_archivo
from collections import deque

def algoritmo(path):
    resultado = []
    timestamps, transacciones = leer_archivo(path)


    sorted_timestamps = sorted(timestamps, key=lambda x: x[0] + x[1])
    mapped_timestamps = [(timestamp, error, timestamp + error) for timestamp, error in sorted_timestamps]
    transacciones = deque(sorted(transacciones))

    for timestamp, error in sorted_timestamps:
        if not transacciones:
            return []

        transaccion_actual = transacciones.popleft()

        if not dentro_de_rango(transaccion_actual, (timestamp, error)):
            return []

        resultado.append((transaccion_actual, timestamp, error))

    return sorted(resultado, key=lambda x: x[0])

def buscar_transaccion_mas_cercana(transacciones, timestamp):
    """
    Encuentra la transacción más cercana al timestamp dado usando búsqueda binaria.

    :param transacciones: list, lista ordenada de timestamps de transacciones.
    :param timestamp: int, timestamp a buscar.
    :return: int, la transacción más cercana al timestamp.
    """
    if not transacciones:
        return None

    izquierda, derecha = 0, len(transacciones) - 1
    mejor_candidato = transacciones[0]

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = transacciones[medio]

        if actual == timestamp:
            return actual

        if abs(actual - timestamp) < abs(mejor_candidato - timestamp):
            mejor_candidato = actual

        if actual < timestamp:
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
