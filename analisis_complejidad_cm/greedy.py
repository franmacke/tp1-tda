from utils import leer_archivo
from collections import deque

def algoritmo(path = None, timestamps = None, transacciones = None):
    if path is None and (timestamps is None or transacciones is None):
        raise ValueError("Se debe proporcionar un archivo o listas de timestamps y transacciones.")

    if path is not None:
        timestamps, transacciones = leer_archivo(path)

    if timestamps is None or transacciones is None:
        raise ValueError("Se deben proporcionar timestamps y transacciones.")

    resultado = []

    sorted_timestamps = sorted(timestamps, key=lambda x: x[0])
    transacciones = deque(sorted(transacciones))

    for index, transaccion in enumerate(transacciones):
        mejor_timestamp = buscar_mejor_timestamp(sorted_timestamps, transaccion)

        if mejor_timestamp is None:
            return "No es el sospechoso correcto"

        resultado.append((transaccion, mejor_timestamp[0], mejor_timestamp[1]))
        sorted_timestamps.remove(mejor_timestamp)

    return sorted(resultado, key=lambda x: x[0])


def buscar_mejor_timestamp(timestamps, transaccion):
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

    ventanas = [((timestamp, error), timestamp + error - transaccion) for timestamp, error in opciones]

    menor_error = min(ventanas, key=lambda x: x[1])

    return menor_error[0][0], menor_error[0][1]


def dentro_de_rango(transaccion, timestamp):
    """
    :param transaccion: int, transaccion a verificar
    :param timestamp: tuple, (timestamp, error)
    """
    return timestamp[0] - timestamp[1] <= transaccion <= timestamp[0] + timestamp[1]
