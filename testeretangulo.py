largura = int(input("digite a largura:"))
altura = int(input("digite a altura:"))

# Defini a variável linha para controlar a linha a ser exibida
linha = 1

# Enquanto houver linha a ser exibida:
while  linha <= altura:

    print("#", end = "")
    coluna = 2

    # Substituído linha por largura também
    while coluna < largura: 

        # Se for a primeira linha, a última ou a última coluna
        if linha == 1 or linha == altura or coluna == largura:
            print("#",end="")
        else:
            print(end = " ")

        coluna = coluna + 1

    print("#")

    # Incrementa a variável linha ao invés de decrementar altura
    linha = linha + 1
