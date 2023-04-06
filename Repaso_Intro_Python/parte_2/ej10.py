#!/usr/bin/env python3
"""Ej 10: Creá un programa para gestionar datos de los socios de un club, el cual permita:

a) Cargar la información de los socios en un diccionario, al cual poder acceder por número de socio. 
Los datos que se deben almacenar son: número , nombre y apellido , fecha de ingreso (ddmmaaaa) , cuota al día (s/n) .
El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:
Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día
Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día
Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día
b) Informar la cantidad de socios que tiene el club.
c) Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.
d) Modificar la fecha de ingreso de todos los socios ingresados ​​el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.
e) Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
f) Imprimir el listado de socios completos.
Definir las funciones y/o procedimientos que crea necesarios."""

# a) Diccionario con los socios fundadores ya cargados
socios = {1: {"nombre": "Florencia", "apellido": "Ocampo", "fecha_ingreso": "14092001", "cuota_al_dia": True}, 
          2: {"nombre": "David", "apellido": "Estévez", "fecha_ingreso": "14092001", "cuota_al_dia": True}, 
          3: {"nombre": "Sofía", "apellido": "Cáceres", "fecha_ingreso": "14092001", "cuota_al_dia": True}}

# Función para cargar un nuevo socio
def cargar_socio(numero, nombre, apellido, fecha_ingreso, cuota_al_dia):
    socios[numero] = {"nombre": nombre, "apellido": apellido, "fecha_ingreso": fecha_ingreso, 
                      "cuota_al_dia": cuota_al_dia}

# b) Función para informar la cantidad de socios
def cantidad_socios():
    return len(socios)
print(f"Cantidad de socios: {cantidad_socios()}")

# c) Función para registrar que un socio ha pagado todas las cuotas
def pagar_cuotas(numero):
    socios[numero]["cuota_al_dia"] = True
pagar_cuotas(1)
pagar_cuotas(2)

# d) Función para modificar la fecha de ingreso de los socios ingresados el 21/10/2017
def corregir_fecha():
    for socio in socios.values():
        if socio["fecha_ingreso"] == "21102017":
            socio["fecha_ingreso"] = "22102017"
corregir_fecha()

# e) Función para dar de baja a un socio
def dar_de_baja(nombre, apellido):
    for numero, socio in socios.items():
        if socio["nombre"] == nombre and socio["apellido"] == apellido:
            del socios[numero]
dar_de_baja("Sofía", "Cáceres")

# f) Función para imprimir el listado de socios
def imprimir_socios():
    print("Listado de socios:")
    for numero, socio in socios.items():
        print(f"Socio número {numero}: {socio['nombre']} {socio['apellido']}, ingresó el {socio['fecha_ingreso']}, cuota al día: {socio['cuota_al_dia']}")
imprimir_socios()

# Carga inicial de socios fundadores
cargar_socio(1, "Florencia", "Ocampo", "14092001", True)
cargar_socio(2, "David", "Estévez", "14092001", True)
cargar_socio(3, "Sofía", "Cáceres", "14092001", True)





