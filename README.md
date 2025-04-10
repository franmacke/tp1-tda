# TP1: Greedy


## Requisitos
No se usaron librerías externas de uso poco común, pero para que se pueda ejecutar en todas las máquinas:

```bash
virtualenv .venv
```

### Linux
```bash
source .venv/bin/activate
```

### Windows
```cmd
.venv\Scripts\activate
```


Para ambos sistemas:
```bash
pip install -r requirements.txt
```

## Uso

```bash
python3 tp1.py <comando|path>
```

### path

Puede ser:

- path relativo: data/archivo.txt
- path absoluto: /home/USER/Documents/archivo.txt

### Comandos disponibles

**test**: Ejecuta los tests unitarios definidos en la carpeta ./tests/.

**ejemplo**: Muestra dos ejemplos generados en el momento aleatoriamente. Uno sospechoso y el otro no.
