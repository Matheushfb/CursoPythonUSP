n = int(input("Digitie o valor de n: ")) #Variavel que contem a quantidade de numeros primos a serem printados
i = 1 
count = 0 # Variável que será incrementada sempre que um número for impar 
parada = False # Condição False na variavel para manter o loop do programa assim que ela for True o programa encerra

while parada == False:  #Enquanto a variavel parada for False o loop continua 
    if count == n: # Se count se igualar ao valor de n a varaivel parada e setada como True o programa encerra
        parada = True        
    if i%2 != 0:   # Se a o resultado do resto da divisão de i por 2 for diferente de zero o numoro é impar
        count = count + 1 # Se o numero for impar incrementa-se a variavel count que é o criterio de parada do programa
        print(i) # Printa o numero impar    
        i = i + 1  # incrementa a variavel i para verificar se o proximo valor de i é impar
    else:   # Caso o programa não satistaça a condição do if acima apenas incrementa-se o valor de i para testar se o proximo valor é impar 
        i = i + 1        
