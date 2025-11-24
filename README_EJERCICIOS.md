# Ejercicios propuestos por tema

Este archivo contiene listados de ejercicios para trabajar con los códigos de la carpeta raíz.  
Para cada grupo de archivos hay 5 problemas del mismo tenor y nivel.  
En la carpeta `soluciones/` se incluye un archivo `.py` con una posible solución para cada ejercicio.

---

## Grupo 1 – Salida por pantalla, cadenas e input
Archivos relacionados: `01_print.py`, `02_print_cadena.py`, `03_suma_cadenas.py`, `04_union_cadenas.py`, `07_comando_str.py`, `08_comando_input.py`

**Ejercicio 1.1**  
Escribe un programa que pida tu nombre y apellido por teclado y los imprima en una sola línea en formato “Apellido, Nombre”.

**Ejercicio 1.2**  
Pide al usuario dos palabras y muestra la concatenación en ambos órdenes: primero palabra1+palabra2 y luego palabra2+palabra1.

**Ejercicio 1.3**  
Pide al usuario el nombre de una ciudad y un país y forma una frase del tipo “Santiago está en Chile”.

**Ejercicio 1.4**  
Pide al usuario su nombre y un número entero, e imprime el nombre repetido tantas veces como indique el número.

**Ejercicio 1.5**  
Pide al usuario una frase y luego imprime la misma frase entre comillas dobles y con un saludo antes, por ejemplo: `Hola, "tu frase"`.

---

## Grupo 2 – Operaciones aritméticas, conversión numérica y lógica
Archivos relacionados: `05_op_aritmeticas_simple.py`, `06_op_parentesis.py`, `09_comando_int.py`, `10_comando_float.py`, `11_operacion_logica.py`

**Ejercicio 2.1**  
Pide al usuario el radio de un círculo (float) y calcula su área y perímetro.

**Ejercicio 2.2**  
Pide dos enteros y muestra su suma, diferencia, producto y cociente (indicando si el segundo número es 0 antes de dividir).

**Ejercicio 2.3**  
Pide al usuario su edad y muestra `True` si es mayor o igual a 18, y `False` en caso contrario.

**Ejercicio 2.4**  
Pide tres números y calcula el promedio, luego muestra si el promedio es mayor que cada uno de los números individuales.

**Ejercicio 2.5**  
Pide dos notas (float) y determina con una expresión lógica si el estudiante aprueba (promedio ≥ 4.0) y si además ninguna nota es menor a 3.0.

---

## Grupo 3 – Condicionales (if, if-else, elif, anidados)
Archivos relacionados: `12_condicion_if.py`, `13_condicion_if_else.py`, `14_anidados.py`, `15_anidados_elif.py`

**Ejercicio 3.1**  
Pide un número entero y muestra si es positivo, negativo o cero.

**Ejercicio 3.2**  
Pide una nota entre 1 y 7 y clasifícala en “insuficiente (<4)”, “suficiente (≥4 y <5.5)” o “sobresaliente (≥5.5)”.

**Ejercicio 3.3**  
Pide la edad y el país, y determina si la persona puede votar (considera mayoría de edad distinta según país, por ejemplo 18 en Chile, 21 en otro).

**Ejercicio 3.4**  
Pide un año y determina si es bisiesto usando condiciones anidadas (divisible por 4, 100, 400).

**Ejercicio 3.5**  
Pide un número del 1 al 7 y muestra el día de la semana correspondiente usando una cadena de if/elif.

---

## Grupo 4 – Ciclos while/for, break, range, acumuladores
Archivos relacionados: `16_ciclos_while.py`, `17_comando_break.py`, `18_comando_range.py`, `19_ciclos_for.py`, `20_ciclo_for.py`, `21_ciclo_while.py`, `22_ciclo_for_ejemplo.py`, `23_doble_ciclo.py`, `24_doble_ciclo_incremento.py`, `25_potencia_acumulado.py`, `25_potencia_acumulado_2.py`, `26_factorial_acumulado.py`

