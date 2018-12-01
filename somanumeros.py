n=int(input("Digite um número inteiro: "))
i = 0
soma = 0
while i < len(str(n)):
    res = n//10**i
    res2 = res%10
    i=i+1
    soma = soma + res2
print(soma)
