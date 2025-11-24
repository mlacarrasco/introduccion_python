# Presentación Ejercicio 8.5 – Variables globales y locales

## Diapositiva 1 – Título y objetivo
- Título: Ámbito de variables en funciones.
- Objetivo: Diferenciar entre variable global y variable local.

## Diapositiva 2 – Enunciado
- Definir una variable global.
- Definir una función que use una variable local con el mismo nombre.
- Definir otra función que modifique la variable global.
- Observar los valores impresos dentro y fuera de las funciones.

## Diapositiva 3 – Idea de la solución
- Declarar `variable_global` fuera de las funciones.
- En la primera función, declarar una variable local con otro valor.
- En la segunda, usar la palabra clave `global` para modificar la global.

## Diapositiva 4 – Código clave
- `variable_global = "Soy global"`
- `def funcion_con_local():`
- `    variable_local = "Soy local"`
- `def funcion_modifica_global():`
- `    global variable_global`
- `    variable_global = "Modificada"`

## Diapositiva 5 – Extensiones
- Agregar comentarios impresos que indiquen desde dónde se está mostrando el valor.
- Probar qué pasa si se quita la palabra clave `global`.