**Ejercicio 4.1**  
Escribe un programa que pida números enteros al usuario hasta que ingrese 0 y luego muestre la suma total.

**Ejercicio 4.2**  
Dado un número entero n, imprime todos los números pares desde 2 hasta n usando `range`.

**Ejercicio 4.3**  
Calcula el factorial de un número entero n pedido al usuario usando un ciclo `for`.

**Ejercicio 4.4**  
Genera la tabla de multiplicar de un número ingresado por el usuario (del 1 al 10) usando un ciclo `for`.

**Ejercicio 4.5**  
Usa un doble ciclo `for` para imprimir todas las combinaciones (i, j) donde i va de 1 a 3 y j va de 1 a 3.

---

## Grupo 5 – Listas, ingreso de datos, promedio, ordenamiento
Archivos relacionados: `27_lista_ingreso.py`, `28_promedio_lista.py`, `29_lista_ordenada.py`

**Ejercicio 5.1**  
Pide al usuario la cantidad de notas a ingresar, luego cada nota, guárdalas en una lista y muestra el promedio.

**Ejercicio 5.2**  
Pide una cantidad n y luego n números; crea una lista, ordénala de menor a mayor y muéstrala.

**Ejercicio 5.3**  
Pide nombres de estudiantes hasta que el usuario escriba “FIN”, almacénalos en una lista y muestra cuántos nombres se ingresaron.

**Ejercicio 5.4**  
Pide números enteros al usuario, almacénalos en una lista y luego muestra sólo los que son mayores que el promedio de la lista.

**Ejercicio 5.5**  
Crea una lista de 10 enteros ingresados por teclado y genera otra lista con los cuadrados de esos enteros.

---

## Grupo 6 – Diccionarios (creación, modificación, acceso, anidados)
Archivos relacionados: `30_diccionario.py`, `31_modifcar_diccionario.py`, `32_acceder_elemento.py`, `33_agregar_valor.py`, `34_recorrer_items.py`, `35_diccionario_de_diccionario.py`

**Ejercicio 6.1**  
Crea un diccionario que almacene el nombre de 3 cursos y su respectiva cantidad de créditos; muestra todos los pares clave–valor.

**Ejercicio 6.2**  
Pide al usuario el nombre de un país y su capital, agrégalo a un diccionario y luego permite consultar la capital a partir del país.

**Ejercicio 6.3**  
Crea un diccionario de estudiantes donde la clave sea el RUT y el valor sea el nombre; permite agregar y eliminar estudiantes por teclado.

**Ejercicio 6.4**  
Crea un diccionario anidado que represente un estudiante con sus notas en tres asignaturas, luego recorre el diccionario e imprime el promedio por asignatura.

**Ejercicio 6.5**  
Dado un diccionario de productos (clave: nombre, valor: precio), recorre sus ítems y muestra sólo los productos con precio mayor a un valor límite ingresado por el usuario.

---

## Grupo 7 – Bibliotecas y uso de módulos
Archivos relacionados: `36_bibliotecas.py`, `37_request_py.py`

**Ejercicio 7.1**  
Importa la biblioteca `math` y pide un número al usuario; muestra su raíz cuadrada y su seno.

**Ejercicio 7.2**  
Usa `random` para simular el lanzamiento de un dado 10 veces y muestra los resultados.

**Ejercicio 7.3**  
Emplea `datetime` para imprimir la fecha y hora actuales, y luego sólo el año.

**Ejercicio 7.4**  
Usa `requests` (o simula su comportamiento) para obtener el contenido HTML de una página y muestra sólo los primeros 100 caracteres, manejando posibles errores de conexión.

**Ejercicio 7.5**  
Escribe un programa que muestre un menú donde cada opción llama a una función de una biblioteca estándar distinta (`math`, `random`, `datetime`) y ejecuta una pequeña acción.

---

