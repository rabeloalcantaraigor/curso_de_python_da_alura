
class Data:
    def __init__(self, dia, mes, ano) -> None:
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatdata(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')
    
data = Data(21,11,2007)
data.formatdata()
        