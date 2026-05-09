# Ejercicio 5 - CSV a lista de diccionarios
import os 

def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    #pass  # Reemplazar con tu implementación
    if not os.path.exists(filename):
        raise FileNotFoundError(f"no existe el archivo")
    lista_resultado = []

    with open(filename , "r") as file:
        lines = [line.strip() for line in file if line.strip()]

        if len(lines) <= 1:
            return[]
        
        header = [h.strip() for h in lines[0].split(",")]

        for line in lines[1:]:
            values= [v.strip() for v in line.split(",")]

            registro = {
                header[0]: values[0],
                header[1]: int(values[1]),
                header[2]: values[2]
            }
            lista_resultado.append(registro)
            
    return lista_resultado
