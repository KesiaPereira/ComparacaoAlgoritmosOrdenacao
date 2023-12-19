import random


class PreencherAleatorio:
    gerador_aleatorio = random.Random()

    @staticmethod
    def criar_lista(tamanho):
        lista = []

        for _ in range(tamanho):
            numero_aleatorio = PreencherAleatorio.gerador_aleatorio.randint(0, 99)
            lista.append(numero_aleatorio)

        return lista