## Grupo 8 – Funciones, parámetros, retorno, variables locales
Archivos relacionados: `38_hola_mundo.py`, `39_hola_mundo_llamado.py`, `40_funcion_parametro.py`, `41_suma_numeros.py`, `42_es_par.py`, `43_es_par_return.py`, `44_es_primo.py`, `45_es_primo_return.py`, `46_parametros.py`, `47_dos_funciones.py`, `48_variables_locales.py`

**Ejercicio 8.1**  
Define una función que reciba un nombre y devuelva un saludo personalizado; pruébala con distintos nombres.

**Ejercicio 8.2**  
Define una función que reciba dos números y retorne su suma, otra que retorne su producto, y llama a ambas desde el programa principal.

**Ejercicio 8.3**  
Define una función `es_par(n)` que devuelva `True` si n es par y `False` en caso contrario, y úsala para imprimir todos los números pares entre 1 y 20.

**Ejercicio 8.4**  
Define una función `es_primo(n)` y luego escribe otra función que reciba una lista de enteros y devuelva una nueva lista solo con los primos.

**Ejercicio 8.5**  
Escribe dos funciones que usen una variable global y otra local con el mismo nombre y muestra en pantalla el valor de cada una para observar la diferencia.

---

## Grupo 9 – Juegos sencillos, errores y manejo de excepciones
Archivos relacionados: `49_mosca.py`, `50_error.py`, `51_manejo_error.py`, `52_manejo_error_tipo.py`, `53_ejemplo_simple.py`

**Ejercicio 9.1**  
Escribe un pequeño juego de adivinar un número entre 1 y 10, donde el programa avise si el usuario se pasa o se queda corto.

**Ejercicio 9.2**  
Simula un error de división por cero dentro de una función y captura la excepción mostrando un mensaje amigable.

**Ejercicio 9.3**  
Pide un número por teclado e intenta convertirlo a entero dentro de un bloque `try/except` para manejar entradas inválidas.

**Ejercicio 9.4**  
Pide al usuario que ingrese dos números y maneja tanto el error de conversión como el de división por cero al dividir el primero por el segundo.

**Ejercicio 9.5**  
Implementa un juego donde el usuario tiene 3 intentos para adivinar una palabra secreta; si falla, el programa termina con un mensaje.

---

## Grupo 10 – pandas, CSV, agrupación, pivot, gráficos
Archivos relacionados: `54_drop_data.py`, `55_unicos.py`, `56_ejercicio.py`, `57_agrupar.py`, `57_agrupar_lambda.py`, `58_agrupar.py`, `58_agrupar_ejercicio.py`, `58_scatter_weight.py`, `59_scatter_height.py`, `60_lectura_formulario_csv.py`, `61_ploty_colab.py`, `62_ploty.py`, `63_pandas_pivot.py`, `64_pivot_household.py`, `65_cross_tab.py`, `66_tablas.py`

**Ejercicio 10.1**  
Lee un archivo CSV simple con pandas, muestra las primeras 5 filas y el resumen estadístico de todas las columnas numéricas.

**Ejercicio 10.2**  
A partir de un DataFrame de estudiantes (nombre, carrera, nota), muestra los nombres únicos de carreras y el promedio de nota por carrera.

**Ejercicio 10.3**  
Carga un CSV con columnas de categoría y valor numérico, y crea una tabla pivote que muestre la suma del valor por categoría.

**Ejercicio 10.4**  
Crea un gráfico de dispersión (scatter) de dos columnas numéricas (por ejemplo altura vs peso) e interpreta visualmente si parecen correlacionadas.

**Ejercicio 10.5**  
A partir de un DataFrame con variables categóricas (por ejemplo género y tipo de curso), genera una tabla de contingencia (`crosstab`) y comenta qué categorías son más frecuentes.

---

## Asignación de ejercicios a cada archivo

