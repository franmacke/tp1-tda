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