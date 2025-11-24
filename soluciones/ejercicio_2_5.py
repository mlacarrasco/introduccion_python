print("Ingrese dos notas (entre 1.0 y 7.0).")

try:
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    promedio = (nota1 + nota2) / 2
    aprueba = promedio >= 4.0 and nota1 >= 3.0 and nota2 >= 3.0

    print("Promedio:", promedio)
    print("¿Aprueba el estudiante?", aprueba)
except ValueError:
    print("Debe ingresar notas numéricas.")