En la siguiente lista se indica, para cada archivo del repositorio, qué conjunto de ejercicios (del 1 al 10) le corresponde.  
Cada archivo usa los 5 ejercicios de su grupo (por ejemplo, el archivo `01_print.py` trabaja con los ejercicios 1.1 a 1.5).

- `01_print.py` → ejercicios 1.1–1.5  
- `02_print_cadena.py` → ejercicios 1.1–1.5  
- `03_suma_cadenas.py` → ejercicios 1.1–1.5  
- `04_union_cadenas.py` → ejercicios 1.1–1.5  
- `07_comando_str.py` → ejercicios 1.1–1.5  
- `08_comando_input.py` → ejercicios 1.1–1.5  

- `05_op_aritmeticas_simple.py` → ejercicios 2.1–2.5  
- `06_op_parentesis.py` → ejercicios 2.1–2.5  
- `09_comando_int.py` → ejercicios 2.1–2.5  
- `10_comando_float.py` → ejercicios 2.1–2.5  
- `11_operacion_logica.py` → ejercicios 2.1–2.5  

- `12_condicion_if.py` → ejercicios 3.1–3.5  
- `13_condicion_if_else.py` → ejercicios 3.1–3.5  
- `14_anidados.py` → ejercicios 3.1–3.5  
- `15_anidados_elif.py` → ejercicios 3.1–3.5  

- `16_ciclos_while.py` → ejercicios 4.1–4.5  
- `17_comando_break.py` → ejercicios 4.1–4.5  
- `18_comando_range.py` → ejercicios 4.1–4.5  
- `19_ciclos_for.py` → ejercicios 4.1–4.5  
- `20_ciclo_for.py` → ejercicios 4.1–4.5  
- `21_ciclo_while.py` → ejercicios 4.1–4.5  
- `22_ciclo_for_ejemplo.py` → ejercicios 4.1–4.5  
- `23_doble_ciclo.py` → ejercicios 4.1–4.5  
- `24_doble_ciclo_incremento.py` → ejercicios 4.1–4.5  
- `25_potencia_acumulado.py` → ejercicios 4.1–4.5  
- `25_potencia_acumulado_2.py` → ejercicios 4.1–4.5  
- `26_factorial_acumulado.py` → ejercicios 4.1–4.5  

- `27_lista_ingreso.py` → ejercicios 5.1–5.5  
- `28_promedio_lista.py` → ejercicios 5.1–5.5  
- `29_lista_ordenada.py` → ejercicios 5.1–5.5  

- `30_diccionario.py` → ejercicios 6.1–6.5  
- `31_modifcar_diccionario.py` → ejercicios 6.1–6.5  
- `32_acceder_elemento.py` → ejercicios 6.1–6.5  
- `33_agregar_valor.py` → ejercicios 6.1–6.5  
- `34_recorrer_items.py` → ejercicios 6.1–6.5  
- `35_diccionario_de_diccionario.py` → ejercicios 6.1–6.5  

- `36_bibliotecas.py` → ejercicios 7.1–7.5  
- `37_request_py.py` → ejercicios 7.1–7.5  

- `38_hola_mundo.py` → ejercicios 8.1–8.5  
- `39_hola_mundo_llamado.py` → ejercicios 8.1–8.5  
- `40_funcion_parametro.py` → ejercicios 8.1–8.5  
- `41_suma_numeros.py` → ejercicios 8.1–8.5  
- `42_es_par.py` → ejercicios 8.1–8.5  
- `43_es_par_return.py` → ejercicios 8.1–8.5  
- `44_es_primo.py` → ejercicios 8.1–8.5  
- `45_es_primo_return.py` → ejercicios 8.1–8.5  
- `46_parametros.py` → ejercicios 8.1–8.5  
- `47_dos_funciones.py` → ejercicios 8.1–8.5  
- `48_variables_locales.py` → ejercicios 8.1–8.5  

- `49_mosca.py` → ejercicios 9.1–9.5  
- `50_error.py` → ejercicios 9.1–9.5  
- `51_manejo_error.py` → ejercicios 9.1–9.5  
- `52_manejo_error_tipo.py` → ejercicios 9.1–9.5  
- `53_ejemplo_simple.py` → ejercicios 9.1–9.5  

