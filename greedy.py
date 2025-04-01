from utils import leer_archivo
from collections import deque

def algoritmo(path):
    resultado = []
    timestamps, transacciones = leer_archivo(path)

    sorted_timestamps = sorted(timestamps, key=lambda x: x[0])
    transacciones = deque(sorted(transacciones))

    for index, transaccion in enumerate(transacciones):
        mejor_timestamp = buscar_mejor_timestamp(sorted_timestamps, transaccion, index)

        if mejor_timestamp is None:
            return []

        resultado.append((transaccion, mejor_timestamp[0], mejor_timestamp[1]))
        sorted_timestamps.remove(mejor_timestamp)

    return sorted(resultado, key=lambda x: x[0])


def buscar_mejor_timestamp(timestamps, transaccion, index):
    """
    Busca el mejor timestamp para una transacción dada.

    :param timestamps: list, lista de timestamps ordenada por timestamp.
    :param transaccion: int, transacción a buscar.

    :return: tuple, el mejor timestamp y su error.
    """

    opciones = []
    for timestamp, error in timestamps:
        if dentro_de_rango(transaccion, (timestamp, error)):
            opciones.append((timestamp, error))

    if not opciones:
        return None

    menor_error = min(opciones, key=lambda x: x[0] + x[1] - transaccion)

    return menor_error


def dentro_de_rango(transaccion, timestamp):
    """
    :param transaccion: int, transaccion a verificar
    :param timestamp: tuple, (timestamp, error)
    """
    return timestamp[0] - timestamp[1] <= transaccion <= timestamp[0] + timestamp[1]
