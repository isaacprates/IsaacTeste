from datetime import datetime

class hora_entrada_saida:
    def entrada():
        get_ha = datetime.now()
        get_ha = get_ha.strftime("%d/%m/%Y %H:%M")  # define formatação do data e horas
        print(get_ha)
        ha = input("deseja usar o dia e hora atual, sim ou não?")  # ha == hora atual pega o horario e data atual
        if ha == "sim":
            print("Hora de entrada:", get_ha, "Bom dia de trabalho!")
            pass
        if ha == "não":
            print("Insira abaixo o horario que deseja  neste formato: DIA/MES/ANO HR:MIN ")
            he = input()
            get_he = datetime.strptime(he, "%d/%m/%Y %H:%M")
            print("Hora de entrada:", get_he, "Bom dia de trabalho!")
            pass
    entrada()

    def saida():
        hs_t = input("Digite 'terminei' se quiser adicionar hora de saida:")
        if hs_t == "terminei":
            hs_a = input("deseja usar a hora atual como a de saida, sim ou não?")
            get_hs_a = datetime.now()
            get_hs_a.strftime("%d/%m/%Y %H:%M")  # define formatação do data e horas
            if hs_a == "sim":
                print(get_hs_a, "Esta é a hora de saida, Até amanhã")
                pass
            if hs_a == "não":
                print("Insira abaixo o horario que deseja neste formato: DIA/MES/ANO HR:MIN ")
                hs_m = input()
                get_hs_m = datetime.strptime(hs_m, "%d/%m/%Y %H:%M")
                print("Esta é a sua hora de saida:", get_hs_m, "Até amanhã")
                pass
    saida()
