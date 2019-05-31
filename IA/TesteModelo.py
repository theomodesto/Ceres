from IA.Classificador import *
import pandas as pd
import tensorflow as tf

dadosDic = [{"TemMin":20,"TemMax":30, "Umidaderelativamin":10,"Umidaderelativamax":50}]

X_teste = pd.DataFrame(data=dadosDic)

funTeste = tf.estimator.inputs.pandas_input_fn(x=X_teste,
                                               batch_size=1,
                                               shuffle=False)
# TreinamentoTensorFlow()

with tf.Session() as sess:
    saver = tf.train.import_meta_graph('Model/model.ckpt-200.meta')
    saver.restore(sess, tf.train.latest_checkpoint(checkpoint_dir='Model',latest_filename='model.ckpt-200.data-00000-of-00001'))

    graph = tf.get_default_graph()
    input_x = graph.get_tensor_by_name("input_x:0")
    result = graph.get_tensor_by_name("result:0")

    feed_dict = {input_x: X_teste,}

    predictions = result.eval(feed_dict=feed_dict)