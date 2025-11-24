# Presentación Ejercicio 9.4 – Manejo combinado de errores

## Diapositiva 1 – Título y objetivo
- Título: Excepciones anidadas para conversión y división.
- Objetivo: Practicar manejo de más de un tipo de error.

## Diapositiva 2 – Enunciado
- Pedir dos valores al usuario.
- Convertirlos a números.
- Dividir el primero por el segundo.
- Manejar errores de conversión y de división por cero.

## Diapositiva 3 – Idea de la solución
- Primero capturar `ValueError` al convertir las entradas.
- Luego, dentro de otro `try`, hacer la división y capturar `ZeroDivisionError`.

## Diapositiva 4 – Código clave
- `a_str = input("A: ")`
- `b_str = input("B: ")`
- `try:`
- `    a = float(a_str); b = float(b_str)`
- `    try:`
- `        print(a / b)`
- `    except ZeroDivisionError:`
- `        print("No se puede dividir por cero.")`
- `except ValueError:`
- `    print("Debe ingresar números válidos.")`

## Diapositiva 5 – Extensiones
- Repetir el proceso hasta obtener una división válida.
- Registrar en pantalla qué tipo de error ocurrió.

