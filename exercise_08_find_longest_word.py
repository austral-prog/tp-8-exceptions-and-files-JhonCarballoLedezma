# Ejercicio 8 - Palabra más larga de un archivo
import os

def find_longest_word(filename):
    """
    Lee el archivo, lo divide en palabras (separadas por cualquier tipo
    de whitespace) y retorna la palabra más larga.

    Reglas:
    - Si hay varias palabras con la misma longitud máxima, retornar la
      PRIMERA en aparecer.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo no tiene ninguna palabra (está vacío o solo tiene
      espacios/saltos de línea), lanzar ValueError("file has no words").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        str - la palabra más larga del archivo.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si el archivo no tiene palabras.

    Ejemplo:
        # archivo contiene: "el gato corre rapido\npor el jardin\n"
        find_longest_word("texto.txt") -> "rapido"
    """
    #pass  # Reemplazar con tu implementación
    if not os.path.exists(filename):
        raise FileNotFoundError(f"No se encontro el archivo")
    longest_word = ""
    found_any = False

    with open(filename , "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                found_any = True
                if len(word) > len(longest_word):
                    longest_word = word
    if not found_any:
        raise ValueError ("File has no words")
    return longest_word