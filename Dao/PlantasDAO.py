from Util.SingletonConnection import *

def gravarPlantaNoBanco(Planta):

    if(verificarPlantaNoBanco(Planta.nome)):
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
    else:
        return False

def verificarPlantaNoBanco(nomePlanta):
    opa = Connection('Plantas').find({"Nome": nomePlanta})
    print(opa)
    if(Connection('Plantas').find({"Nome":nomePlanta}) == None):
        return True

    return False