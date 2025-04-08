from scipy.stats import t
import seaborn as sns
import numpy as np
import scipy as sp
import time
import matplotlib.pyplot as plt


from greedy import algoritmo
#from tests.generador import Generador


# Este parámetro controla cuántas veces se ejecuta el algoritmo para cada tamaño
RUNS_PER_SIZE = 5

def _time_run(algorithm, *args):
    start = time.time()
    algorithm(*args)
    return time.time() - start

def time_algorithm(algorithm, sizes, get_args):
    # Diccionario para almacenar los tiempos de ejecución
    times = {size: [] for size in sizes}
    
    for size in sizes:
        for _ in range(RUNS_PER_SIZE):
            args = get_args(size)  # Obtiene los argumentos necesarios para la función
            run_time = _time_run(algorithm, *args)  # Calcula el tiempo de ejecución
            times[size].append(run_time)

    # Promediamos los tiempos para cada tamaño
    avg_times = {size: np.mean(times[size]) for size in sizes}

    return avg_times

# Función para obtener los argumentos adecuados según el tamaño de entrada
def get_args(n):
    # Suponiendo que 'n' es el tamaño de las listas de timestamps y transacciones
    timestamps = [(i, i % 5) for i in range(n)]  # Simulamos timestamps
    transacciones = [i for i in range(n)]  # Simulamos transacciones
    return (None, timestamps, transacciones)

#
# Ejecutando la función time_algorithm con el algoritmo
if __name__ == '__main__':
    sizes = [2000, 4000, 6000, 8000, 10000]  # Diferentes tamaños de entrada
    avg_times = time_algorithm(algoritmo, sizes, get_args)
    
    # #____________________________AJUSTE O ERROR POR CUADRADOS MINIMOS_____________________________________________________#

    # # función a ajustar: c_1 * n * n + c_2             ---------> nuestro algoritmo tiene pinta de ser O(n * n) = 0(n cuadrado)
    # La variable x van a ser los valores del eje x de los gráficos en todo el notebook
    
    x = np.array([2000, 4000, 6000, 8000, 10000])  

    # # matriz A, cada fila es (n_i * n_i, 1)
    A = np.array([[n * n, 1] for n in x])

    # # vector b, cada elemento es el tiempo que tardó en ejecutar el algoritmo
    b = np.array([avg_times[n] for n in x])

    # # encontramos traspuesta(A)*A
    AtA = A.T @ A

    # # encontramos traspuesta(A)*b
    Atb = A.T @ b

    # # resolvemos x = (traspuesta(A) * A)^-1 * traspuesta(A) * b
    c = np.linalg.inv(AtA) @ Atb

    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    r = np.linalg.norm(A @ c - b)**2 # || Ax - b ||^2
    print(f"Error cuadrático total: {r}")
    
    

    

