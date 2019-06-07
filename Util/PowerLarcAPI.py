from Model.Clima import *
import requests

from Util.ParserJsonAPI import ParseJson


def GetDadosAPI(lat,lon,dataInicio,dataFinal):
    resp = requests.get('https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?' 
                        'request=execute&' \
                        'identifier=SinglePoint&' \
                        'parameters=T2M,PS,ALLSKY_SFC_SW_DWN&' \
                        'userCommunity=SSE&' \
                        'tempAverage=DAILY&' \
                        'outputList=JSON&' \
                        'user=anonymous&' \
                        'startDate='+str(dataInicio)+
                        '&endDate='+str(dataFinal)+
                        '&lat='+str(lat)+
                        '&lon='+str(lon))
    jsonResp = resp.json()
    
    for f in jsonResp['features']:
        clima = f['properties']['parameter']['T2M']
        print(clima)


GetDadosAPI(35,40,20160301,20160331)

