def fatorial (numero):
    resultado = numero
    for i in range (numero-1, 0, -1):
        resultado*= i
        print (f'{resultado}')
        
n=int(input("Digite o número: "))

fatorial(n)
        