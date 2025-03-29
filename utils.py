import re


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



def leer_archivos_respuestas(file_path):
    data = {}

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.endswith(".txt"):
                current_file = line
                data[current_file] = []
            elif "-no-es.txt" in (current_file or ""):
                data[current_file] = "No es el sospechoso correcto"
            else:
                match = re.match(r"(\d+)\s*-->\s*(\d+)\s*±\s*(\d+)", line)
                if match and current_file:
                    num1, num2, tolerance = map(int, match.groups())
                    data[current_file].append((num1, num2, tolerance))

    return data

# data_dict = leer_archivos_respuestas("data/Resultados Esperados.txt")
# print(data_dict)
