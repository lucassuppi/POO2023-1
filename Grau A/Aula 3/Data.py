import os
os.system('cls'if os.name== 'nt'else'clear')

class Data():
    def __init__(self, dia, mes, ano, cidade):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.cidade = cidade

    def imprimirdata(self):
        if self.mes < 10:
            print(f'{self.dia}/0{self.mes}/{self.ano}')
        else:
            print(f'{self.dia}/{self.mes}/{self.ano}')

    def imprimirtdataporextenso(self):
        meses = {
            1: "janeiro",
            2: "fevereiro",
            3: "março",
            4: "abril",
            5: "maio",
            6: "junho",
            7: "julho",
            8: "agosto",
            9: "setembro",
            10: "outubro",
            11: "novembro",
            12: "dezembro"
        }
        
        print(f"{self.cidade}, {self.dia} de {meses[self.mes]} de {self.ano}")
    
data = Data(14, 3, 2023, 'São Leopoldo') 
data.imprimirdata()
data.imprimirtdataporextenso()





