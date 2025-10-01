## A função é obrigado a retornar algo

def soma (a,b):
    """Função de soma
    args:
        a: numero 
        b: numero
    return:
        a soma de a+b"""
    return a+b

#forma posicional de chamar a função
print(soma(10, 10))

#forma nomedadde de chamar a função (chave valor)
print(soma(a=2, b=3))