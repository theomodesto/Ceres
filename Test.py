from Model.Plantio import *
from Model.Planta import *
from Model.Clima import *
from IA.DadosTreinamento import *

DadosPlantas()

planta = Planta('Arroz',21,21,12,12,0.8)
plantio = Plantio(planta,['Terra','Agua'])
print("Nome: "+plantio.Planta.Nome+" Passos: "+str(plantio.Passos))
