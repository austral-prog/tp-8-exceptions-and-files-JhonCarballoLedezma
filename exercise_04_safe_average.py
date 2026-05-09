# Ejercicio 4 - Promedio seguro con manejo de errores
import os

def safe_average(filename):
    """
    Lee un archivo donde hay UN número por línea y retorna el promedio de
    los números válidos (como float).

    Reglas:
    - Las líneas que no se puedan convertir a float deben ignorarse (usar
      try/except ValueError internamente).
    - Las líneas vacías también se ignoran.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo existe pero no contiene ningún número válido, lanzar
      ValueError("no valid numbers").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        float - promedio de los números válidos.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si no hay números válidos en el archivo.

    Ejemplo:
        # archivo contiene: "10\n20\nno_es_un_numero\n30\n"
        safe_average("numeros.txt") -> 20.0
    """
    #pass  # Reemplazar con tu implementación
    if not os.path.exists(filename):
        raise FileNotFoundError ("No existe el archivo")
    numeros_validos = [] #generamos una lista almacenar cada iteración
    with open (filename , "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            try:
                valor = float(line)
                numeros_validos.append(valor)
            except ValueError:
                continue
    
    if len(numeros_validos) == 0:
        raise ValueError("numero no valido")
    return sum(numeros_validos) / len(numeros_validos)
