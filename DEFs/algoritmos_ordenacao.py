class AlgoritmosOrdenacao:
    @staticmethod
    def bubble_sort(lista):
        tamanho = len(lista)

        for i in range(tamanho - 1):
            for j in range(tamanho - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        return lista

    @staticmethod
    def selection_sort(lista):
        tamanho = len(lista)

        for i in range(tamanho - 1):
            indice_menor = i

            for j in range(i + 1, tamanho):
                if lista[j] < lista[indice_menor]:
                    indice_menor = j
                    
            if indice_menor != i:
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

        meio = tamanho // 2

        esquerda = lista[:meio]
        direita = lista[meio:]

        return AlgoritmosOrdenacao.merge(AlgoritmosOrdenacao.merge_sort(esquerda), AlgoritmosOrdenacao.merge_sort(direita))

    @staticmethod
    def merge(esquerda, direita):
        lista_ordenada = []
        tamanho_esquerda = len(esquerda)
        tamanho_direita = len(direita)

        indice_esquerda = indice_direita = 0

        while indice_esquerda < tamanho_esquerda and indice_direita < tamanho_direita:
            if esquerda[indice_esquerda] < direita[indice_direita]:
                lista_ordenada.append(esquerda[indice_esquerda])
                indice_esquerda += 1
            else:
                lista_ordenada.append(direita[indice_direita])
                indice_direita += 1

        lista_ordenada.extend(esquerda[indice_esquerda:])
        lista_ordenada.extend(direita[indice_direita:])

        return lista_ordenada

    @staticmethod
    def quick_sort(lista):
        tamanho = len(lista)
        if tamanho <= 1:
            return lista
        
        pivo = lista[tamanho - 1]
        esquerda = []
        direita = []
        for i in range (tamanho - 1):
            if lista[i] < pivo:
                esquerda.append(lista[i])
            else:
                direita.append(lista[i])

        return AlgoritmosOrdenacao.quick_sort(esquerda) + [pivo] + AlgoritmosOrdenacao.quick_sort(direita)

    @staticmethod
    def counting_sort(lista):
        maior_valor = max(lista)

        lista_auxiliar = [0] * (maior_valor + 1)

        for elemento in lista:
            lista_auxiliar[elemento] += 1

        lista_ordenada = []
        for i in range(len(lista_auxiliar)):
            while lista_auxiliar[i] > 0:
                lista_ordenada.append(i)
                lista_auxiliar[i] -= 1

        return lista_ordenada
