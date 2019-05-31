from MODEL.Classificador import *
import pandas as pd
import tensorflow as tf

dadosDic = {}

dadosDic = [{ "TemMin":20,"TemMax":30, "Umidaderelativamin":10,"Umidaderelativamax":50}]

# X_teste = pd.DataFrame(data=[[17,20,10,90],[15,25,75,75]])
X_teste = pd.DataFrame(data=dadosDic)

funTeste = tf.estimator.inputs.pandas_input_fn( x=X_teste,
                                                batch_size=1,
                                                shuffle=False)
classificador = TreinamentoTensorFlow()
valores = []
for p in classificador.predict(input_fn=funTeste):
    valores.append(p['class_ids'][0])
    print(p['class_ids'][0])
