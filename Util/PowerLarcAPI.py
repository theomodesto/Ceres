from Model.Clima import *
import requests

def GetDadosAPI():
    resp = requests.get('https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?request=execute&identifier=SinglePoint&parameters=T2M,PS,ALLSKY_SFC_SW_DWN&startDate=20160301&endDate=20160331&userCommunity=SSE&tempAverage=DAILY&outputList=JSON,ASCII&lat=36&lon=45&user=anonymous')
    print(resp)
    for c in resp.json():
       print(c)

GetDadosAPI()