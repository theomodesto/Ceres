from Model.Clima import *
import requests
import json

from Util.ParserJsonAPI import ParseJson

def GetDadosAPI(lat,lon,dataInicio,dataFinal):
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
    print(jsonResp)
    for f in jsonResp['features']:
        temp = f['properties']['parameter']['T2M']
        umid = f['properties']['parameter']['RH2M']
        prec = f['properties']['parameter']['PRECTOT']
        for key in temp:
            print("TemMed:"+str(temp[key])+" UmiMed:"+str(umid[key])+" Prec:"+str(prec[key]))

def MediaClima(DadosClima):
    pass

GetDadosAPI(35,40,20160301,20160331)

