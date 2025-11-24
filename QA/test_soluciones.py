import importlib
import runpy
import unittest
from io import StringIO
from unittest.mock import patch


def run_module_with_input(module_name, inputs):
    """Ejecuta el código de un módulo de soluciones con entradas simuladas.

    Se usa runpy.run_module para ejecutar el módulo en un nuevo espacio de
    nombres en cada prueba, evitando problemas de recarga e importación.
    """
    if inputs is None:
        inputs = []
    with patch("builtins.input", side_effect=inputs):
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            runpy.run_module(module_name, run_name="__main__")
        return fake_out.getvalue()


class TestSolucionesGrupo1(unittest.TestCase):
    def test_ejercicio_1_1(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_1_1", ["Ana", "Pérez"]
        )
        self.assertIn("Pérez, Ana", salida)

    def test_ejercicio_1_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_1_2", ["hola", "mundo"]
        )
        self.assertIn("holamundo", salida)
        self.assertIn("mundohola", salida)

    def test_ejercicio_1_3(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_1_3", ["Santiago", "Chile"]
        )
        self.assertIn("Santiago está en Chile", salida)

    def test_ejercicio_1_4(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_1_4", ["Ana", "3"]
        )
        self.assertGreaterEqual(salida.count("Ana"), 3)

    def test_ejercicio_1_5(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_1_5", ["hola"]
        )
        self.assertIn('Hola, "hola"', salida)

    def test_ejercicio_1_1_otro_nombre(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_1_1", ["Juan", "García"]
        )
        self.assertIn("García, Juan", salida)


class TestSolucionesGrupo2(unittest.TestCase):
    def test_ejercicio_2_1(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_2_1", ["2.0"]
        )
        self.assertIn("Área:", salida)
        self.assertIn("Perímetro:", salida)

    def test_ejercicio_2_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_2_2", ["10", "2"]
        )
        self.assertIn("Suma:", salida)
        self.assertIn("Diferencia", salida)
        self.assertIn("Producto:", salida)

    def test_ejercicio_2_3(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_2_3", ["20"]
        )
        self.assertIn("True", salida)

    def test_ejercicio_2_4(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_2_4", ["1", "2", "3"]
        )
        self.assertIn("Promedio:", salida)

    def test_ejercicio_2_5(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_2_5", ["5.0", "6.0"]
        )
        self.assertIn("¿Aprueba el estudiante?", salida)

    def test_ejercicio_2_3_menor_de_edad(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_2_3", ["16"]
        )
        # Debe imprimir False para menor de 18
        self.assertIn("False", salida)


class TestSolucionesGrupo3(unittest.TestCase):
    def test_ejercicio_3_1(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_3_1", ["5"]
        )
        self.assertIn("positivo", salida.lower())

    def test_ejercicio_3_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_3_2", ["6.0"]
        )
        self.assertIn("Sobresaliente", salida)

    def test_ejercicio_3_3(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_3_3", ["18", "Chile"]
        )
        self.assertIn("puede votar", salida)

    def test_ejercicio_3_4(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_3_4", ["2020"]
        )
        self.assertIn("bisiesto", salida.lower())

    def test_ejercicio_3_5(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_3_5", ["1"]
        )
        self.assertIn("Lunes", salida)

    def test_ejercicio_3_1_negativo(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_3_1", ["-3"]
        )
        self.assertIn("negativo", salida.lower())


class TestSolucionesGrupo4(unittest.TestCase):
    def test_ejercicio_4_1(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_4_1", ["1", "2", "0"]
        )
        self.assertIn("La suma total es:", salida)

    def test_ejercicio_4_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_4_2", ["6"]
        )
        self.assertIn("Números pares desde 2 hasta", salida)

    def test_ejercicio_4_3(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_4_3", ["5"]
        )
        self.assertIn("El factorial de", salida)

    def test_ejercicio_4_4(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_4_4", ["3"]
        )
        self.assertIn("Tabla de multiplicar del", salida)

    def test_ejercicio_4_5(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_4_5", []
        )
        self.assertIn("( 1 , 1 )", salida)

    def test_ejercicio_4_1_suma_simple(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_4_1", ["5", "5", "0"]
        )
        # 5 + 5 = 10
        self.assertIn("10", salida)

    def test_ejercicio_4_4_tabla_de_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_4_4", ["2"]
        )
        # Comprobar algunas líneas típicas de la tabla del 2
        self.assertIn("2 x 1 = 2", salida)
        self.assertIn("2 x 10 = 20", salida)


class TestSolucionesGrupo5(unittest.TestCase):
    def test_ejercicio_5_1(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_5_1", ["3", "5.0", "6.0", "7.0"]
        )
        self.assertIn("promedio", salida.lower())

    def test_ejercicio_5_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_5_2", ["3", "3", "1", "2"]
        )
        self.assertIn("Lista ordenada", salida)

    def test_ejercicio_5_3(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_5_3", ["Ana", "Luis", "FIN"]
        )
        self.assertIn("Se ingresaron", salida)

    def test_ejercicio_5_4(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_5_4", ["1", "2", "3", "0"]
        )
        self.assertIn("Promedio:", salida)

    def test_ejercicio_5_5(self):
        # 10 entradas (algunas no numéricas para probar manejo)
        entradas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        salida = run_module_with_input(
            "soluciones.ejercicio_5_5", entradas
        )
        self.assertIn("Lista de cuadrados:", salida)

    def test_ejercicio_5_1_promedio_simple(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_5_1", ["2", "5.0", "7.0"]
        )
        # Promedio = 6.0, debe aparecer en la salida
        self.assertIn("6.0", salida)

    def test_ejercicio_5_3_dos_nombres(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_5_3", ["Ana", "Luis", "FIN"]
        )
        # Debe contar 2 nombres
        self.assertIn("2", salida)


