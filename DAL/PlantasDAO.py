from Util.SingletonConnection import *

def gravarPlantaNoBanco(Planta):
    if(verificarPlantaNoBanco(Planta.nome)):
		try:
			Connection('Plantas').insert({
			"idPlanta":Planta.idPlanta,
			"Nome": Planta.nome,
			"Categoria": Planta.categoria ,
			"Foto": Planta.foto,
			"Descricao": Planta.descricao,
			"Tempo": Planta.tempo,
			"Nutrientes": Planta.nutrientes,
			"Calorias": Planta.calorias,
			"Passos": Planta.passos
			})
			return True

		except Exception:
			print(Exception)
			return False

    else:
        return False

def retornaPlantasPorNome(nomePlanta):
	cursor = Connection('Plantas').find({'Nome':nomePlanta})
	return cursor

def retornaPlantasPorId(id):
	cursor = Connection('Plantas').find({'idPlanta':id})
	return cursor

def verificarPlantaNoBanco(nomePlanta):
    if(list(Connection('Plantas').find({'Nome':nomePlanta})) == []):
        return True
    return False