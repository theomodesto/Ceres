from MODEL.Classificador import Treinamento

def previsao(dadosClima):
    classificador = Treinamento()
    prev = classificador.predict(dadosClima)
    print(prev)
    return prev