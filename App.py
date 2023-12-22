from DEFs.preenchimento_automatico import PreencherAleatorio
from DEFs.cronometro import Cronometro
from DEFs.algoritmos_ordenacao import AlgoritmosOrdenacao

def main():
    preenchimento_automatico = PreencherAleatorio()
    cronometro = Cronometro()
    algoritmos_ordenacao = AlgoritmosOrdenacao()

    #tamanhos = [100, 500, 1000, 30000, 80000, 100000, 150000, 200000]
    tamanho_lista = 100 #Alterar o valor conforme o nescessário.
    lista = preenchimento_automatico.criar_lista(tamanho_lista)
    
    lista_auxiliar1 = lista.copy()
    lista_auxiliar2 = lista.copy()
    lista_auxiliar3 = lista.copy()
    lista_auxiliar4 = lista.copy()
    lista_auxiliar5 = lista.copy()
    lista_auxiliar6 = lista.copy()

    print(f"\n***** Lista de {len(lista)} elementos *****")

    cronometro.iniciar()
    algoritmos_ordenacao.bubble_sort(lista_auxiliar1)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.formatar_tempo(tempo_duracao)} usando o Bubble Sort")

    cronometro.iniciar()
    algoritmos_ordenacao.selection_sort(lista_auxiliar2)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.formatar_tempo(tempo_duracao)} usando o Selection Sort")

    cronometro.iniciar()
    algoritmos_ordenacao.insertion_sort(lista_auxiliar3)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.formatar_tempo(tempo_duracao)} usando o Insertion Sort")

    cronometro.iniciar()
    algoritmos_ordenacao.merge_sort(lista_auxiliar4)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.formatar_tempo(tempo_duracao)} usando o Merge Sort")

    cronometro.iniciar()
    algoritmos_ordenacao.quick_sort(lista_auxiliar5)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.formatar_tempo(tempo_duracao)} usando o Quick Sort")

    cronometro.iniciar()
    algoritmos_ordenacao.counting_sort(lista_auxiliar6)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.formatar_tempo(tempo_duracao)} usando o Counting Sort")

if __name__ == "__main__":
    main()
