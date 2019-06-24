# import requests
# from datetime import datetime
# ano = datetime.year()
# resp = requests.get('https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?'+
#                     'request=execute&' +
#                     'identifier=SinglePoint&' +
#                     'parameters=T2M,RH2M,PRECTOT&' +
#                     'userCommunity=SSE&' +
#                     'tempAverage=DAILY&' +
#                     'outputList=JSON&' +
#                     'user=anonymous&' +
#                     'startDate='+str(ano)+'0320'+
#                     '&endDate='+str(ano+1)+'0320'+
#                     '&lat=-25.369695'+
#                     '&lon=-49.466263'
#                     )
#
# jsonResp = resp.json()
#
# OutonoInicio = datetime(ano, 3, 20)
# OutonoFinal = datetime(ano, 6, 20)
# InvernoIncio = datetime(ano, 6, 21)
# InvernoFinal = datetime(ano, 9, 22)
# PrimaveraInicio = datetime(ano, 9, 22)
# PrimaveraFinal = datetime(ano, 12, 21)
# VeraoInicio = datetime(ano, 12, 22)
# VeraoFinal = datetime(ano+1, 3, 20)
#
# for f in jsonResp['features']:
#     temp = f['properties']['parameter']['T2M']
#     umid = f['properties']['parameter']['RH2M']
#     prec = f['properties']['parameter']['PRECTOT']
#     for key in prec:
#         date = datetime.strptime(key, '%Y%m%d')
#         if date > OutonoInicio and date < OutonoFinal :
#             print(date)

from DAL.PlantasDAO import *

print(retornaPlantasPorId(1))