from desafio_1y2 import hipo, chimuelo, maria

print("Entergía de chimuelo antes de entrenar:",chimuelo.energia)
print("Entergía de maria antes de entrenar:", maria.energia)
print(hipo.entrenar([chimuelo,maria]))
print("Entergía de chimuelo después de entrenar:",chimuelo.energia)
print("Entergía de maria después de entrenar:",maria.energia)
print(hipo.entrenamiento_intensivo([chimuelo,maria]))
print(chimuelo.energia)