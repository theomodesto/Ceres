from IA.DadosTreinamento import *
from IA.Classificador import *

def Treinamento():

    X_Treinamento, y_Treinamento = DadosPlantas()

    print(X_Treinamento.head())
    print(y_Treinamento.head())

    # labEnc = LabelEncoder()
    # y_Treinamento = pd.DataFrame(data=labEnc.fit_transform(y_Treinamento))

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento,
                                                             y=y_Treinamento,
                                                             batch_size=1,
                                                             num_epochs=None,
                                                             shuffle=False)

    numPlantas = len(y_Treinamento)

    print(numPlantas)
    classificador = Classificador(numPlantas)

    print("Treinando a IA!!!")

    classificador.train(input_fn=funcao_treinamento,
                        steps=10000)

    print("Treinamento concluido!!!")

    return True

Treinamento()