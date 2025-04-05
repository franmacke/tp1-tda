from random import randint

class Generador:
    def __init__(self, n, error = None):
        self.n = n
        self.error = error if error else n

    def generar(self):
        return (self.generar_timestamps(), self.generar_transacciones())

    def generar_transacciones(self):
        return [randint(1, 100) for _ in range(self.n)]

    def generar_timestamps(self):
        return [(randint(1, 100), randint(1, self.error)) for _ in range(self.n)]

    @staticmethod
    def generar_caso_es_sospechoso(n, error, timestamp_interval=(1, 100)):
        """
        Genera un caso donde es sospechoso.
        """
        timestamps = [(randint(timestamp_interval[0], timestamp_interval[1]), randint(1, error)) for _ in range(n)]
        timestamps.sort(key=lambda x: x[0])

        transacciones = [timestamps[i][0] + timestamps[i][1] - 1 for i in range(n)]


        return (timestamps, transacciones)

    @staticmethod
    def generar_caso_no_es_sospechoso(n, error, timestamp_interval=(1, 100)):
        """
        Genera un caso donde no es sospechoso.
        """
        timestamps = [(randint(timestamp_interval[0], timestamp_interval[1]), randint(1, error)) for _ in range(n)]
        timestamps.sort(key=lambda x: x[0])

        randint_index = randint(0, n - 1)

        transacciones = [timestamps[i][0] + timestamps[i][1] for i in range(n)]

        transacciones[randint_index] = transacciones[randint_index] + 1

        return (timestamps, transacciones)
