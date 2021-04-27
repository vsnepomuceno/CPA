import db.connectorMySql as conn
import utils
import charts
import chartsPanda


def g1Pres():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals4(dict1)
        res = conn.executeAllQuery("SELECT c97 , COUNT(*) total FROM tae_presencial GROUP  BY c97")
        for value in res:
            utils.addInTotals4(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals4(dict2)
        res = conn.executeAllQuery("SELECT c96 , COUNT(*) total FROM doc_presencial GROUP  BY c96")
        for value in res:
            utils.addInTotals4(value, dict2) 
        totals.append(dict2)

        dict3 = dict()
        utils.initAddInTotals4(dict3)
        res = conn.executeAllQuery("SELECT c42 , COUNT(*) total FROM disc_presencial GROUP  BY c42")
        for value in res:
            utils.addInTotals4(value, dict3) 
        totals.append(dict3)

    except Exception as e:
        print(e)
    
    return totals

def g1EAD():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals4(dict1)
        res = conn.executeAllQuery("SELECT c105 , COUNT(*) total FROM tae_ead GROUP  BY c105")
        for value in res:
            utils.addInTotals4(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals4(dict2)
        res = conn.executeAllQuery("SELECT c105 , COUNT(*) total FROM doc_ead GROUP  BY c105")
        for value in res:
            utils.addInTotals4(value, dict2) 
        totals.append(dict2)

        dict2 = dict()
        utils.initAddInTotals4(dict2)
        res = conn.executeAllQuery("SELECT c47 , COUNT(*) total FROM disc_ead GROUP  BY c47")
        for value in res:
            utils.addInTotals4(value, dict2) 
        totals.append(dict2)

    except Exception as e:
        print(e)
    
    return totals


#ts = g1Pres()
#charts.plotChartTriplo(ts[0].keys(), '', 
#    'Você conhece as fontes de captação de recursos do IFPE?', ts[0].values(), ts[1].values(), ts[2].values())

#ts = g1EAD()
#charts.plotChartTriplo(ts[0].keys(), '', 
#    'Você conhece as fontes de captação de recursos do IFPE?', ts[0].values(), ts[1].values(), ts[2].values())

def g2EAD():
    totals=list()
    try:
        for i in range(4):
            to = dict()
            utils.initAddInTotals15(to)

            res = conn.executeAllQuery("SELECT c"+str(i+106)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+106)+"")
            for value in res:
                utils.addInTotals15(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+106)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+106)+"")
            for value in res:
                utils.addInTotals15(value, to)

            res = conn.executeAllQuery("SELECT c"+str(i+48)+" , COUNT(*) total FROM disc_ead GROUP  BY c"+str(i+48)+"")
            for value in res:
                utils.addInTotals15(value, to)  

            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g2Pres():
    totals=list()
    try:
        for i in range(4):
            to = dict()
            utils.initAddInTotals15(to) 

            res = conn.executeAllQuery("SELECT c"+str(i+98)+" , COUNT(*) total FROM tae_presencial GROUP  BY c"+str(i+98)+"")
            for value in res:
                utils.addInTotals15(value, to) 
                     
            res = conn.executeAllQuery("SELECT c"+str(i+97)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+97)+"")
            for value in res:
                utils.addInTotals15(value, to)       
            
            res = conn.executeAllQuery("SELECT c"+str(i+43)+" , COUNT(*) total FROM disc_presencial GROUP  BY c"+str(i+43)+"")
            for value in res:
                utils.addInTotals15(value, to) 

            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g2Plot(totals):
    ts = totals
    novoTs = list()

    for i in range(len(ts[0].values())):
        barList = list()
        for j in range(len(ts)):
            l = list(ts[j].values())
            barList.append(l[i])      
        novoTs.append(barList)
 
    barLabels = list(ts[0].keys())
    chartsPanda.plotChartPd10(['Se o planejamento orç ... (ensino) é adequado',
                             'Se o planejamento orç ... (pesquisa) é adequado',
                             'Se o planejamento orç ... (extensão) é adequado',
                             'Se o planejamento orç ... combate ao COVID é coerente'],
                        'Total de Respostas',barLabels, 
                        'Sobre sustentabilidade financeira, na perspectiva da relação com o desenvolvimento institucional, avalie:',
                        novoTs)

#g2Plot(g2Pres())
#g2Plot(g2EAD())


def g3EAD():
    totals=list()
    try:
        for i in range(3):
            to = dict()
            utils.initAddInTotals16(to)

            res = conn.executeAllQuery("SELECT c"+str(i+110)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+110)+"")
            for value in res:
                utils.addInTotals16(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+110)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+110)+"")
            for value in res:
                utils.addInTotals16(value, to)

            res = conn.executeAllQuery("SELECT c"+str(i+52)+" , COUNT(*) total FROM disc_ead GROUP  BY c"+str(i+52)+"")
            for value in res:
                utils.addInTotals16(value, to)  

            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g3Pres():
    totals=list()
    try:
        for i in range(3):
            to = dict()
            utils.initAddInTotals16(to) 

            res = conn.executeAllQuery("SELECT c"+str(i+102)+" , COUNT(*) total FROM tae_presencial GROUP  BY c"+str(i+102)+"")
            for value in res:
                utils.addInTotals16(value, to) 
                     
            res = conn.executeAllQuery("SELECT c"+str(i+101)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+101)+"")
            for value in res:
                utils.addInTotals16(value, to)       
            
            res = conn.executeAllQuery("SELECT c"+str(i+47)+" , COUNT(*) total FROM disc_presencial GROUP  BY c"+str(i+47)+"")
            for value in res:
                utils.addInTotals16(value, to) 

            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g3Plot(totals):
    ts = totals
    novoTs = list()

    for i in range(len(ts[0].values())):
        barList = list()
        for j in range(len(ts)):
            l = list(ts[j].values())
            barList.append(l[i])      
        novoTs.append(barList)
 
    barLabels = list(ts[0].keys())
    chartsPanda.plotChartPd11(['Você conhece o orçamento do IFPE',
                             'Você participa do planejamento do orçamento',
                             'Você acompanha a aplicação do orçamento'],
                        'Total de Respostas',barLabels, 
                        'Sobre sustentabilidade financeira, na perspectiva da participação da comunidade interna. Avalie:',
                        novoTs)

g3Plot(g3Pres())
g3Plot(g3EAD())