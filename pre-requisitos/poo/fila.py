class Fila:
   
    def __init__(self):
        self.fila = []
    
    def entrar(self, nome):
        self.fila.append(nome)
    def sair (self, nome):
        self.fila.pop(0)
    def mostrar(self):
        return self.fila
f= Fila()

nome = input("Digite um nome: ")

f.entrar(nome)

print (f.mostrar())
