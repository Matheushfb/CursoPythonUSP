import math

a = int(input("insira o valor para a: "))
b = int(input("insira o valor para b: "))
c = int(input("insira o valor para c: "))

delta = ((b**2)-(4*a*c))
if (delta < 0):
    print("esta equação não possui raízes reais")
if (delta == 0 ):
    X1 = int((-b + math.sqrt(delta)) / (2*a))
    print("a raiz desta equação é",X1)        
if (delta > 0):
    X1 = ((-b + math.sqrt(delta)) / (2*a))
    X2 = ((-b - math.sqrt(delta)) / (2*a))
    if(X1 > X2):
        print("as raízes da equação são",X2,"e",X1)
    else:
        print("as raízes da equação são",X1,"e",X2)
        
