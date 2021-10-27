def bissexto(recebimento, antecipado):

    pago_mes = recebimento.split("/")[1]
    pago_ano = recebimento.split("/")[2]
    antecipacao_mes = antecipado.split("/")[1]

    if pago_mes == "02":
        if int(pago_ano) % 400 == 0 or int(pago_ano) % 4 == 0 and int(pago_ano) % 100 != 0:
            if pago_mes < antecipacao_mes:
                #print("Bissexto - Meses diferentes")
                return True
            else: 
                return False

#CALCULANDO A QUANTIDADE DE DIAS
def quant_dias(ano, recebimento, antecipado):
    
    pago_dia = recebimento.split("/")[0]
    pago_mes = recebimento.split("/")[1]
    antecipacao_dia = antecipado.split("/")[0]
    antecipacao_mes = antecipado.split("/")[1]
   
    if ano == True:
        #print("Mes com 29 dias")
        return int(antecipacao_dia) + (29 - int(pago_dia))
    
    else:
        if pago_mes < antecipacao_mes or pago_mes > antecipacao_mes:
            if pago_mes == "04" or pago_mes == "06" or pago_mes == "09" or pago_mes == "11":
                print("Mes com 30 dias")
                return int(antecipacao_dia) + (30 - int(pago_dia))
            elif pago_mes == "02":
                #print("Mes com 28 dias")
                return int(antecipacao_dia) + (28 - int(pago_dia))
            else:
                #print("Mes com 31 dias")
                return int(antecipacao_dia) + (31 - int(pago_dia))

        #CASO A FATURA E A ANTECIPAÇÃO ESTEJAM NO MESMO MES
        if pago_mes == antecipacao_mes:
            #print("Sub com o mesmo mes")
            return int(antecipacao_dia) - int(pago_dia)

#CALCULANDO O VALOR DA ANTECIPAÇÃO
def valor(taxa_eduzz, dias, fatura):
    porcentagem = taxa_eduzz + (30-int(dias))*0.1
    valor = float(fatura) * (float(porcentagem)/100)
    return float(valor)

#CALCULANDO O VALOR DA PORCENTAGEM
def porcentagem_taxa(dias, taxa_eduzz):
    porcentagem = taxa_eduzz + (30-int(dias))*0.1
    return porcentagem