from Model.DadosTreinamentoPlanta import *
from Dao.PlantasDAO import *
from Model.Planta import Planta

planta = Planta('Arroz',21,21,12,12,0.8)
print(type(planta))
SetPlantas(planta)

