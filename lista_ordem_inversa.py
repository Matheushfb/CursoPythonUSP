lista = []
pos = 0
numero = 1 
while numero != 0:
    numero = int(input("digite um numero: "))
    lista.append(numero)
    pos = pos + 1

tamanho = len(lista) - 1
while tamanho >= 0:
    print(lista[tamanho],end = "")
    tamanho = tamanho - 1 
