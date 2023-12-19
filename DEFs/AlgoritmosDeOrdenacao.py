def bubble_sort(lista):
    tamanho = len(lista)

    for i in range(tamanho - 1):
        for j in range(tamanho - i - 1):
            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

def selection_sort(lista):
    tamanho = len(lista)

    for i in range(tamanho - 1):
        indice_menor_valor = i

        for j in range(i + 1, tamanho):
            if lista[j] < lista[indice_menor_valor]:
                indice_menor_valor = j

            lista[i], lista[indice_menor_valor] = lista[indice_menor_valor], lista[i]

    return lista

def insertion_sort(lista):
    tamanho = len(lista)

    for i in range(1, tamanho):
        valor_atual = lista[i]
        j = i -1

        while j >= 0 and lista[j] > valor_atual:
            lista[j + 1] = lista [j]
            j -= 1
        
        lista[j + 1] = valor_atual
    
    return lista

def merge_sort(lista):
    tamanho = len(lista)

    if tamanho < 2:
        return lista
    
    meio = tamanho // 2

    lista_esquerda = merge_sort(lista[:meio])
    lista_direita = merge_sort(lista[meio:])

    merge(lista, lista_esquerda, lista_direita)

    return lista

def merge(lista, lista_esquerda, lista_direita):
    tamanho_lista_esquerda = len(lista_esquerda)
    tamanho_lista_direita = len(lista_direita)

    indice_lista_esquerda = indice_lista_direita = indice_lista = 0

    while indice_lista_esquerda < tamanho_lista_esquerda and indice_lista_direita < tamanho_lista_direita:
        if lista_esquerda[indice_lista_esquerda] <= lista_direita[indice_lista_direita]:
            lista[indice_lista] = lista_esquerda[indice_lista_esquerda]
            indice_lista_esquerda += 1
        else:
            lista[indice_lista] = lista_direita[indice_lista_direita]
            indice_lista_direita += 1

        indice_lista += 1

    while indice_lista_esquerda < tamanho_lista_esquerda:
        lista[indice_lista] = lista_esquerda[indice_lista_esquerda]
        indice_lista_esquerda += 1
        indice_lista += 1

    while indice_lista_direita < tamanho_lista_direita:
        lista[indice_lista] = lista_direita[indice_lista_direita]
        indice_lista_direita += 1
        indice_lista +=1

def quick_sort(lista):
    pilha = [(0, len(lista) - 1)]

    while pilha:
        inicio, fim = pilha.pop()

        indice_pivo = particionar(lista, inicio, fim)

        if (indice_pivo - 1) > inicio:
            pilha.append((inicio, indice_pivo - 1))

        if (indice_pivo + 1) < fim:
            pilha.append((indice_pivo + 1, fim))

def particionar(lista, inicio, fim):
    pivo = lista[fim]
    indice_pivo = inicio - 1

    for indice_atual in range(inicio, fim):
        if lista[indice_atual] <= pivo:
            indice_pivo += 1
            lista[indice_pivo], lista[indice_atual] = lista[indice_atual], lista[indice_pivo]

    lista[indice_pivo + 1], lista[fim] = lista[fim], lista[indice_pivo + 1]

    return indice_pivo + 1

def counting_sort(lista):
    tamanho = len(lista)
    maior_valor = max(lista)

    lista_auxiliar = [0] * (maior_valor + 1)

    for elemento in lista:
        lista_auxiliar[elemento] += 1

    indice_lista = 0

    for i in range(len(lista_auxiliar)):
        while lista_auxiliar[i] > 0:
            lista[indice_lista] = i
            indice_lista += 1
            lista_auxiliar[i] -= 1
    
    return lista
