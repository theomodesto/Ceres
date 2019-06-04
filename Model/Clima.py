from Model.Localizacao import *

class Clima:
    def __init__(self,TemMin,TemMax,UmiMin,UmiMax,Localizacao):
        self.TemMin = TemMin
        self.TemMax = TemMax
        self.UmiMin = UmiMin
        self.UmiMax = UmiMax
        self.Localizacao = Localizacao