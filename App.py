from DEFs.preenchimento_automatico import PreencherAleatorio
from DEFs.cronometro import Cronometro
from DEFs.algoritmos_ordenacao import AlgoritmosOrdenacao

def main():
    preenchimento_automatico = PreencherAleatorio()
    cronometro = Cronometro()
    algoritmos_ordenacao = AlgoritmosOrdenacao()

    tamanho_lista = 30000
    lista = preenchimento_automatico.criar_lista(tamanho_lista)
    lista_aux = lista.copy()

    print(f"\n***** Lista de {len(lista)} elementos *****")

    cronometro.iniciar()
    algoritmos_ordenacao.bubble_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Bubble Sort")
    lista = lista_aux

    cronometro.iniciar()
    algoritmos_ordenacao.selection_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Selection Sort")
    lista = lista_aux

    cronometro.iniciar()
    algoritmos_ordenacao.insertion_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Insertion Sort")
    lista = lista_aux

    cronometro.iniciar()
    algoritmos_ordenacao.merge_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Merge Sort")
    lista = lista_aux

    cronometro.iniciar()
    algoritmos_ordenacao.quick_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Quick Sort")
    lista = lista_aux

    cronometro.iniciar()
    algoritmos_ordenacao.counting_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Counting Sort")
    lista = lista_aux

if __name__ == "__main__":
    main()
