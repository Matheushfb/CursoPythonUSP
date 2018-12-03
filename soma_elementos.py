def soma_elementos(nums):
    i = 0 #Variavel de incremento
    resultado = 0 # Variavel que vai receber a somatoria dos elemento da lista

    while i < len(nums): # Laço que percorre todas as posições do vetor 
        resultado = resultado + nums[i]     #Variavel resultado sempre receberá o ultimo valor armazenodo e soma ao valor so próximo elemento do vetor.
        i = i +1  #Incrementando a veriável i para que percorra todo a lista

    return(resultado) # retorno do resultado
    
