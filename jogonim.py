def usuario_escolhe_jogada(n,m):
    limite = m
    m = int(input("Inisira o numero de peças que deseja retirar do tabuleiro: "))
    while m > limite or m < 0 or m  == 0:
        print("Valor inválido! ")
        m = int(input("Inisira o numero de peças que deseja retirar do tabuleiro: "))
    if m > n or n == m :
        m = n
    return m

def computador_escolhe_jogada(n,m):
    i = 1
    if m > n or n == m:
        m = n
        return m
    else:
        while True:
            if m % 2 == 0:
                return m
                break
            elif m % 2 != 0:
                return m - 1
                break
            else:
                return i
               # i = i + 1
                #if m >= n//2 or
def partida():
    n = int(input("Insira o numero de peças do tabuleiro: "))
    m = int(input("Insira o número máximo de peças a serem retiradas por jogada: "))
    if  m < 0 or n < 0:
        print("Valores insvalidos!!")
        partida()
    if n % (m+1) == 0:
        print ("Você começa")
        while n >= 0:
            u = usuario_escolhe_jogada(n,m)
            n = n - u
            print("O usuário retirou",u,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("Fim do jogo! O usuário ganhou!")
                break
            c = computador_escolhe_jogada(n,m)
            n = n - c
            print("O computador retirou",c,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                break
    else:        
        while n >= 0:
            c = computador_escolhe_jogada(n,m)
            n = n - c
            print("O computador retirou",c,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                break
            u = usuario_escolhe_jogada(n,m)
            n = n - u
            print("O usuário retirou",u,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("Fim do jogo! O usuário ganhou!")
                break
               
def campeonato():
    print("Modo campeonato")
    champs = 4
    while champs > 0:
        champs = champs - 1
        if champs == 0:
            break
        partida()

def main():
    n = 0
    m = 0
    while True:
        jogo = int(input("Escolha um modo de jogo! \n1: Partida \n2: Campeonato\n"))
        if jogo == 1:
            partida()
        if jogo == 2:
            campeonato()
        
main()

