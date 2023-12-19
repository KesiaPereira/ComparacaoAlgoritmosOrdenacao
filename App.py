from DEFs.PreenchimentoAutomatico import PreencherAleatorio
from DEFs.Cronometro import Cronometro
from DEFs.AlgoritmosOrdenacao import AlgoritmosOrdenacao

def main():
    PreenchimentoAutomatico = PreencherAleatorio()
    Cronometro = Cronometro()
    AlgoritmosOrdenacao = AlgoritmosOrdenacao()

    tamanho_lista = 30000
    lista = PreenchimentoAutomatico.criar_lista(tamanho_lista)
    lista_aux = lista.copy()

    print(f"\n***** Lista de {len(lista)} elementos *****")

    Cronometro.iniciar()
    AlgoritmosOrdenacao.bubble_sort(lista)
    tempo_duracao = Cronometro.parar()
    print(f"\n--> Ordenada em {Cronometro.obter_tempo(tempo_duracao)} usando o Bubble Sort")
    lista = lista_aux

    Cronometro.iniciar()
    AlgoritmosOrdenacao.selection_sort(lista)
    tempo_duracao = Cronometro.parar()
    print(f"\n--> Ordenada em {Cronometro.obter_tempo(tempo_duracao)} usando o Selection Sort")
    lista = lista_aux

    Cronometro.iniciar()
    AlgoritmosOrdenacao.insertion_sort(lista)
    tempo_duracao = Cronometro.parar()
    print(f"\n--> Ordenada em {Cronometro.obter_tempo(tempo_duracao)} usando o Insertion Sort")
    lista = lista_aux

    Cronometro.iniciar()
    AlgoritmosOrdenacao.merge_sort(lista)
    tempo_duracao = Cronometro.parar()
    print(f"\n--> Ordenada em {Cronometro.obter_tempo(tempo_duracao)} usando o Merge Sort")
    lista = lista_aux

    Cronometro.iniciar()
    AlgoritmosOrdenacao.quick_sort(lista)
    tempo_duracao = Cronometro.parar()
    print(f"\n--> Ordenada em {Cronometro.obter_tempo(tempo_duracao)} usando o Quick Sort")
    lista = lista_aux

    Cronometro.iniciar()
    AlgoritmosOrdenacao.counting_sort(lista)
    tempo_duracao = Cronometro.parar()
    print(f"\n--> Ordenada em {Cronometro.obter_tempo(tempo_duracao)} usando o Counting Sort")
    lista = lista_aux

if __name__ == "__main__":
    main()