- `54_drop_data.py` → ejercicios 10.1–10.5  
- `55_unicos.py` → ejercicios 10.1–10.5  
- `56_ejercicio.py` → ejercicios 10.1–10.5  
- `57_agrupar.py` → ejercicios 10.1–10.5  
- `57_agrupar_lambda.py` → ejercicios 10.1–10.5  
- `58_agrupar.py` → ejercicios 10.1–10.5  
- `58_agrupar_ejercicio.py` → ejercicios 10.1–10.5  
- `58_scatter_weight.py` → ejercicios 10.1–10.5  
- `59_scatter_height.py` → ejercicios 10.1–10.5  
- `60_lectura_formulario_csv.py` → ejercicios 10.1–10.5  
- `61_ploty_colab.py` → ejercicios 10.1–10.5  
- `62_ploty.py` → ejercicios 10.1–10.5  
- `63_pandas_pivot.py` → ejercicios 10.1–10.5  
- `64_pivot_household.py` → ejercicios 10.1–10.5  
- `65_cross_tab.py` → ejercicios 10.1–10.5  
- `66_tablas.py` → ejercicios 10.1–10.5  

---

## Ejercicios individuales (uno por cada código original)

En esta sección se define **un ejercicio específico para cada uno de los 66 programas** de la carpeta raíz.  
La idea es que el estudiante pueda tomar el archivo base, leerlo y luego resolver el ejercicio propuesto, que es del mismo tenor.

