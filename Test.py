from DAL.PlantasDAO import *
planta = list(retornaPlantasPorId(1))
print(planta[0]["Passos"])