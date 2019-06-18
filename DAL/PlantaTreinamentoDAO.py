from DAL.ConnectionMongoDB import *


def gravarPlantaNoBanco(PlantaTreinamento):
    if (verificarPlantaNoBancoPorID(PlantaTreinamento.idPlanta)):
        Connection('PlantasTreinamento').insert({
        "idPlanta":PlantaTreinamento.idPlanta,
        "Nome":PlantaTreinamento.nome,
        "UmMin":PlantaTreinamento.umMin,
        "UmMax":PlantaTreinamento.umMax,
        "TempMin":PlantaTreinamento.tempMin,
        "TempMax":PlantaTreinamento.tempMax,
         })
        return True

    return False


def retornaTodasAsPlantasTreinamento():
    cursor = Connection('PlantasTreinamento').find()
    return cursor


def retornaPlantasTreinamentoPorNome(nomePlanta):
    cursor = Connection('PlantasTreinamento').find({'Nome': nomePlanta})
    return cursor


def retornaPlantasTreinamentoPorId(id):
    cursor = Connection('PlantasTreinamento').find({'idPlanta': id})
    return cursor


def deletePlantaPorId(idPlanta):
    Connection('PlantasTreinamento').delete_one({'idPlanta': idPlanta})


def updatePlantasTreinamento(PlantaTreinamento):
    Connection('PlantasTreinamento').update({'idPlanta': PlantaTreinamento.idPlanta}, {'$set': {	
                                                                                        "idPlanta":PlantaTreinamento.idPlanta,
                                                                                        "Nome":PlantaTreinamento.nome,
                                                                                        "UmMin":PlantaTreinamento.umMin,
                                                                                        "UmMax":PlantaTreinamento.umMax,
                                                                                        "TempMin":PlantaTreinamento.tempMin,
                                                                                        "TempMax":PlantaTreinamento.tempMax,
                                                                                    }})


def verificarPlantaNoBancoPorID(idPlanta):
    if (list(Connection('PlantasTreinamento').find({'idPlanta': idPlanta})) == []):
        return True
    return False