from MODEL.Classificador import *
import pandas as pd
import tensorflow as tf


X_teste = pd.DataFrame(data=[[17.02,20.0,10.89,90],[15,25,75,75]])


funTeste = tf.estimator.inputs.pandas_input_fn( x=X_teste,
                                                batch_size=1,
                                                shuffle=False)
classificador = TreinamentoTensorFlow()
prev = classificador.predict(input_fn=funTeste)


print(prev)