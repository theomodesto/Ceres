import datetime

from Model.DadosTreinamentoPlanta import *
from Dao.PlantasDAO import *
from Model.Planta import Planta

planta = Planta(1,'Merda','Shit','Opa',"Muito usado no sushi","4 Dias","Muitos",5,["Planta","Espera","Colhe"])

if(gravarPlantaNoBanco(planta)):
    print("Deu boa")
else:
    print("Não deu")

for plantas in retornaPlantasPorNome('Arroz'):
    print(plantas)