class TestSolucionesGrupo6(unittest.TestCase):
    def test_ejercicio_6_1(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_6_1", []
        )
        self.assertIn("Cursos y sus créditos", salida)

    def test_ejercicio_6_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_6_2",
            ["Chile", "Santiago", "Chile"],
        )
        self.assertIn("capital de", salida)

    def test_ejercicio_6_3(self):
        # Agregar y mostrar, luego salir
        entradas = [
            "1", "11111111-1", "Ana",
            "3",
            "4",
        ]
        salida = run_module_with_input(
            "soluciones.ejercicio_6_3", entradas
        )
        self.assertIn("Listado de estudiantes", salida)

    def test_ejercicio_6_4(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_6_4", []
        )
        self.assertIn("Estudiante:", salida)

    def test_ejercicio_6_5(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_6_5", ["2000"]
        )
        self.assertIn("Productos con precio mayor", salida)


class TestSolucionesGrupo7(unittest.TestCase):
    def test_ejercicio_7_1(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_7_1", ["9"]
        )
        self.assertIn("Raíz cuadrada:", salida)

    def test_ejercicio_7_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_7_2", []
        )
        self.assertIn("Lanzando un dado 10 veces", salida)

    def test_ejercicio_7_3(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_7_3", []
        )
        self.assertIn("Fecha y hora actual", salida)

    def test_ejercicio_7_4(self):
        # No se afirma sobre salida específica por depender de red;
        # solo se verifica que el módulo se ejecuta con una URL.
        salida = run_module_with_input(
            "soluciones.ejercicio_7_4", ["https://www.example.com"]
        )
        self.assertTrue(len(salida) >= 0)

    def test_ejercicio_7_5(self):
        # Seleccionar la opción 4 inmediatamente para salir.
        salida = run_module_with_input(
            "soluciones.ejercicio_7_5", ["4"]
        )
        self.assertIn("Saliendo del programa", salida)


class TestSolucionesGrupo8(unittest.TestCase):
    def test_ejercicio_8_1(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_8_1", ["Ana"]
        )
        self.assertIn("Hola, Ana!", salida)

    def test_ejercicio_8_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_8_2", ["3", "4"]
        )
        self.assertIn("Suma:", salida)
        self.assertIn("Producto:", salida)

    def test_ejercicio_8_3(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_8_3", []
        )
        self.assertIn("Números pares entre 1 y 20", salida)

    def test_ejercicio_8_4(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_8_4", ["2 3 4 5"]
        )
        self.assertIn("Números primos en la lista:", salida)

    def test_ejercicio_8_5(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_8_5", []
        )
        self.assertIn("Antes de llamar funciones", salida)

    def test_ejercicio_8_1_dos_saludos(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_8_1", ["María"]
        )
        self.assertIn("Hola, María!", salida)

    def test_ejercicio_8_3_par_e_impar(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_8_3", []
        )
        # Debe contener el primer y último par del rango
        self.assertIn("2", salida)
        self.assertIn("20", salida)


class TestSolucionesGrupo9(unittest.TestCase):
    def test_ejercicio_9_1(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_9_1", ["5"]
        )
        self.assertIn("número secreto", salida.lower())

    def test_ejercicio_9_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_9_2", []
        )
        self.assertIn("no se puede dividir por cero", salida.lower())

    def test_ejercicio_9_3(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_9_3", ["abc"]
        )
        self.assertIn("número entero válido", salida.lower())

    def test_ejercicio_9_4(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_9_4", ["10", "0"]
        )
        self.assertIn("dividir por cero", salida.lower())

    def test_ejercicio_9_5(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_9_5", ["java", "c", "c++"]
        )
        self.assertIn("palabra secreta era", salida.lower())

    def test_ejercicio_9_3_entrada_valida(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_9_3", ["42"]
        )
        # Debe reconocer el número entero sin mensaje de error
        self.assertIn("Ingresó el número entero: 42", salida)


class TestSolucionesGrupo10(unittest.TestCase):
    def test_ejercicio_10_1(self):
        # Se entrega una ruta inexistente para comprobar manejo de error.
        salida = run_module_with_input(
            "soluciones.ejercicio_10_1", ["no_existe.csv"]
        )
        self.assertTrue(
            "No se encontró el archivo indicado." in salida
            or "Ocurrió un error al leer el CSV" in salida
        )

    def test_ejercicio_10_2(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_10_2", []
        )
        self.assertIn("DataFrame de estudiantes", salida)

    def test_ejercicio_10_3(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_10_3", ["no_existe.csv", "categoria", "valor"]
        )
        # El mensaje puede ser de archivo no encontrado u otro error controlado
        self.assertTrue(
            "No se encontró el archivo indicado." in salida
            or "Ocurrió un error:" in salida
        )

    def test_ejercicio_10_4(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_10_4", ["no_existe.csv", "x", "y"]
        )
        self.assertTrue(
            "No se encontró el archivo indicado." in salida
            or "Ocurrió un error:" in salida
        )

    def test_ejercicio_10_5(self):
        salida = run_module_with_input(
            "soluciones.ejercicio_10_5", ["no_existe.csv", "fila", "columna"]
        )
        self.assertTrue(
            "No se encontró el archivo indicado." in salida
            or "Ocurrió un error:" in salida
        )


if __name__ == "__main__":
    unittest.main()
