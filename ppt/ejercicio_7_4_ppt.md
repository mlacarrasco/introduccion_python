# Presentación Ejercicio 7.4 – Petición HTTP con `requests`

## Diapositiva 1 – Título y objetivo
- Título: Uso básico de la biblioteca `requests`.
- Objetivo: Practicar peticiones HTTP y manejo de errores.

## Diapositiva 2 – Enunciado
- Pedir una URL al usuario.
- Obtener el contenido HTML de la página.
- Mostrar sólo los primeros 100 caracteres del contenido.
- Manejar posibles errores (por ejemplo, sin conexión).

## Diapositiva 3 – Idea de la solución
- Intentar importar `requests` y verificar si está disponible.
- Usar `requests.get(url)` dentro de un bloque `try`.
- Acceder al texto con `respuesta.text` y cortar con `[:100]`.

## Diapositiva 4 – Código clave
- `import requests`
- `url = input("URL: ")`
- `resp = requests.get(url)`
- `print(resp.text[:100])`

## Diapositiva 5 – Extensiones
- Mostrar también el código de estado (`resp.status_code`).
- Guardar el HTML en un archivo de texto.

