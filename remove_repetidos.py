def remove_repetidos(nums):
    i = 0  # Variavel de incremento
    newnums = [] # Nova lista para receber somente os elementos únicos
    list.sort(nums)  # Ordenando a lista

    while(i < len(nums)):
        if nums[i] not in newnums: # Se a variavel nums[i] não existir na nova lista eu a adiciono 
            newnums.append(nums[i]) # Adicionando o novo elemento a lista
            i=i+1   
        else:    # Se o elemento da posição num[i] ja existir na em newnums eu apenas pulo para o proximo elemento do vetor a ser verificado
            i=i+1  
    return(newnums) 
