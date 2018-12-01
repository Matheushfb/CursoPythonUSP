n = int(input("Insira um numero para saber a divisibilidade por 3 e 5: "))

if(n%3 == 0 and n%5 == 0):
    print("FizzBuzz")
else:
    print(n)