1. `01_print.py` – Escribe un programa que imprima un mensaje de bienvenida personalizado para un curso de “Introducción a la Programación” y luego muestre en pantalla el resultado de tres operaciones aritméticas simples (suma, resta y multiplicación) usando variables.
2. `02_print_cadena.py` – Escribe un programa que declare dos cadenas de texto (por ejemplo, nombre de la carrera y nombre de la universidad) y las imprima en tres líneas: una por cada cadena y una tercera con ambas unidas.
3. `03_suma_cadenas.py` – Escribe un programa que pida al usuario dos frases cortas y muestre en pantalla la concatenación de ambas separadas por un espacio y también sin espacio, para observar la diferencia.
4. `04_union_cadenas.py` – Escribe un programa que pida nombre, apellido paterno y apellido materno por teclado, y construya una cadena con el nombre completo en el formato “Apellido Paterno Apellido Materno, Nombre”.
5. `05_op_aritmeticas_simple.py` – Escribe un programa que pida dos números enteros al usuario y calcule: suma, resta, multiplicación, división real y resto de la división entera, mostrando cada resultado con una etiqueta clara.
6. `06_op_parentesis.py` – Escribe un programa que calcule tres expresiones aritméticas diferentes que usen paréntesis (por ejemplo `(2+3)*4`, `(10-3)/(2+1)`, etc.) y muestre los resultados comparando cómo cambia la prioridad de las operaciones.
7. `07_comando_str.py` – Escribe un programa que pida al usuario un número entero y convierta ese valor a cadena con `str()`, luego muestre un mensaje del tipo “El número ingresado fue: X” concatenando texto y la versión en cadena.
8. `08_comando_input.py` – Escribe un programa que pida al usuario su nombre, su edad y su ciudad, y luego imprima una sola frase que combine toda la información de forma legible.
9. `09_comando_int.py` – Escribe un programa que pida al usuario la cantidad de asignaturas inscritas (como texto) y convierta la entrada a entero con `int()`, luego imprima cuántos créditos totales representa si cada asignatura vale 6 créditos.
10. `10_comando_float.py` – Escribe un programa que pida al usuario la longitud y el ancho de una sala en metros (usando `float()`), calcule el área y muestre el resultado con un mensaje adecuado.
11. `11_operacion_logica.py` – Escribe un programa que pida la edad de un estudiante y su nota final, y determine mediante una expresión lógica si “es mayor de edad y está aprobado” (por ejemplo, edad ≥ 18 y nota ≥ 4.0).
12. `12_condicion_if.py` – Escribe un programa que pida un número entero y muestre un mensaje sólo si el número es estrictamente mayor que 100, sin hacer nada en caso contrario.
13. `13_condicion_if_else.py` – Escribe un programa que pida un entero representando la temperatura ambiente y muestre “Hace frío” si es menor a 15 grados y “No hace frío” en caso contrario.
14. `14_anidados.py` – Escribe un programa que pida una nota entre 1 y 7 y, usando `if` anidados, indique si el alumno está reprobado (<4), aprobando justo (≥4 y <5.5) o tiene nota destacada (≥5.5).
15. `15_anidados_elif.py` – Escribe un programa que pida un número entero del 1 al 5 y, usando `if/elif/else`, muestre un mensaje distinto para cada número y un mensaje de error si está fuera de rango.
16. `16_ciclos_while.py` – Escribe un programa que use un ciclo `while` para imprimir todos los números del 1 al 10 en orden creciente, y luego imprima un mensaje indicando que el ciclo terminó.
17. `17_comando_break.py` – Escribe un programa que pida repetidamente números enteros al usuario usando un `while True`, y que termine (usando `break`) cuando el usuario ingrese un número negativo; al final debe mostrar cuántos números no negativos se ingresaron.
18. `18_comando_range.py` – Escribe un programa que utilice `range()` para imprimir todos los números entre 0 y 50 que sean múltiplos de 5, cada uno en una línea distinta.
19. `19_ciclos_for.py` – Escribe un programa que, usando un ciclo `for`, imprima los números del 1 al 20 y señale para cada uno si es par o impar.
20. `20_ciclo_for.py` – Escribe un programa que pida al usuario una palabra y luego, usando un `for`, imprima cada carácter de la palabra en una línea diferente, junto con su posición (índice).
21. `21_ciclo_while.py` – Escribe un programa que pida al usuario una contraseña hasta que la ingrese correctamente (por ejemplo “python123”) usando un `while`, contando la cantidad de intentos utilizados.
22. `22_ciclo_for_ejemplo.py` – Escribe un programa que pida un número entero positivo `n` y, usando un `for`, calcule la suma de los primeros `n` números naturales (1 + 2 + … + n) mostrando el resultado final.
23. `23_doble_ciclo.py` – Escribe un programa que utilice dos ciclos `for` anidados para imprimir una pequeña tabla con las combinaciones de dos dados (valores de 1 a 6 en cada dado).
24. `24_doble_ciclo_incremento.py` – Escribe un programa que muestre una “matriz” de 5 filas por 5 columnas con números del 1 al 25 impresos fila por fila, usando ciclos anidados.
25. `25_potencia_acumulado.py` – Escribe un programa que pida un número entero `n` y calcule la suma de las potencias `2^0 + 2^1 + ... + 2^n` usando un ciclo con una variable acumuladora.
26. `25_potencia_acumulado_2.py` – Escribe un programa que pida un número entero `n` y calcule el valor de `3^n` multiplicando sucesivamente en un ciclo, sin usar el operador de potencia `**`.
27. `26_factorial_acumulado.py` – Escribe un programa que pida un número entero `n` y calcule su factorial `n!` utilizando un ciclo y una variable acumuladora, mostrando el resultado.
28. `27_lista_ingreso.py` – Escribe un programa que pida al usuario cuántos números desea ingresar, luego los lea y los guarde en una lista, y finalmente muestre la lista completa y la suma de sus elementos.
29. `28_promedio_lista.py` – Escribe un programa que pida al usuario las notas de todos los ramos del semestre, las guarde en una lista y luego calcule y muestre el promedio general.
30. `29_lista_ordenada.py` – Escribe un programa que pida 10 números enteros, los guarde en una lista y luego imprima la lista ordenada de menor a mayor y de mayor a menor.
31. `30_diccionario.py` – Escribe un programa que cree un diccionario con al menos 4 países como claves y sus capitales como valores, y luego imprima cada país y su capital en una línea.
32. `31_modifcar_diccionario.py` – Escribe un programa que parta con un diccionario de productos y precios, permita cambiar el precio de un producto dado su nombre y luego muestre el diccionario actualizado.
33. `32_acceder_elemento.py` – Escribe un programa que defina un diccionario de códigos de curso y nombres (por ejemplo `"INF100": "Introducción a la Programación"`) y luego pida un código al usuario para mostrar el nombre del curso correspondiente.
34. `33_agregar_valor.py` – Escribe un programa que inicialice un diccionario vacío de estudiantes (RUT → nombre) y permita agregar tres estudiantes desde teclado, mostrando el diccionario al final.
35. `34_recorrer_items.py` – Escribe un programa que tenga un diccionario con asignaturas como claves y notas finales como valores, y recorra sus ítems imprimiendo una frase del tipo “En ASIGNATURA tu nota fue NOTA”.
36. `35_diccionario_de_diccionario.py` – Escribe un programa que represente, mediante un diccionario de diccionarios, a dos estudiantes con su nombre y sus notas en tres ramos, y luego imprima el promedio de cada estudiante.
37. `36_bibliotecas.py` – Escribe un programa que importe `math` y `random`, pida un número al usuario y muestre su raíz cuadrada y luego un número aleatorio entero entre 1 y ese número.
38. `37_request_py.py` – Escribe un programa que, usando `requests` si está disponible, intente descargar el contenido de `https://www.example.com`, imprima el código de estado HTTP y los primeros 200 caracteres del cuerpo de la respuesta.
39. `38_hola_mundo.py` – Escribe un programa que defina una función `saludo()` que imprima “Hola Mundo desde una función” y la llame desde el bloque principal del programa.
40. `39_hola_mundo_llamado.py` – Escribe un programa que defina una función `saludar(nombre)` que reciba un nombre y lo imprima en un saludo personalizado, y luego sea llamada al menos dos veces con nombres distintos.
41. `40_funcion_parametro.py` – Escribe un programa que defina una función que reciba un número entero y muestre su cuadrado, y luego pida un número al usuario y llame a la función con ese valor.
42. `41_suma_numeros.py` – Escribe un programa que defina una función que reciba dos números y retorne su suma; luego pida dos números al usuario, llame a la función y muestre el resultado.
43. `42_es_par.py` – Escribe un programa que defina una función `es_par(n)` que imprima si un número es par o impar, y luego pida al usuario un número para pasarlo a la función.
44. `43_es_par_return.py` – Escribe un programa que defina una función `es_par(n)` que devuelva `True` o `False` según corresponda y luego use esa función para construir una lista con sólo los números pares entre 1 y 30.
45. `44_es_primo.py` – Escribe un programa que defina una función `es_primo(n)` que imprima si un número es primo o no, y la utilice para probar todos los números del 1 al 20.
46. `45_es_primo_return.py` – Escribe un programa que defina una función `es_primo(n)` que retorne `True` o `False`, y luego reciba desde teclado una lista de números (separados por espacio) y muestre sólo aquellos que son primos.
47. `46_parametros.py` – Escribe un programa que defina una función que reciba el nombre de un curso y el número de créditos, y que imprima un mensaje describiendo ese curso; llama a la función al menos tres veces con valores distintos.
48. `47_dos_funciones.py` – Escribe un programa que defina dos funciones: una que convierta grados Celsius a Fahrenheit y otra que convierta Fahrenheit a Celsius; luego pida al usuario una temperatura y un tipo de conversión a realizar.
49. `48_variables_locales.py` – Escribe un programa que defina una variable global `contador`, dos funciones que la modifiquen en distinta forma (una sumando 1 y otra sumando 2) y muestre cómo cambia su valor luego de llamar a ambas.
50. `49_mosca.py` – Escribe un programa que implemente un sencillo “juego de la mosca”: el computador elige aleatoriamente un número entre 1 y 5, el usuario intenta adivinarlo y el programa indica si acertó o no.
51. `50_error.py` – Escribe un programa que provoque intencionalmente un error de índice en una lista (por ejemplo, acceder a una posición que no existe) y capture la excepción mostrando un mensaje explicativo.
52. `51_manejo_error.py` – Escribe un programa que defina una función que intente dividir un número entre otro y, usando `try/except`, maneje cualquier error mostrando el tipo de excepción producida.
53. `52_manejo_error_tipo.py` – Escribe un programa que pida un número al usuario y, si la conversión a entero falla, capture el `ValueError` y muestre un mensaje indicando que el tipo de dato ingresado no es válido.
54. `53_ejemplo_simple.py` – Escribe un programa que combine todas las ideas básicas: pida un nombre, edad y tres notas, calcule el promedio de las notas y muestre un mensaje resumido, manejando posibles errores de entrada numérica.
55. `54_drop_data.py` – Escribe un programa que lea un CSV con pandas, elimine al menos una columna usando `drop()` y muestre el `DataFrame` antes y después de la eliminación.
56. `55_unicos.py` – Escribe un programa que lea un archivo CSV y muestre los valores únicos de una columna categórica (por ejemplo, “Nombre” o “Carrera”) usando el método `.unique()`.
57. `56_ejercicio.py` – Escribe un programa que lea un CSV de datos de estudiantes, calcule el promedio de una columna numérica (por ejemplo, “Nota”) y muestre además cuántos registros tienen valores por sobre ese promedio.
58. `57_agrupar.py` – Escribe un programa que lea un CSV con pandas, agrupe los datos por una columna categórica usando `groupby()` y muestre la suma de una columna numérica para cada grupo.
59. `57_agrupar_lambda.py` – Escribe un programa que haga un `groupby()` sobre un `DataFrame` y aplique una función `lambda` para calcular alguna métrica personalizada (por ejemplo, rango máximo–mínimo de una columna numérica por grupo).
60. `58_agrupar.py` – Escribe un programa que construya un `DataFrame` de ejemplo en memoria (sin leer archivo) con columnas de categoría y valor numérico, y luego muestre la media de la columna numérica por categoría.
61. `58_agrupar_ejercicio.py` – Escribe un programa que, a partir de un `DataFrame` de ventas con columnas “vendedor”, “mes” y “monto”, calcule el total vendido por cada vendedor en todo el período.
62. `58_scatter_weight.py` – Escribe un programa que lea datos de altura y peso desde un CSV y construya un gráfico de dispersión (scatter) con altura en el eje X y peso en el eje Y.
63. `59_scatter_height.py` – Escribe un programa que genere un `DataFrame` sintético con alturas de estudiantes por curso y construya un gráfico de dispersión o de puntos que muestre altura versus índice del estudiante.
64. `60_lectura_formulario_csv.py` – Escribe un programa que lea un archivo CSV proveniente de un formulario (con nombre, edad y carrera) y, tras cargarlo en pandas, imprima cuántos estudiantes hay en cada carrera.
65. `61_ploty_colab.py` – Escribe un programa que prepare un `DataFrame` con datos simples (por ejemplo, año y matrícula de estudiantes) y genere un gráfico de líneas usando Plotly (o deje preparado el código para ejecutarlo en Colab).
66. `62_ploty.py`, `63_pandas_pivot.py`, `64_pivot_household.py`, `65_cross_tab.py`, `66_tablas.py` – Diseña un programa para cada uno de estos archivos que tome un conjunto de datos tabulares y genere distintos informes: gráficos interactivos con Plotly, tablas pivote de gastos por categoría y hogar, tablas cruzadas de variables categóricas y resúmenes en “tablas de reporte” listos para ser exportados.
