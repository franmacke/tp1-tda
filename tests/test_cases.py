from unittest import TestCase
from utils import leer_archivo, leer_archivos_respuestas
from greedy import algoritmo

class CorridasTestCase(TestCase):

    def setUp(self):
        self.respuestas = leer_archivos_respuestas("data/Resultados Esperados.txt")


    def test_son_el_sospechoso(self):
        for archivo, respuestas in self.respuestas.items():
            if "no-es" in archivo:
                continue


            with self.subTest(archivo=archivo):
                archivo = "data/" + archivo

                resultado = algoritmo(archivo)

                self.assertEqual(len(resultado), len(respuestas), f"Error en {archivo}: Longitud de resultados no coincide")

                for respuesta in respuestas:
                    self.assertIn(respuesta, resultado, f"Error en {archivo}: Respuesta {respuesta} no está en el resultado")


    def test_no_son_el_sospechoso(self):
        for archivo, respuesta in self.respuestas.items():
            if "no-es" not in archivo:
                continue

            resultado = algoritmo("data/" + archivo)

            self.assertEqual(resultado, [], f"Error en {archivo}: Se esperaba un resultado vacío")

