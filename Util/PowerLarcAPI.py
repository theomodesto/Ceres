from Model.Clima import *
import requests
import pandas as pd
from datetime import datetime


def GetDadosAPI(lat,lon,ano):

    mediaEstacoes = {}

    resp = requests.get('https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?' 
                        'request=execute&' \
                        'identifier=SinglePoint&' \
                        'parameters=T2M,RH2M,PRECTOT&' \
                        'userCommunity=SSE&' \
                        'tempAverage=DAILY&' \
                        'outputList=JSON&' \
                        'user=anonymous&' \
                        'startDate='+str(ano)+'0320'+
                        '&endDate='+str(ano+1)+'0320'+
                        '&lat='+str(lat)+
                        '&lon='+str(lon))

    jsonResp = resp.json()

    OutonoInicio = datetime(ano, 3, 20)
    OutonoFinal = datetime(ano, 6, 20)
    InvernoIncio = datetime(ano, 6, 21)
    InvernoFinal = datetime(ano, 9, 22)
    PrimaveraInicio = datetime(ano, 9, 22)
    PrimaveraFinal = datetime(ano, 12, 21)
    VeraoInicio = datetime(ano, 12, 22)
    VeraoFinal = datetime(ano + 1, 3, 20)

    Outono = []
    Inverno = []
    Primavera = []
    Verao = []
    for f in jsonResp['features']:
        temp = f['properties']['parameter']['T2M']
        umid = f['properties']['parameter']['RH2M']
        prec = f['properties']['parameter']['PRECTOT']
        for key in temp:
            date = datetime.strptime(key, '%Y%m%d')
            if date > OutonoInicio and date < OutonoFinal:
                Outono.append({"TemMed":temp[key], "UmiMed":umid[key], "Prec":prec[key]})
            elif date > InvernoIncio and date < InvernoFinal:
                Inverno.append({"TemMed":temp[key], "UmiMed":umid[key], "Prec":prec[key]})
            elif date > PrimaveraInicio and date < PrimaveraFinal:
                Primavera.append({"TemMed":temp[key], "UmiMed":umid[key], "Prec":prec[key]})
            elif date > VeraoInicio and date < VeraoFinal:
                Verao.append({"TemMed":temp[key], "UmiMed":umid[key], "Prec":prec[key]})

    mediaEstacoes['Outono'] = MediaClima(Outono)
    mediaEstacoes['Inverno'] = MediaClima(Inverno)
    mediaEstacoes['Primavera'] = MediaClima(Primavera)
    mediaEstacoes['Verao'] = MediaClima(Verao)

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



