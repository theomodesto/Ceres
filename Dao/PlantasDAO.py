from Model.DadosTreinamentoPlanta import *
from Util.SingletonConnection import *

def SetPlantas(Planta):
    Connection('Plantas').insert({"Nome":Planta.Nome,})
    return True