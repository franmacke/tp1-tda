import sys
from greedy import algoritmo

def main(argv):

    if len(argv) != 2:
        print("Uso: python3 tp1.py <path>")
        sys.exit(1)

    input_file = argv[1]

    respuesta = algoritmo(input_file)
    print(respuesta)


if __name__ == "__main__":
    main(sys.argv)
