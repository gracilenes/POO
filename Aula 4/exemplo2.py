class Aluno:
    def __init__(self):
        self.__matricula = "202412040003"
        self.__nome = "Gracilene"
        self.__media_final = 85
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def media_final(self):
        return self.__media_final
    
    @media_final.setter
    def media_final(self, media_final):
        self.__media_final = media_final

