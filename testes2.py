from datetime import datetime

class entrada:
    def __init__(self, get_ha, ha, he, get_he):
        self.get_ha = get_ha
        self.ha = ha
        self.he = he
        self.get_ha = ha

    def get_hora(self):
        self.get_ha = datetime.now()
        self.get_ha = self.get_ha.strftime("%d/%m/%Y %H:%M")  # define formatação do data e horas
        print(self.get_ha)
        self.ha = input("deseja usar o dia e hora atual, sim ou não?")  # ha == hora atual pega o horario e data atual
        if self.ha == "sim":
            print("Hora de entrada:", self.get_ha, "Bom dia de trabalho!")
        if self.ha == "não":
            print("Insira abaixo o horario que deseja  neste formato: DIA/MES/ANO HR:MIN ")
            self.he = input()
            self.get_he = datetime.strptime(self.he, "%d/%m/%Y %H:%M")
            print("Hora de entrada:", self.get_he, "Bom dia de trabalho!")
    
class saida:
    def __init__(self, hs_t, hs_a, get_hs_a, hs_m, get_hs_m):
        self.hs_t = hs_t
        self.hs_a = hs_a
        self.get_hs_a = get_hs_a
        self.hs_m = hs_m
        self.get_hs_m = get_hs_m