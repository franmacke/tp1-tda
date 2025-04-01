from unittest import TestCase
from utils import leer_archivos_respuestas
from greedy import algoritmo
import os

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

    def test_no_son_el_sospechoso(self):
        dir_files = os.listdir("data")

        no_es_files = [f for f in dir_files if f.endswith("-no-es.txt")]

        for archivo in no_es_files:
            with self.subTest(archivo=archivo):
                resultado = algoritmo("data/" + archivo)

                self.assertEqual(resultado, "No es el sospechoso correcto", f"Error en {archivo}: Se esperaba un resultado vacío")

