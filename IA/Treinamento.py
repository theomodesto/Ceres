from IA.DadosTreinamento import *
from IA.Classificador import *
import pickle
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from Util.NormalizacaoDados import *

steps = 50000

def Treinamento():

    X_Treinamento, y_Treinamento = DadosPlantasAumentados()

    # X_Treinamento = EscalonamentoDados(X_Treinamento)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X_Treinamento,
                                                        y_Treinamento,
                                                        test_size=0.1,
                                                        random_state=42)

    funcao_treinamento = tf.estimator.inputs.pandas_input_fn(x=X_train,
                                                             y=y_train,
                                                             batch_size=32,
                                                             num_epochs=None,
                                                             shuffle=False)

    funcao_teste = tf.estimator.inputs.pandas_input_fn(x=X_test,
                                                       y=y_test,
                                                       batch_size=32,
                                                       num_epochs=None,
                                                       shuffle=False)

    # numPlantas = len(list(set(y_Treinamento)))+1

    classificador = Classificador()

    print("Treinando a IA !!!")

    classificador.train(input_fn=funcao_treinamento, steps=steps)

    eval = classificador.evaluate(input_fn=funcao_teste, steps=steps)

    print("Treinamento concluido !!!\nScore:", eval)

    return True

def TreinamentoSklearn():
    X_Treinamento, y_Treinamento = DadosPlantasAumentados()

    X_Treinamento = EscalonamentoDados(X_Treinamento)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X_Treinamento, y_Treinamento, test_size=0.3, random_state=42)

    classificador = ClassificadorSklearn()

    print("Treinando a IA !!!")

    classificador.fit(X_train, y_train)

    print("Treinamento concluido !!!\n"
          "Score: ",
          classificador.score(X_test,y_test))

    predict = classificador.predict(X_test)

    from sklearn.metrics import accuracy_score
    from sklearn.metrics import mean_absolute_error

    print("Accuracy: "+str(accuracy_score(y_test,predict)))
    print("MAE: "+str(mean_absolute_error(y_test,predict)))

    filename = 'Model/sklearn/digits_classifier.joblib.pkl'
    f = open(filename,'wb')
    pickle.dump(classificador, f)

    return classificador
