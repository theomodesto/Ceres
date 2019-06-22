from Model.Clima import *
import requests
import pandas as pd

def GetDadosAPI(lat,lon,ano):

    estacoes = {
        "Outono": {"Inicio": str(ano) + "0320", "Final": str(ano) + "0620"},
        "Inverno": {"Inicio": str(ano) + "0621", "Final": str(ano) + "0922"},
        "Primavera": {"Inicio": str(ano) + "0922", "Final": str(ano) + "1221"},
        "Verao": {"Inicio": str(ano) +"1222", "Final":str((ano+1)) + "0320"}
    }

    mediaEstacoes = {}
    for estacao in estacoes:
        resp = requests.get('https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?' 
                            'request=execute&' \
                            'identifier=SinglePoint&' \
                            'parameters=T2M,RH2M,PRECTOT&' \
                            'userCommunity=SSE&' \
                            'tempAverage=DAILY&' \
                            'outputList=JSON&' \
                            'user=anonymous&' \
                            'startDate='+str(estacoes[estacao]["Inicio"])+
                            '&endDate='+str(estacoes[estacao]["Final"])+
                            '&lat='+str(lat)+
                            '&lon='+str(lon))

        jsonResp = resp.json()

        dadosClima = []
        for f in jsonResp['features']:
            temp = f['properties']['parameter']['T2M']
            umid = f['properties']['parameter']['RH2M']
            prec = f['properties']['parameter']['PRECTOT']
            for key in temp:
                dadosClima.append({"TemMed":temp[key], "UmiMed":umid[key], "Prec":prec[key]})

        mediaEstacoes[estacao] = MediaClima(dadosClima)

    # MediasPandas = pd.DataFrame.from_dict(mediaEstacoes)

    return mediaEstacoes

def MediaClima(DadosClima):

    quantidade = len(DadosClima)
    somaTem = 0
    somaUmi = 0
    somaPrec = 0

    for clima in DadosClima:
        somaTem = somaTem + clima['TemMed']
        somaUmi = somaUmi + clima['UmiMed']
        somaPrec = somaPrec + clima['Prec']

    mediaTem = somaTem/quantidade
    mediaUmi = somaUmi/quantidade
    mediaPrec = ((somaPrec/quantidade)*100)

    dictMedia = {}

    dictMedia["Tem"] = mediaTem
    dictMedia["Umi"] = mediaUmi
    dictMedia["Prec"] = mediaPrec

    return dictMedia

# print(GetDadosAPI(-25.364296,-49.434763,2016))



