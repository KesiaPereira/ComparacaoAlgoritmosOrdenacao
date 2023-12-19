import time

class Cronometro:
    def __init__(self):
        self.tempo_inicial = 0

    def iniciar(self):
        self.tempo_inicial = time.time()

    def parar(self):
        tempo_decorrido = int((time.time() - self.tempo_inicial) * 1000)
        self.tempo_inicial = 0
        return tempo_decorrido
    
    def obter_tempo(self, milissegundos):
        horas = int(milissegundos / (1000 * 60 * 60))
        minutos = int((milissegundos % (1000 * 60 * 60)) / (1000 * 60))
        segundos = int((milissegundos % (1000 * 60)) / 1000)
        milissegundos_restantes = milissegundos % 1000
        tempo_formatado = "{:02d}:{:02d}:{:02d}.{:03d}".format(horas, minutos, segundos, milissegundos_restantes)

        return tempo_formatado