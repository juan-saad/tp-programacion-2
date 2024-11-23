# Ejercicios de Grafos: Palíndromos y Reemplazos

## Introducción

Este proyecto es parte de los contenidos prácticos de la materia **Programación 2** de la **Tecnicatura Universitaria en Inteligencia Artificial**. Está diseñado para reforzar conceptos fundamentales de grafos dirigidos y manipulación de cadenas de caracteres. Los ejercicios propuestos combinan teoría de grafos con problemas prácticos de programación, promoviendo el análisis y desarrollo de algoritmos eficientes.

El objetivo principal es implementar un conjunto de funciones y clases que permitan transformar cadenas de caracteres en **palíndromos** mediante operaciones específicas de reemplazo. Estas transformaciones se modelan utilizando un grafo dirigido, lo que permite explorar conexiones entre diferentes cadenas y calcular la distancia mínima a un palíndromo.

Este repositorio contiene el esqueleto del código y las tareas necesarias para completar el proyecto. Es ideal tanto para estudiantes como para programadores interesados en aprender más sobre la combinación de estructuras de datos avanzadas y problemas prácticos.

## Problema Principal: Transformación en Palíndromos

El objetivo principal es transformar una cadena de caracteres en un **palíndromo** aplicando operaciones de reemplazo. Una cadena se considera un palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda (por ejemplo, "abba" o "dad").

### Operación de Reemplazo

La operación `reemplaza(a, b)` cambia todas las ocurrencias del carácter `a` en una cadena por el carácter `b`. Por ejemplo:

- Si `S = "abracadabra"` y aplicamos `reemplaza(b, c)`, la cadena resultante será `acracadacra`.

### Grafo de Reemplazos

Se define un grafo dirigido `Gr = (V, E)` para modelar las transformaciones posibles entre cadenas:

- **Vértices (V):** Todas las posibles cadenas de longitud `n` utilizando un alfabeto dado.
- **Aristas (E):** Dos nodos están conectados si existe una operación `reemplaza(a, b)` que transforma una cadena en la otra.

#### Ejemplo: Grafo de Reemplazos para `n = 2`, Alfabeto `{a, b}`

Vértices: `"aa"`, `"ab"`, `"ba"`, `"bb"`

Aristas:

- `reemplaza(a, b)` transforma `"aa"` en `"bb"`
- `reemplaza(b, a)` transforma `"ab"` en `"aa"`

## Tareas a Implementar

El repositorio incluye un esqueleto de código para completar las siguientes tareas:

1. **Función `es_palindromo`:**

   - Recibe una cadena y determina si es un palíndromo.

2. **Clase `GrafoDirigido`:**

   - Representa un grafo dirigido utilizando un diccionario de nodos y vecinos.

3. **Función `generar_G_r`:**

   - Genera el grafo de reemplazos dado un número positivo `n` y un alfabeto.

4. **Función `distancia_a_palindromo`:**
   - Calcula la cantidad mínima de operaciones de reemplazo necesarias para convertir una palabra en un palíndromo, utilizando el grafo de reemplazos.

### Aclaraciones

- El alfabeto consistirá únicamente de letras minúsculas del español.
- Las palabras evaluadas tendrán entre 1 y 8 caracteres de longitud.
- Cada palabra contendrá un máximo de 4 letras distintas.

## Entrega y Evaluación

- **Formato de entrega:** Código completo en los archivos proporcionados.
- **Restricciones:** No se permiten archivos auxiliares ni bibliotecas no indicadas explícitamente.
- **Evaluación:** Casos de prueba de caja negra; calidad del código; defensa oral del trabajo.
- **Trabajo en grupo:** De 2 a 3 integrantes por grupo (excepcionalmente se aceptarán entregas individuales).

### Fecha de Entrega

**Domingo 24/11/2024 a las 23:59 (horario servidor FCEIA)**.

## Recursos Útiles

- Documentación oficial de [itertools](https://docs.python.org/3/library/itertools.html).

_Tecnicatura Universitaria en Inteligencia Artificial - Programación 2 - 2024_
