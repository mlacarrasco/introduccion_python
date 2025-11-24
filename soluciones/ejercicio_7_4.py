try:
    import requests
except ImportError:
    requests = None

url = input("Ingrese la URL de la página: ")

if requests is None:
    print("La biblioteca 'requests' no está disponible.")
else:
    try:
        respuesta = requests.get(url, timeout=5)
        contenido = respuesta.text
        print("Primeros 100 caracteres del contenido:")
        print(contenido[:100])
    except Exception as e:
        print("Ocurrió un error al realizar la petición:", e)

