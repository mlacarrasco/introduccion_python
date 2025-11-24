def dividir_por_cero():
    return 1 / 0

try:
    dividir_por_cero()
except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

