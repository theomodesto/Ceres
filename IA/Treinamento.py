from IA.DadosTreinamento import *
from IA.Classificador import *

def Treinamento(classificador):

    X_Treinamento, y_Treinamento = DadosPlantas("Plantas")

    # labEnc = LabelEncoder()
    # y_Treinamento = pd.DataFrame(data=labEnc.fit_transform(y_Treinamento))

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento,
                                                             y=y_Treinamento[0],
                                                             batch_size=1,
                                                             num_epochs=None,
                                                             shuffle=False)

    numPlantas = len(y_Treinamento)

    classificador = Classificador(numPlantas)

    classificador.train(input_fn=funcao_treinamento,
                        steps=10000)

    return True