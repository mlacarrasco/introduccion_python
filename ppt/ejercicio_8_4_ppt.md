# Presentación Ejercicio 8.4 – Función `es_primo` y filtrado

## Diapositiva 1 – Título y objetivo
- Título: Funciones de decisión con bucles.
- Objetivo: Practicar comprobación de primalidad y uso en otras funciones.

## Diapositiva 2 – Enunciado
- Definir una función `es_primo(n)` que indique si `n` es primo.
- Definir otra función que reciba una lista de enteros.
- La segunda función debe devolver una nueva lista sólo con los primos.

## Diapositiva 3 – Idea de la solución
- En `es_primo`, descartar `n < 2`.
- Probar divisores desde 2 hasta `sqrt(n)` y cortar si se encuentra uno.
- Recorrer la lista original y agregar a la nueva lista sólo los que cumplan `es_primo`.

## Diapositiva 4 – Código clave
- `def es_primo(n):`
- `    if n < 2: return False`
- `    for i in range(2, int(n ** 0.5) + 1):`
- `        if n % i == 0: return False`
- `    return True`

## Diapositiva 5 – Extensiones
- Mostrar también cuántos primos hay en la lista.
- Probar la función con listas generadas automáticamente.

