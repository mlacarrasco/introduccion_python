import math

radio_str = input("Ingrese el radio del círculo: ")

try:
    radio = float(radio_str)
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    print("Área:", area)
    print("Perímetro:", perimetro)
except ValueError:
    print("Debe ingresar un número válido para el radio.")

