import sys
import unittest
from greedy import algoritmo

def main(argv):

    if len(argv) != 2:
        print("Uso: python3 tp1.py <path>")
        sys.exit(1)

    if argv[1] == "test":
        loader = unittest.TestLoader()
        tests = loader.discover('./tests', pattern='test_*.py')  # Busca archivos test_*.py
        test_runner = unittest.TextTestRunner()
        test_runner.run(tests)
        sys.exit(0)

    input_file = argv[1]

    respuesta = algoritmo(input_file)
    print(respuesta)


if __name__ == "__main__":
    main(sys.argv)
