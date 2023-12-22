class AlgoritmosOrdenacao:
    @staticmethod
    def bubble_sort(lista):
        tamanho = len(lista)

        for i in range(tamanho):
            for j in range(0, tamanho - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        return lista

    @staticmethod
    def selection_sort(lista):
        tamanho = len(lista)

        for i in range(tamanho):
            indice_menor = i

            for j in range(i + 1, tamanho):
                if lista[j] < lista[indice_menor]:
                    indice_menor = j
                    
            #if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

        return lista

    @staticmethod
    def insertion_sort(lista):
        tamanho = len(lista)

        for i in range(1, tamanho):
            valor_atual = lista[i]
            j = i - 1

            while j >= 0 and lista[j] > valor_atual:
                lista[j + 1] = lista[j]
                j -= 1

            lista[j + 1] = valor_atual

        return lista

    @staticmethod
    def merge_sort(lista):
        tamanho = len(lista)

        if tamanho <= 1:
            return lista
        else:
            meio = tamanho // 2

            esquerda = lista[:meio]
            direita = lista[meio:]

            AlgoritmosOrdenacao.merge_sort(esquerda)
            AlgoritmosOrdenacao.merge_sort(direita)

            indice_esquerda = indice_direita = indice_lista = 0
            tamanho_esquerda = len(esquerda)
            tamanho_direita = len(direita)

            while indice_esquerda < tamanho_esquerda and indice_direita < tamanho_direita:
                if esquerda[indice_esquerda] < direita[indice_direita]:
                    lista[indice_lista] = esquerda[indice_esquerda]
                    indice_esquerda +=1
                else:
                    lista[indice_lista] = direita[indice_direita]
                    indice_direita += 1
                indice_lista += 1

            while indice_esquerda < tamanho_esquerda:
                lista[indice_lista] = esquerda[indice_esquerda]
                indice_esquerda += 1
                indice_lista +=1

            while indice_direita < tamanho_direita:
                lista[indice_lista] = direita[indice_direita]
                indice_direita += 1
                indice_lista += 1

            return lista


    #@staticmethod
    #def merge(esquerda, direita):
    #    lista_ordenada = []
    #    tamanho_esquerda = len(esquerda)
    #    tamanho_direita = len(direita)
    #    indice_esquerda = indice_direita = 0

    #    while indice_esquerda < tamanho_esquerda and indice_direita < tamanho_direita:
    #        if esquerda[indice_esquerda] < direita[indice_direita]:
    #            lista_ordenada.append(esquerda[indice_esquerda])
    #            indice_esquerda += 1
    #        else:
    #            lista_ordenada.append(direita[indice_direita])
    #            indice_direita += 1

    #    lista_ordenada.extend(esquerda[indice_esquerda:])
    #    lista_ordenada.extend(direita[indice_direita:])

    #    return lista_ordenada

    @staticmethod
    def quick_sort(lista):
        tamanho = len(lista)
        if tamanho <= 1:
            return lista
        else:
            pivot = lista[0]
            esquerda = [x for x in lista[1:] if x <= pivot]
            direita = [x for x in lista[1:] if x > pivot]
            return AlgoritmosOrdenacao.quick_sort(esquerda) + [pivot] + AlgoritmosOrdenacao.quick_sort(direita)

    @staticmethod
    def counting_sort(lista):
        tamanho = len(lista)
        maior_valor = max(lista)

        lista_auxiliar = [0] * (maior_valor + 1)

        for elemento in lista:
            lista_auxiliar[elemento] += 1

        for i in range(1, maior_valor + 1):
           lista_auxiliar[i] += lista_auxiliar[i - 1]

        lista_ordenada  = [0] * tamanho

        i = tamanho - 1
        while i >= 0:
            lista_ordenada[lista_auxiliar[lista[i]] - 1] = lista[i]
            lista_auxiliar[lista[i]] -= 1
            i -= 1

        return lista_ordenada
