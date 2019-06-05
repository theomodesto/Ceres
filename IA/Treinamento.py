from IA.DadosTreinamento import *
from IA.Classificador import *
import pickle
from sklearn.preprocessing import StandardScaler

steps = 20000

def Treinamento():

    X_Treinamento, y_Treinamento = DadosPlantas()

    scaler = StandardScaler()

    X_Treinamento = pd.DataFrame(data=scaler.fit_transform(X_Treinamento), columns=X_Treinamento.columns)

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento,
                                                             y=y_Treinamento,
                                                             batch_size=1,
                                                             num_epochs=None,
                                                             shuffle=False)

    numPlantas = len(y_Treinamento)

    classificador = Classificador(numPlantas)

    print("Treinando a IA !!!")

    classificador.train(input_fn=funcao_treinamento,
                        steps=steps)

    eval = classificador.evaluate(input_fn=funcao_treinamento,steps=steps)

    print("Treinamento concluido !!!\nScore:",eval)

    return True

def TreinamentoDadosAumentados():

    X_Treinamento, y_Treinamento = DadosPlantasAumentados()

    scaler = StandardScaler()

    X_Treinamento  = pd.DataFrame(data=scaler.fit_transform(X_Treinamento),columns=X_Treinamento.columns)

    print(X_Treinamento.head())

    # labEnc = LabelEncoder()
    # y_Treinamento = pd.DataFrame(data=labEnc.fit_transform(y_Treinamento))

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_Treinamento,
                                                             y=y_Treinamento,
                                                             batch_size=1,
                                                             num_epochs=None,
                                                             shuffle=False)

    numPlantas = len(y_Treinamento)

    classificador = ClassificadorDadosAumentados(numPlantas)

    print("Treinando a IA !!!")

    classificador.train(input_fn=funcao_treinamento,
                        steps=steps)

    eval = classificador.evaluate(input_fn=funcao_treinamento, steps=steps)

    print("Treinamento concluido !!!\nScore:",eval)

    return True

def TreinamentoSklearn():
    X_Treinamento, y_Treinamento = DadosPlantas()

    scaler = StandardScaler()

    X_Treinamento = pd.DataFrame(data=scaler.fit_transform(X_Treinamento), columns=X_Treinamento.columns)

    numPlantas = len(y_Treinamento)

    classificador = ClassificadorSklearn(numPlantas)

    print("Treinando a IA !!!")

    classificador.fit(X_Treinamento,y_Treinamento)

    print("Treinamento concluido !!!\nScore: ",
          classificador.score(X_Treinamento,y_Treinamento))

    filename = 'Model/sklearn/digits_classifier.joblib.pkl'
    f = open(filename,'wb')
    pickle.dump(classificador, f)

    return classificador

# Treinamento()
# TreinamentoDadosAumentados()
TreinamentoSklearn()