#!/usr/bin/env python3
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y 
#decir cuantos caracteres tiene.

def longest_word(archivo):
    max_long = 0
    palabra = ""
    with open(archivo,"r") as f:
        word_list = f.read().split()
        for word in word_list:
            if len(word) > max_long:
                max_long = len(word)
                palabra = word
    print("La palabra más larga es", palabra, "con", max_long, "caracteres")
longest_word("archivo1.txt")