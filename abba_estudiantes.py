"""
    Trabajo practico Programacion 2: "Problema de aplicación: abba"
    Autores:
        - Juan Manuel Saad
        - Alfredo Sanz
"""

from itertools import product
from collections import deque
from typing import List, Set, Dict

class GrafoDirigido:
    def __init__(self) -> None:
        self.vertices: List[str] = []
        self.vecinos: Dict[str, Set[str]] = {}

    def agregar_vertice(self, vertice: str) -> None:
        if vertice not in self.vecinos:
            self.vertices.append(vertice)
            self.vecinos[vertice] = set()

    def agregar_arista(self, origen: str, destino: str) -> None:
        # Si origen y destino no están en la lista de vecinos, los agrego como nodos
        if origen not in self.vecinos:
            self.agregar_vertice(origen)

        if destino not in self.vecinos:
            self.agregar_vertice(destino)

        self.vecinos[origen].add(destino)

    def get_vecinos(self, vertice: str) -> Set[str]:
        return self.vecinos[vertice]

    def get_vertices(self) -> List[str]:
        return self.vertices

    def __eq__(self, other: "GrafoDirigido") -> bool:
        """compara dos grafos dirigidos (sin tener en cuenta el orden de los conjuntos de vertices y aristas)"""

        if len(self.vecinos.keys()) != len(other.vecinos.keys()):
            return False

        for vertice, vecinos in self.vecinos.items():
            if vertice not in other.vecinos:
                return False

            if vecinos != other.vecinos[vertice]:
                return False

        return True

    def __str__(self) -> str:
        grafo_str = "{"
        for vertice, vecinos in self.vecinos.items():
            grafo_str += (
                f" {vertice}: {{" + ", ".join([str(v) for v in vecinos]) + "}},"
            )
        grafo_str = grafo_str.rstrip(",") + " }"
        return grafo_str


def es_palindromo(s: str) -> bool:
    return s == s[::-1]


def generar_G_r(n: int, alfabeto: list[str]) -> GrafoDirigido | None:
    """
    Genera el grafo de reemplazos para todas las cadenas posibles de longitud `n`
    construidas a partir de un conjunto de caracteres (alfabeto) dado.

    En el grafo de reemplazos, los nodos representan todas las combinaciones
    posibles de caracteres de longitud `n` generadas a partir del alfabeto.
    Dos nodos `s` y `s'` están conectados mediante una arista dirigida de `s` a `s'`
    si `s'` puede obtenerse de `s` mediante una operación de reemplazo que cambia
    todas las ocurrencias de un carácter `char1` por otro carácter `char2`.

    Args:
        n (int): La longitud de las cadenas que forman los nodos del grafo.
        alfabeto (list[str]): Lista de caracteres usados para generar todas las
                              combinaciones posibles de longitud `n`.

    Returns:
        GrafoDirigido | None: El grafo de reemplazos generado. Retorna `None` si
                              `n` es 0 o si el alfabeto está vacío, ya que no
                              pueden generarse cadenas en estos casos.
    """
    if n <= 0 or len(alfabeto) == 0:
        return None

    grafo = GrafoDirigido()

    # Producto cartesiano de todas las posibles combinaciones del alfabeto n veces
    producto = product(alfabeto, repeat=n)
    vertices = ["".join(combinacion) for combinacion in producto]

    for vertice in vertices:
        grafo.agregar_vertice(vertice)

    for vertice in grafo.get_vertices():
        for old in alfabeto:
            for new in alfabeto:
                reemplazo = reemplaza(vertice, old, new)
                if old != new and reemplazo and reemplazo in grafo.get_vertices():
                    grafo.agregar_arista(vertice, reemplazo)

    return grafo


def distancia_a_palindromo(grafo: GrafoDirigido, start: str) -> int:
    """utiliza un algoritmo BFS para encontrar la minima distancia desde start
    a un palindromo en el grafo de reemplazos"""

    if es_palindromo(start):
        return 0

    visitados = []

    # Me guardo el nodo y la distancia inicial
    cola = deque([(start, 0)])

    while len(cola) != 0:
        vertice, distancia = cola.popleft()

        if es_palindromo(vertice):
            return distancia

        if vertice not in visitados:
            visitados.append(vertice)

            for vecino in grafo.get_vecinos(vertice):
                if vecino not in visitados:
                    cola.append((vecino, distancia + 1))

    # Retorno -1 si no encuentro un palíndromo
    return -1


def reemplaza(vertice: str, old: str, new: str) -> "str | None":
    # Evito reemplazos innecesarios en caso que no haya reemplazos posibles
    if old not in vertice:
        return None

    return vertice.replace(old, new)


# Ejemplo basico de uso
# grafo_basico = GrafoDirigido()
# v1 = "1"
# v2 = "2"
# v3 = "3"

# grafo_basico.agregar_vertice(v1)
# grafo_basico.agregar_vertice(v2)
# grafo_basico.agregar_vertice(v3)

# grafo_basico.agregar_arista(v1, v2)
# grafo_basico.agregar_arista(v1, v3)

# print(grafo_basico)

# # Test de funcion reemplaza
# print(reemplaza("ab", "a", "b"))

# Ejemplo para comprobar que el grafo de reemplazo es correcto
# grafo = generar_G_r(2, ["a", "b"])
# print(grafo.vecinos)

# Ejemplo Básico:
grafo = generar_G_r(4, ["o", "n", "c", "e"])
print(grafo.vecinos)
print(distancia_a_palindromo(grafo, "once"))  # Deberia devolver 2.
