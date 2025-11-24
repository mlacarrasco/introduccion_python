# Reporte de ejecución de QA sobre ejercicios de Python

Fecha de ejecución: 2025-11-24  
Comando utilizado: `python -m unittest QA/test_soluciones.py`

Resultado general:
- Tests ejecutados: 60
- Suites de prueba: 10 (Grupos 1 al 10)
- Resultado: **OK** (sin fallos ni errores)

Los tests de QA validan el comportamiento de los scripts de la carpeta `soluciones/` que implementan las respuestas a los ejercicios. Se simula la entrada por teclado (`input()`) y se valida la salida por pantalla (`print()`).

## Resumen por grupo

### Grupo 1 – Cadenas e input
- Scripts probados: `ejercicio_1_1.py` a `ejercicio_1_5.py`
- Tests: 6
- Verifica: formato “Apellido, Nombre”, concatenación de cadenas, construcción de frases, repetición de nombre, uso de comillas.
- Estado: **OK**

### Grupo 2 – Operaciones aritméticas y lógicas
- Scripts probados: `ejercicio_2_1.py` a `ejercicio_2_5.py`
- Tests: 6
- Verifica: área y perímetro de un círculo, operaciones básicas entre enteros, evaluación de mayoría de edad, cálculo de promedio y condición de aprobación.
- Estado: **OK**

### Grupo 3 – Condicionales
- Scripts probados: `ejercicio_3_1.py` a `ejercicio_3_5.py`
- Tests: 6
- Verifica: clasificación de números (positivo/negativo/cero), rangos de notas, votación por país, años bisiestos y días de la semana.
- Estado: **OK**

### Grupo 4 – Ciclos y acumuladores
- Scripts probados: `ejercicio_4_1.py` a `ejercicio_4_5.py`
- Tests: 7
- Verifica: suma de números hasta 0, generación de pares con `range`, factorial con `for`, tablas de multiplicar y doble ciclo `for` (combinaciones).
- Estado: **OK**

### Grupo 5 – Listas
- Scripts probados: `ejercicio_5_1.py` a `ejercicio_5_5.py`
- Tests: 7
- Verifica: cálculo de promedio en listas, ordenamiento, conteo de nombres, filtrado por promedio y generación de lista de cuadrados.
- Estado: **OK**

### Grupo 6 – Diccionarios
- Scripts probados: `ejercicio_6_1.py` a `ejercicio_6_5.py`
- Tests: 5
- Verifica: creación y recorrido de diccionarios, alta/baja de estudiantes, diccionarios anidados con notas y filtrado por precio.
- Estado: **OK**

### Grupo 7 – Bibliotecas estándar y externas
- Scripts probados: `ejercicio_7_1.py` a `ejercicio_7_5.py`
- Tests: 5
- Verifica: uso de `math`, `random`, `datetime`, llamadas HTTP con `requests` (si está disponible) y menú que combina varias bibliotecas.
- Estado: **OK**

### Grupo 8 – Funciones
- Scripts probados: `ejercicio_8_1.py` a `ejercicio_8_5.py`
- Tests: 7
- Verifica: funciones con parámetros y retorno, suma y producto, función `es_par`, filtrado de primos y manejo de variables globales/locales.
- Estado: **OK**

### Grupo 9 – Manejo de errores y juegos simples
- Scripts probados: `ejercicio_9_1.py` a `ejercicio_9_5.py`
- Tests: 6
- Verifica: juego de adivinar número, división por cero, validación de entrada entera, manejo combinado de errores y juego de adivinar palabra con intentos limitados.
- Estado: **OK**

### Grupo 10 – pandas, CSV y gráficos
- Scripts probados: `ejercicio_10_1.py` a `ejercicio_10_5.py`
- Tests: 5
- Verifica:
  - Manejo de lectura de CSV inexistente (`FileNotFoundError`) y mensajes de error controlados.
  - Creación de `DataFrame` de ejemplo, obtención de valores únicos y `groupby`.
  - Uso de `pivot_table`, `matplotlib` (scatter) y `crosstab` con manejo de errores de archivo.
- Estado: **OK**

## Notas sobre el entorno

- Durante la ejecución se generan algunos *warnings* del sistema y de `matplotlib` (permisos y caché de fuentes), pero no afectan el resultado de los tests.
- No se asume la existencia de archivos CSV específicos; los tests de los ejercicios 10.x se centran en que el código maneje correctamente las rutas inválidas y no produzca excepciones no controladas.

