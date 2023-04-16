from aves import pepita, anastasia, roberta
"""
Pepita es un objeto (los llamamos instancias) individual o único dentro de la clase Golondrinas
Entiende mensajes y tiene las características de una golondrina (atributos)
Estos mensajes se llaman métodos.
Los objetos tienen un estado, dado por sus atributos
"""

print("Energía que tiene al comienzo Pepita:",pepita.energia)
print(pepita.volar_en_circulos())
#pepita sabe volar porque no se queja (no hay error)

#print(pepita.hablar())
#pepita no sabe hablar (attribute error)
print("Energía que tiene luego de volar:",pepita.energia)
print(pepita.comer_alpiste(200)) #200 gramos
print("Energía que tiene lugeo de comer:",pepita.energia)

"""
Ahora sabemos que cuando le damos órdenes, hace algo y cambia algo en su estado (energía)
También sabemos que tiene una energía basal
El estado de pepita está dado por su energía
Y como atributos volar y comer alpiste
El estado de los objetos puede cambiar o modificarse
"""

print("Ahora usamos a Anastasia, Energía al comienzo:", anastasia.energia)
anastasia.volar_en_circulos()
print("Luego de volar tiene:", anastasia.energia)
anastasia.comer_alpiste(200)
print("Energía luego de comer:", anastasia.energia)
anastasia #me muestra que es una golondrina
#Los distintos objetos pueden tener distintos estados (anastasia tiene más energía basal)
#Aún con distintos estados, los objetos pueden entender los mismos métodos (mensajes)

print("Ahora utilizamos a roberta, Energía al comienzo:", roberta.energia)
#Tiene 1000 de energía basal
roberta.volar_en_circulos()
print("Energía después de volar:", roberta.energia) #gasta solo 1 de energía
#roberta.comer_alpiste(200)
#print("Energía luego de comer:",roberta.energia) 
#Ups Roberta es un Dragón, no come alpiste
roberta.escupir_fuego()
print("Energía luego de escupir fuego:", roberta.energia)
roberta.comer_peces(200)
print("Energía luego de comer peces:",roberta.energia) 

"""
Entendimos que hay objetos que entienden los mismos mensajes aunque no sean de la misma clase
Los objetos cuentan con una interfaz= el conjunto de mensajes que entienden
Los objetos que comparten su interfaz son polimórficos. En este caso vemos un polimorfismo parcial
Los objetos no saben si son o no polimórficos.
Para ver polimorfismo necesitamos un observador u otro actor (acá nosotros)
"""
print(pepita.esta_feliz())
print(roberta.esta_feliz())

#juanita.correr_en_circulos()
#print("Energía luego de comer:", juanita.energia)