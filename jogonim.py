def usuario_escolhe_jogada(n,m):
    limite = m
    m = int(input("Inisira o numero de peças que deseja retirar do tabuleiro: "))
    while m > limite or m < 0 or m  == 0:
        print("Valor inválido! ")
        m = int(input("Inisira o numero de peças que deseja retirar do tabuleiro: "))
    if m > n:
        m = n
    return m

def computador_escolhe_jogada(n,m):
    i = 0
    limite = m
    if m > n or n == m:
        m = n
        return m
    
    if n % 2 == 1 and m % 2 == 1:
        m = 1
        return m

    else:
        while True:
            if n % (m+1) == 0:
                return i 
                break
            else:
                print("Mais um")
                n = n - 1
                i = i + 1
            
            

def partida():
    n = int(input("Insira o numero de peças do tabuleiro: "))
    m = int(input("Insira o número máximo de peças a serem retiradas por jogada"))
    if  m < 0 or n < 0:
        print("Valores insvalidos!!")
        partida()
    if n % (m+1) == 0:
        print ("Usuário começa!")
        while n >= 0:
            m = usuario_escolhe_jogada(n,m)
            n = n - m
            print("O usuário retirou",m,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("Usuário venceu.")
                break
            m = computador_escolhe_jogada(n,m)
            n = n - m
            print("O computador retirou",m,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("Computador venceu!")
                break

    
        
    else:        
        print ("Computador começa!")
        while n >= 0:
            m = computador_escolhe_jogada(n,m)
            n = n - m
            print("O computador retirou",m,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("Computador venceu!")
                break
            m = usuario_escolhe_jogada(n,m)
            n = n - m
            print("O usuário retirou",m,"peças \nRestam",n,"peças no tabuleiro")
            if n == 0:
                print("Usuário venceu!")
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

