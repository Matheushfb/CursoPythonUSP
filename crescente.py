## Algoritmo deve receber 3 numeros e veerificar se estão em ordem crescente ou não ##

#Entrada das variáveis
n = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
n3 = int(input("Insira o terceiro número: "))

# Verificação das variaveis 
if(n <= n2):  
    if(n2 <= n3):
        print("crescente")
    else:
        print("não está em ordem crescente")
else:
    print("não está em ordem crescente")
