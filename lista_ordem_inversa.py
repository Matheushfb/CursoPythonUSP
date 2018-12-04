lista = [] # Criando lista vazia
numero = 1  

while numero != 0: # Laço se repete enquanto nosso input for diferente de 0, esse é o motivo da variavel numero ser inicializada com o valor 1
    numero = int(input("digite um numero: "))  # Recebe um numero 
    lista.append(numero) # Adiciona o numero a lista  

## Printando invertido ##
tamanho = len(lista) - 1  # Primeiro geramos uma variavel com o valor do comprimento da lista para ser decrementada 
while tamanho >= 0: # Enquanto essa lista não for percorrida até seu primeiro elemento o loop continua
    print(lista[tamanho],end = "")  # Printando a posição da variavel
    tamanho = tamanho - 1  # decrementando a variavél ate que chegue a 0
