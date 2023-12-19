from DEFs.preenchimento_automatico import PreencherAleatorio
from DEFs.cronometro import Cronometro
from DEFs.algoritmos_ordenacao import AlgoritmosOrdenacao

def main():
    PreenchimentoAutomatico = PreencherAleatorio()
    cronometro = Cronometro()
    AlgoritmosOrdenacao = AlgoritmosOrdenacao()

    tamanho_lista = 30000
    lista = PreenchimentoAutomatico.criar_lista(tamanho_lista)
    lista_aux = lista.copy()

    print(f"\n***** Lista de {len(lista)} elementos *****")

    cronometro.iniciar()
    AlgoritmosOrdenacao.bubble_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Bubble Sort")
    lista = lista_aux

    cronometro.iniciar()
    AlgoritmosOrdenacao.selection_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Selection Sort")
    lista = lista_aux

    cronometro.iniciar()
    AlgoritmosOrdenacao.insertion_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Insertion Sort")
    lista = lista_aux

    cronometro.iniciar()
    AlgoritmosOrdenacao.merge_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Merge Sort")
    lista = lista_aux

    cronometro.iniciar()
    AlgoritmosOrdenacao.quick_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Quick Sort")
    lista = lista_aux

    cronometro.iniciar()
    AlgoritmosOrdenacao.counting_sort(lista)
    tempo_duracao = cronometro.parar()
    print(f"\n--> Ordenada em {cronometro.obter_tempo(tempo_duracao)} usando o Counting Sort")
    lista = lista_aux

if __name__ == "__main__":
    main()
