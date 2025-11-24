# Presentación Ejercicio 2.1 – Área y perímetro de un círculo

## Diapositiva 1 – Título y objetivo
- Título: Cálculo geométrico con `math`.
- Objetivo: Practicar `float`, operadores aritméticos e importación de módulos.

## Diapositiva 2 – Enunciado
- Pedir al usuario el radio de un círculo (número real).
- Calcular el área: π·r².
- Calcular el perímetro: 2·π·r.
- Mostrar ambos resultados.

## Diapositiva 3 – Idea de la solución
- Usar `input()` y convertir el radio a `float`.
- Importar `math` para usar `math.pi`.
- Aplicar las fórmulas de área y perímetro.

## Diapositiva 4 – Código clave
- `import math`
- `radio = float(input("Radio: "))`
- `area = math.pi * radio ** 2`
- `perimetro = 2 * math.pi * radio`
- `print("Área:", area)`

## Diapositiva 5 – Extensiones
- Redondear resultados con `round()`.
- Validar que el radio sea positivo.

