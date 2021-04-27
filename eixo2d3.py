import db.connectorMySql as conn
import utils
import charts
import chartsPanda

""" 
“Em relação a responsabilidade social do IFPE, avalie o alinhamento entre as 
políticas institucionais expressas no PDI quanto:” Gráfico de colunas 100% empilhadas, 
com participação dos três segmentos da comunidade. Com dados de todos os Campi presenciais em conjunto.
Eixo x = conteúdo das linhas, ao todo são 6, 
ex: ao desenvolvimento econômico, ao desenvolvimento social.... 
Eixo y = percentuais (de 0 a 100%). 
Colunas com cores e rótulos com percentuais de “ótimo (verde), bom (azul claro), 
regular (amarela), ruim (laranja), péssimo (vermelha), Inexistente / Desconheço (cinza), 
Não se aplica (preta)”.
 """
def g1EAD():
    totals=list()
    try:
        for i in range(6):
            to = dict()
            
            res = conn.executeAllQuery("SELECT c"+str(i+23)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+23)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+24)+" , COUNT(*) total FROM disc_ead GROUP  BY c"+str(i+24)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+23)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+23)+"")
            for value in res:
                utils.addInTotals3(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g1Pres():
    totals=list()
    try:
        for i in range(6):
            to = dict()
            
            res = conn.executeAllQuery("SELECT c"+str(i+23)+" , COUNT(*) total FROM tae_presencial GROUP  BY c"+str(i+23)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+23)+" , COUNT(*) total FROM disc_presencial GROUP  BY c"+str(i+23)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+22)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+22)+"")
            for value in res:
                utils.addInTotals3(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def gPlot(totals):
    ts = totals
    novoTs = list()

    for i in range(len(ts[0].values())):
        barList = list()
        for j in range(len(ts)):
            l = list(ts[j].values())
            barList.append(l[i])      
        novoTs.append(barList)
 
    barLabels = list(ts[0].keys())
    chartsPanda.plotChartPd(['ao desenvolvimento econômico',
                            'ao desenvolvimento social',
                            'à melhoria de vida da população',
                            'à ações de inclusão',
                            'à ações de empreendedorismo',
                            'à ações exitosas e inovadoras'],
                        'Total de Respostas',barLabels, 
                        'Em relação a responsabilidade social do IFPE, avalie o alinhamento entre as políticas institucionais expressas no PDI quanto:',
                        novoTs)



#res = g1Pres()
#gPlot(res)

"""
“Você é professor / servidor efetivo do IFPE?” 
Gráfico de colunas agrupadas, com participação dos dois segmentos da comunidade (docente e TAE). 
Com dados de todos os Polos EAD em conjunto. 
Cada segmento (docente, tae) será representado em dupla coluna no eixo x, 
cada coluna com as respostas “sim” ou “não”. 
Eixo y = percentuais (de 0 a 100%).
"""
def g2EAD():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals4(dict1)
        res = conn.executeAllQuery("SELECT c30 , COUNT(*) total FROM tae_ead GROUP  BY c30")
        for value in res:
            utils.addInTotals4(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals4(dict2)
        res = conn.executeAllQuery("SELECT c30 , COUNT(*) total FROM doc_ead GROUP  BY c30")
        for value in res:
            utils.addInTotals4(value, dict2) 
        totals.append(dict2)

    except Exception as e:
        print(e)
    
    return totals

ts = g2EAD()
charts.plotChartDuplo(ts[0].keys(), '', 
    '1. Você é servidor efetivo do IFPE?', ts[0].values(), ts[1].values())