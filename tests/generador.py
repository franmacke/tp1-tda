from random import randint
from collections import deque

class Generador:
    @staticmethod
    def generar_caso_es_sospechoso(n, error, timestamp_interval=(1, 100)):
        """
        Genera un caso donde es sospechoso.
        """
        timestamps = [(randint(timestamp_interval[0], timestamp_interval[1]), randint(1, error)) for _ in range(n)]
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

    @staticmethod
    def generar_ejemplos_con_explicacion():
        timestamps, transacciones = Generador.generar_caso_es_sospechoso(5, 100, (1, 100))

        print("Timestamps:", [f"{ts}" for ts in timestamps])
        print("Transacciones:", [f"{tr}" for tr in transacciones])
        print("\n--- Paso a paso del algoritmo ---\n")

        # ---------- INICIO ALGORITMO ----------

        resultado = []
        sorted_timestamps = sorted(timestamps, key=lambda x: x[0])
        transacciones_deque = deque(sorted(transacciones))

        for index, transaccion in enumerate(transacciones_deque):
            print(f"Transacción #{index+1}: {transaccion}")
            opciones = []

            for timestamp, error in sorted_timestamps:
                if timestamp - error <= transaccion <= timestamp + error:
                    offset = timestamp + error - transaccion
                    opciones.append(((timestamp, error), offset))
                    print(f"  - Candidato válido: timestamp={timestamp}, error={error}, offset={offset}")
                else:
                    print(f"  - No entra en rango: timestamp={timestamp}, error={error}")

            if not opciones:
                print("  ❌ No se encontró timestamp válido. Transacción no emparejada.")
                return "No es el sospechoso correcto"

            mejor = min(opciones, key=lambda x: x[1])
            mejor_timestamp = mejor[0]
            print(f"  ✅ Seleccionado: timestamp={mejor_timestamp[0]}, error={mejor_timestamp[1]} (offset mínimo: {mejor[1]})\n")

            resultado.append((transaccion, mejor_timestamp[0], mejor_timestamp[1]))
            sorted_timestamps.remove(mejor_timestamp)

        # ---------- FIN ALGORITMO ----------

        print("\n--- Resultado final ---")
        for r in sorted(resultado, key=lambda x: x[0]):
            print(f"Transacción {r[0]} ⟶ Timestamp {r[1]} ±{r[2]}")

        return resultado

    @staticmethod
    def generar_ejemplos_con_explicacion_no_sospechoso():
        timestamps, transacciones = Generador.generar_caso_no_es_sospechoso(5, 100, (1, 100))

        print("Timestamps:", [f"{ts}" for ts in timestamps])
        print("Transacciones:", [f"{tr}" for tr in transacciones])
        print("\n--- Paso a paso del algoritmo ---\n")

        # ---------- INICIO ALGORITMO ----------
        resultado = []
        sorted_timestamps = sorted(timestamps, key=lambda x: x[0])
        transacciones_deque = deque(sorted(transacciones))

        for index, transaccion in enumerate(transacciones_deque):
            print(f"Transacción #{index+1}: {transaccion}")
            opciones = []

            for timestamp, error in sorted_timestamps:
                if timestamp - error <= transaccion <= timestamp + error:
                    offset = timestamp + error - transaccion
                    opciones.append(((timestamp, error), offset))
                    print(f"  - Candidato válido: timestamp={timestamp}, error={error}, offset={offset}")
                else:
                    print(f"  - No entra en rango: timestamp={timestamp}, error={error} ➝ Rango válido: [{timestamp - error}, {timestamp + error}]")

            if not opciones:
                print("  ❌ No se encontró timestamp válido. Transacción no emparejada.")
                print("  🧠 Explicación: Esta transacción no se encuentra dentro del rango de ningún timestamp disponible. Por lo tanto, no es posible que haya sido generada por el sospechoso.")
                return "No es el sospechoso correcto"

            mejor = min(opciones, key=lambda x: x[1])
            mejor_timestamp = mejor[0]
            print(f"  ✅ Seleccionado: timestamp={mejor_timestamp[0]}, error={mejor_timestamp[1]} (offset mínimo: {mejor[1]})\n")

            resultado.append((transaccion, mejor_timestamp[0], mejor_timestamp[1]))
            sorted_timestamps.remove(mejor_timestamp)

        # ---------- FIN ALGORITMO ----------

        print("\n--- Resultado final ---")
        for r in sorted(resultado, key=lambda x: x[0]):
            print(f"Transacción {r[0]} ⟶ Timestamp {r[1]} ±{r[2]}")

        return resultado

