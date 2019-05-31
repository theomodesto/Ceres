from IA.Classificador import *

def previsao(dadosClima):
    classificador = TreinamentoTensorFlow()
    prev = classificador.predict(dadosClima)
    print(prev)
    return prev