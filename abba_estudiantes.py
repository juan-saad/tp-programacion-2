from itertools import permutations, product
from collections import deque
from typing import Any, Dict, List, Set


class Vertice:
    def __init__(self, nombre: str) -> None:
        self.nombre = str(nombre)

    def get_nombre(self) -> str:
        return self.nombre

    def reemplaza(self, old: str, new: str) -> "Vertice | None":
        if old not in self.nombre:
            return None
        return Vertice(self.nombre.replace(old, new))

    def __str__(self) -> str:
        return self.nombre

    def __repr__(self) -> str:
        return f"{self.nombre}"

    def __eq__(self, other):
        if isinstance(other, Vertice):
            return self.nombre == other.nombre

        return False

    def __hash__(self):
        return hash(self.nombre)


class GrafoDirigido:
    def __init__(self) -> None:
        self.vertices: List[Vertice] = []
        self.vecinos: Dict[Vertice, Set[Vertice]] = {}

    def agregar_vertice(self, vertice: "Vertice") -> None:
        if vertice not in self.vecinos:
            self.vertices.append(vertice)
            self.vecinos[vertice] = set()

    def agregar_arista(self, origen: "Vertice", destino: "Vertice") -> None:
        if origen not in self.vecinos:
            self.agregar_vertice(origen)

        if destino not in self.vecinos:
            self.agregar_vertice(destino)

        self.vecinos[origen].add(destino)

    def get_adjacent(self, vertice: "Vertice") -> Set[Vertice]:
        return self.vecinos[vertice]

    def get_nodes(self) -> list["Vertice"]:
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
                f" {vertice.get_nombre()}: {{"
                + ", ".join([str(v.get_nombre()) for v in vecinos])
                + "}},"
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

    # Hago el producto de todos los elementos del alfabeto para generar todos los posibles vertices
    producto = product(alfabeto, repeat=n)
    vertices = ["".join(combinacion) for combinacion in producto]

    for vertice in vertices:
        v = Vertice(vertice)
        grafo.agregar_vertice(v)

    for vertice in grafo.get_nodes():
        for old in alfabeto:
            for new in alfabeto:
                reemplazo = vertice.reemplaza(old, new)
                if old != new and reemplazo and reemplazo in grafo.get_nodes():
                    grafo.agregar_arista(vertice, reemplazo)

    return grafo


def distancia_a_palindromo(grafo: GrafoDirigido, start: str) -> int:
    """utiliza un algoritmo BFS para encontrar la minima distancia desde start
    a un palindromo en el grafo de reemplazos"""
    vertice_start = Vertice(start)

    if es_palindromo(vertice_start.get_nombre()):
        return 0

    visitados = []
    cola = deque([(vertice_start, 0)])  # Vertice actual y la distancia

    while len(cola) != 0:
        vertice, distancia = cola.popleft()

        if es_palindromo(vertice.get_nombre()):
            return distancia

        if vertice not in visitados:
            visitados.append(vertice)

            for vecino in grafo.get_adjacent(vertice):
                if vecino not in visitados:
                    cola.append((vecino, distancia + 1))

    # No se encontró ningun palíndromo
    return -1


# Ejemplo basico de uso
# grafo_basico = GrafoDirigido()
# v1 = Vertice(1)
# v2 = Vertice(2)
# v3 = Vertice(3)

# grafo_basico.agregar_vertice(v1)
# grafo_basico.agregar_vertice(v2)
# grafo_basico.agregar_vertice(v3)

# grafo_basico.agregar_arista(v1, v2)
# grafo_basico.agregar_arista(v1, v3)

# print(grafo_basico)

# # Test de funcion reemplaza
# print(Vertice("ab").reemplaza("a", "b"))

# Ejemplo para comprobar que el grafo de reemplazo es correcto
# grafo = generar_G_r(2, ["a", "b"])
# print(grafo.vecinos)

# Ejemplo Básico:
grafo = generar_G_r(4, ["o", "n", "c", "e"])
print(grafo.vecinos)
print(distancia_a_palindromo(grafo, "once"))  # Deberia devolver 2.
