
def leer_archivo(path) -> tuple:
    """
    :param path: str, path del archivo a leer. Puede ser absoluto o relativo.
    :return: tuple, (timestamps, transacciones)
    """
    with open(path, 'r') as f:
        f.readline()

        n = int(f.readline())

        timestamps = []
        for i in range(n):
            timestamp, error = f.readline().strip().split(',')
            timestamps.append((int(timestamp), int(error)))

        transacciones = []
        for i in range(n):
            transaccion = f.readline().strip()
            transacciones.append(int(transaccion))

    return timestamps, transacciones
