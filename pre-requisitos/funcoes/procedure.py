## uma procedure não é obrigada a retorna, um dado

lista = []
def aumenta_lista(num):
    """Adiciona um número no array
    args:
        num: número para ser adicionado
    return: 
        a lista com um número a mais
    """
    lista.append(num)
print(lista)
aumenta_lista(2)
print(lista)
aumenta_lista(3)
print(lista)