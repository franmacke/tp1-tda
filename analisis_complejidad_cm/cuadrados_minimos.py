# Imports necesarios para el notebook
from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

from utilidad import time_algorithm
from greedy import algoritmo

# Siempre seteamos la seed de aleatoridad para que los resultados sean reproducibles
seed(12345)
np.random.seed(12345)

sns.set_theme()

#_____________________CALCULO DE COMPLEJIDAD CON TIME_ALGORITHM_______________________________#


def get_random_timestamps_with_errors(size: int):
    # Generamos un arreglo de tuplas (timestamp, error) donde:
    # - 'timestamp' está en el rango [0, 100000)
    # - 'error' está en el rango [1, 100)
    return [(np.random.randint(0, 100000), np.random.randint(1, 101)) for _ in range(size)]


# La variable x van a ser los valores del eje x de los gráficos en todo el notebook
# Tamaño mínimo=100, tamaño máximo=10kk, cantidad de puntos=20
x = np.linspace(100, 10_000_000, 20).astype(int)

results = time_algorithm(algoritmo, x, lambda s: get_random_timestamps_with_errors(s))
ax: plt.Axes
fig, ax = plt.subplots()
ax.plot(x, [results[i] for i in x], label="Medición")
ax.set_title('Tiempo de ejecución de algoritmo')
ax.set_xlabel('Tamaño del array')
ax.set_ylabel('Tiempo de ejecución (s)')
None
# ACA DEBERIA SALIR UN GRAFICO!


#____________________________AJUSTE O ERROR POR CUADRADOS MINIMOS_____________________________________________________#

# función a ajustar: c_1 * n * n + c_2             ---------> nuestro algoritmo tiene pinta de ser O(n * n) = 0(n cuadrado)

# matriz A, cada fila es (n_i * n_i, 1)
A = np.array([[n * n, 1] for n in x])

# vector b, cada elemento es el tiempo que tardó en ejecutar el algoritmo
b = np.array([results[n] for n in x])

# encontramos traspuesta(A)*A
AtA = A.T @ A

# encontramos traspuesta(A)*b
Atb = A.T @ b

# resolvemos x = (traspuesta(A) * A)^-1 * traspuesta(A) * b
c = np.linalg.inv(AtA) @ Atb

print(f"c_1 = {c[0]}, c_2 = {c[1]}")
r = np.linalg.norm(A @ c - b)**2 # || Ax - b ||^2
print(f"Error cuadrático total: {r}") 

# ACA SE DEBERIA IMPRIMIR ALGO DE LA PINTA:
"""
c1 = 1.16e-06, c2 = -7.13e-02
Error cuadratico total = 6.65e-01

"""

#GRAFICO (LO QUE DEBERIA SALIR)
ax.plot(x, [c[0] * n * n + c[1] for n in x], 'r--', label="Ajuste")
ax.legend()
fig

