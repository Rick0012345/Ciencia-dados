# programa em python que calcula a sequencia fibonnacci
from time import sleep
def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)


lista = []


while len(lista) <15:
    lista.append(fibonnaci(len(lista)))
    sleep(0.1)
    print (lista)