from Model.Clima import *
import requests
import pandas as pd

def GetDadosAPI(lat,lon,dataInicio,dataFinal):
    ano = "2018"
    estacoes = {
        "Outono": {"Inicio": ano + "0320", "Final": ano + "0620"},
        "Inverno": {"Inicio": ano + "0621", "Final": ano + "0922"},
        "Primavera": {"Inicio": ano + "0922", "Final": ano + "1221"},
        "Verão": {"Inicio": ano + "01222", "Final": ano + "0320"}
    }

    resp = requests.get('https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?' 
                        'request=execute&' \
                        'identifier=SinglePoint&' \
                        'parameters=T2M,RH2M,PRECTOT&' \
                        'userCommunity=SSE&' \
                        'tempAverage=DAILY&' \
                        'outputList=JSON&' \
                        'user=anonymous&' \
                        'startDate='+str(dataInicio)+
                        '&endDate='+str(dataFinal)+
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
    return MediaClima(dadosClima)

def MediaClima(DadosClima):
    quantidade = len(DadosClima)
    somaTem = 0
    somaUmi = 0
    somaPrec = 0
    for clima in DadosClima:
        somaTem = somaTem + clima['TemMed']
        somaUmi = somaUmi + clima['UmiMed']
        somaPrec = somaPrec + clima['Prec']
    print("MediaTem",somaTem/quantidade)
    mediaTem = somaTem/quantidade
    print("MediaUmi",somaUmi/quantidade)
    mediaUmi = somaUmi/quantidade
    print("MediaPrec",somaPrec/quantidade)
    mediaPrec = somaPrec/quantidade

    dictMedia = {}

    dictMedia['Tem'] = mediaTem
    dictMedia['Umi'] = mediaUmi
    dictMedia['Prec'] = mediaPrec

    dados = pd.DataFrame.from_dict(data=dictMedia)
    print(dados)
    return dados

# GetDadosAPI(35,40,20160301,20160331)




