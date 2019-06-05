from Model.Localizacao import *

class Clima(Localizacao):
    def __init__(self,TemMin,TemMax,UmiMin,UmiMax,Localizacao):
        self.temMin = TemMin
        self.temMax = TemMax
        self.umiMin = UmiMin
        self.umiMax = UmiMax
        self.localizacao = Localizacao