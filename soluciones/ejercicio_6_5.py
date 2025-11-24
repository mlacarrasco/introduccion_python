productos = {
    "Pan": 1000,
    "Leche": 1200,
    "Queso": 5000,
    "Huevos": 2500
}

limite_str = input("Ingrese el precio mínimo para filtrar productos: ")

try:
    limite = int(limite_str)
    print("Productos con precio mayor que", limite, ":")
    for nombre, precio in productos.items():
        if precio > limite:
            print(nombre, "->", precio)
except ValueError:
    print("Debe ingresar un número entero para el precio mínimo.")

