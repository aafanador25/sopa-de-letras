import json

def get_file_content(file_path):
    """
    Lee el contenido de un archivo de texto y devuelve las líneas en una lista, 
    eliminando los saltos de línea al final de cada línea.
    
    Args:
    file_path (str): La ruta del archivo que se va a leer.

    Returns:
    list: Lista donde cada elemento es una línea del archivo sin saltos de línea.
    """
    with open(file_path) as f:
        content = f.readlines()
    return [line.strip() for line in content]


def encontrar_palabra(sopa, palabra):
    """
    Busca una palabra dentro de una sopa de letras en todas las direcciones posibles (horizontal, 
    vertical y diagonal).

    Args:
    sopa (list): Una lista bidimensional que representa la sopa de letras.
    palabra (str): La palabra que se desea buscar en la sopa de letras.

    Returns:
    bool: True si la palabra es encontrada en la sopa, False en caso contrario.
    """
    filas = len(sopa)
    columnas = len(sopa[0])
    longitud_palabra = len(palabra)

    direcciones = [
        (0, 1),    # Derecha
        (1, 0),    # Abajo
        (0, -1),   # Izquierda
        (-1, 0),   # Arriba
        (1, 1),    # Diagonal abajo-derecha
        (1, -1),   # Diagonal abajo-izquierda
        (-1, 1),   # Diagonal arriba-derecha
        (-1, -1)   # Diagonal arriba-izquierda
    ]

    def buscar_desde(x, y, palabra):
        """
        Verifica si una palabra se encuentra comenzando en una posición específica (x, y)
        y moviéndose en las direcciones posibles.

        Args:
        x (int): La coordenada de fila de inicio.
        y (int): La coordenada de columna de inicio.
        palabra (str): La palabra a buscar.

        Returns:
        bool: True si la palabra es encontrada en la dirección, False en caso contrario.
        """
        for dx, dy in direcciones:
            encontrado = True
            for i in range(longitud_palabra):
                nx, ny = x + i * dx, y + i * dy
                if nx < 0 or nx >= filas or ny < 0 or ny >= columnas or sopa[nx][ny].lower() != palabra[i].lower():
                    encontrado = False
            if encontrado:
                return True
        return False

    for x in range(filas):
        for y in range(columnas):
            if buscar_desde(x, y, palabra):
                return True

    return False


def encontrar_palabras(sopa, palabras):
    """
    Busca una lista de palabras dentro de la sopa de letras y genera un reporte indicando
    si cada palabra fue encontrada o no con valores de True o False.

    Args:
    sopa: la sopa de letras.
    palabras: Lista de palabras que se desean buscar en la sopa de letras.

    Returns:
    Un diccionario donde las claves son las palabras y los valores son True o False,
          indicando si cada palabra fue encontrada o no.
    """
    reporte = {}
    for palabra in palabras:
        encontrada = encontrar_palabra(sopa, palabra)
        reporte[palabra] = encontrada
    return reporte


def main(file_path, output_path):
    """
    Función principal que maneja la lectura del archivo, búsqueda de palabras
    y genera el reporte en formato JSON.

    Args:
    file_path: La ruta del archivo de entrada que contiene la sopa de letras y las palabras.
    output_path : La ruta del archivo de salida donde se guardará el reporte generado.
    """
    contenido = get_file_content(file_path)

    sopa = [list(line) for line in contenido[:5]]
    palabras = contenido[6:]

    reporte = encontrar_palabras(sopa, palabras)

    with open(output_path, 'w') as f:
        json.dump(reporte, f, indent=2)

    print("Reporte generado con éxito:", output_path)
    print(json.dumps(reporte, indent=2))


if __name__ == "__main__":
    input_file = '/Users/Garrincha/Downloads/parcial/sopa de letras.txt'
    output_file = '/Users/Garrincha/Downloads/parcial/output.json'

    main(input_file, output_file)
