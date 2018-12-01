n = int(input("Digitie o valor de n: "))
i = 1
count = 0
parada = False
while parada == False:
    if count == n:
        parada = True        
    if i%2 != 0:
        count = count + 1
        print(i)
        i = i + 1 
    else:
        i = i + 1        
