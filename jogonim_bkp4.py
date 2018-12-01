def main():
    while True:
        jogo = int(input("Escolha um modo de jogo! \n1: Partida \n2: Campeonato\n"))
        if jogo == 1:
            partida()
        if jogo == 2:
            campeonato()
        

            
def usuario_escolhe_jogada(n,m):
    limite = m
    num = int(input("Inisira o numero de peças que deseja retirar do tabuleiro: "))
    while num > limite or num < 0 or num  == 0:
        print("Valor inválido! ")
        num = int(input("Inisira o numero de peças que deseja retirar do tabuleiro: "))
    if num > n:
        num = n
    return num

def computador_escolhe_jogada(n,m):
    limite = m
    if n < m:
        m = n
        return m
    if n % 2 == 1 and m % 2 == 1:
        m = 1
        return m
    else:
        return m

def partida():
    n = int(input("Insira o numero de peças do tabuleiro: "))
    m = int(input("Insira o número máximo de peças a serem retiradas por jogada"))
    if  m < 0 or n < 0:
        print("Valores insvalidos!!")
        partida()
    if n % (m+1) == 0:
        print ("Usuário escolhe jogada!")
        while n >= 0:
            p = usuario_escolhe_jogada(n,m)
            n = n - p
            print("O usuário retirou",p,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("O usuario veceu!")
                break
            p = computador_escolhe_jogada(n,m)
            n = n - p
            print("O computador retirou",p,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("O computador veceu!")
                break

    
        
    if n % 2 == 1 and m % 2 == 1:
        
        print ("computador secolhe jogada")
        while n >= 0:
            p = computador_escolhe_jogada(n,m)
            n = n - p
            print("O computador retirou",p,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("O computador veceu!")
                break
            p = usuario_escolhe_jogada(n,m)
            n = n - p
            print("O usuário retirou",p,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("O usuário veceu!")
                break
            
        
def campeonato():
    print("Modo campeonato")
    champs = 4
    while champs > 0:
        champs = champs - 1
        if champs == 0:
            break
        partida()
        
    
main()

