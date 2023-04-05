def read_n_back_lines(n, archivo):
    texto = open(archivo, "r").readlines()
    for i in range((len(texto)-n), len(texto)):
        print(texto[i])

read_n_back_lines(2,"archivo1.txt")