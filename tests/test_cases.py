import os
from unittest import TestCase
from utils import leer_archivos_respuestas
from greedy import algoritmo
from generador import Generador

class CorridasTestCase(TestCase):

    def setUp(self):
        self.respuestas = leer_archivos_respuestas("data/Resultados Esperados.txt")
        self.generador = Generador(10, 5)

    def test_son_el_sospechoso(self):
        for archivo, respuestas in self.respuestas.items():
            if "no-es" in archivo:
                continue


            with self.subTest(archivo=archivo):
                archivo = "data/" + archivo

                resultado = algoritmo(path=archivo)

                self.assertEqual(len(resultado), len(respuestas), f"Error en {archivo}: Longitud de resultados no coincide")

    def test_no_son_el_sospechoso(self):
        dir_files = os.listdir("data")

        no_es_files = [f for f in dir_files if f.endswith("-no-es.txt")]

        for archivo in no_es_files:
            with self.subTest(archivo=archivo):
                resultado = algoritmo(path="data/" + archivo)

                self.assertEqual(resultado, "No es el sospechoso correcto", f"Error en {archivo}: Se esperaba un resultado vacío")


    def test_generador_es_sospechoso(self):
        timestamps, transacciones = self.generador.generar_caso_es_sospechoso(10, 5)

        resultado = algoritmo(timestamps=timestamps, transacciones=transacciones)

        self.assertNotEqual(resultado, "No es el sospechoso correcto", "Error en el generador: Se esperaba un resultado válido")
        self.assertEqual(len(resultado), len(transacciones), "Error en el generador: Longitud de resultados no coincide")


    def test_generador_no_es_sospechoso(self):
        timestamps, transacciones = self.generador.generar_caso_no_es_sospechoso(10, 5)

        resultado = algoritmo(timestamps=timestamps, transacciones=transacciones)

        self.assertEqual(resultado, "No es el sospechoso correcto", "Error en el generador: Se esperaba un resultado vacío")