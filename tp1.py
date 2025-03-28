import sys
from utils import leer_archivo


def main(argv):

    if len(argv) != 2:
        print("Uso: python3 tp1.py <path>")
        sys.exit(1)

    input_file = argv[1]

    timestamps, transacciones = leer_archivo(input_file)


if __name__ == "__main__":
    main(sys.argv)
