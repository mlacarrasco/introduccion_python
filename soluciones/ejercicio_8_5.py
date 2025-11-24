variable_global = "Soy global"

def funcion_con_local():
    variable_local = "Soy local dentro de la función"
    print("Dentro de funcion_con_local, variable_local:", variable_local)
    print("Dentro de funcion_con_local, variable_global:", variable_global)

def funcion_modifica_global():
    global variable_global
    variable_global = "Global modificada en la función"
    print("Dentro de funcion_modifica_global, variable_global:", variable_global)

print("Antes de llamar funciones, variable_global:", variable_global)
funcion_con_local()
funcion_modifica_global()
print("Después de llamar funciones, variable_global:", variable_global)

