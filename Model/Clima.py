from Model.Localizacao import *

class Clima(Localizacao):
    def __init__(self,TemMedia,UmidadeMedia,Localizacao):
        self.temMedia = TemMedia
        self.umidadeMedia = UmidadeMedia
        self.localizacao = Localizacao