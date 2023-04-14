#!/bin/python3
import os, sys

usuario = sys.argv[1] 
# argv es argumento, esto es para declarar una variable
#Espera que le pase el argumento en la terminal
#Con el 1 dice que toma el primer argumento

def saludador(nombre):
   return "Hola " + nombre

#sys.argv toma los argumentos que le pasamos al script por consola
#[1] significa que toma el primer argumento


if __name__ == "__main__":
  saludador(usuario)
#Para salir y poder ejecutarlo, poner exit() + enter en la terminal.
