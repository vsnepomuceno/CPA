import cpa.db.connectorMySql as conn
import utils
import charts
import chartsPanda

def g1Pres():
    totals=list() 
    try:
        totals1=dict()  
        utils.initAddInTotals(totals1)  
        res = conn.executeAllQuery("SELECT c7 , COUNT(*) total FROM tae_presencial GROUP  BY c7")
        for value in res:
            utils.addInTotals(value, totals1)      
        totals.append(totals1)         

        totals2=dict()  
        utils.initAddInTotals(totals2) 
        res = conn.executeAllQuery("SELECT c7 , COUNT(*) total FROM disc_presencial GROUP  BY c7")
        for value in res:
            utils.addInTotals(value, totals2) 
        totals.append(totals2) 

        totals3=dict()  
        utils.initAddInTotals(totals3) 
        res = conn.executeAllQuery("SELECT c6 , COUNT(*) total FROM doc_presencial GROUP  BY c6")
        for value in res:
            utils.addInTotals(value, totals3) 
        totals.append(totals3) 

    except Exception as e:
        print(e)
    
    return totals



def g1EAD():
    totals=list()    
    try:
            
        totals1=dict()  
        utils.initAddInTotals(totals1)  
        res = conn.executeAllQuery("SELECT c7 , COUNT(*) total FROM tae_ead GROUP  BY c7")
        for value in res:
            utils.addInTotals(value, totals1) 
        totals.append(totals1)

        totals2=dict()   
        utils.initAddInTotals(totals2) 
        res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM disc_ead GROUP  BY c8")
        for value in res:
            utils.addInTotals(value, totals2) 
        totals.append(totals2)

        totals3=dict()   
        utils.initAddInTotals(totals3) 
        res = conn.executeAllQuery("SELECT c7 , COUNT(*) total FROM doc_ead GROUP  BY c7")
        for value in res:
            utils.addInTotals(value, totals3) 
        totals.append(totals3)
        

    except Exception as e:
        print(e)
    
    return totals


def plotChartEixo2D1(g, title):
    res = g  
    novoRes = list()

    for i in range(len(res[0].values())):
        barList = list()
        for j in range(len(res)):
            l = list(res[j].values())
            barList.append(l[i])      
        novoRes.append(barList)

    barLabels = list(res[0].keys())

    novoRes = [[0.001 if x == 0 else x for x in row] for row in novoRes]
    chartsPanda.plotChartPd2(["TAE","Discentes","Docentes"],"",barLabels,
                            title, novoRes)



#plotChartEixo2D1(g1Pres(), "Como voc?? avalia seu n??vel de conhecimento a respeito do PDI?")
#plotChartEixo2D1(g1EAD(), "Como voc?? avalia seu n??vel de conhecimento a respeito do PDI?")


def g2Pres():
    totals=list() 
    try:
        totals1=dict()  
        utils.initAddInTotals(totals1)  
        res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM tae_presencial GROUP  BY c8")
        for value in res:
            utils.addInTotals(value, totals1)      
        totals.append(totals1)         

        totals2=dict()  
        utils.initAddInTotals(totals2) 
        res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM disc_presencial GROUP  BY c8")
        for value in res:
            utils.addInTotals(value, totals2) 
        totals.append(totals2) 

        totals3=dict()  
        utils.initAddInTotals(totals3) 
        res = conn.executeAllQuery("SELECT c7 , COUNT(*) total FROM doc_presencial GROUP  BY c7")
        for value in res:
            utils.addInTotals(value, totals3) 
        totals.append(totals3) 

    except Exception as e:
        print(e)
    
    return totals


def g2EAD():
    totals=list()    
    try:
            
        totals1=dict()  
        utils.initAddInTotals(totals1)  
        res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM tae_ead GROUP  BY c8")
        for value in res:
            utils.addInTotals(value, totals1) 
        totals.append(totals1)

        totals2=dict()   
        utils.initAddInTotals(totals2) 
        res = conn.executeAllQuery("SELECT c9 , COUNT(*) total FROM disc_ead GROUP  BY c9")
        for value in res:
            utils.addInTotals(value, totals2) 
        totals.append(totals2)

        totals3=dict()   
        utils.initAddInTotals(totals3) 
        res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM doc_ead GROUP  BY c8")
        for value in res:
            utils.addInTotals(value, totals3) 
        totals.append(totals3)
        

    except Exception as e:
        print(e)
    
    return totals

#plotChartEixo2D1(g2Pres(), 'Como voc?? avalia seu conhecimento a respeito da miss??o institucional, metas e objetivos do PDI.')
#plotChartEixo2D1(g2EAD(), 'Como voc?? avalia seu conhecimento a respeito da miss??o institucional, metas e objetivos do PDI.')

def g3Pres():
    totals=list() 
    try:
        totals1=dict()  
        utils.initAddInTotals2(totals1)  
        res = conn.executeAllQuery("SELECT c9 , COUNT(*) total FROM tae_presencial GROUP  BY c9")
        for value in res:
            utils.addInTotals2(value, totals1)      
        totals.append(totals1)         

        totals2=dict()  
        utils.initAddInTotals2(totals2) 
        res = conn.executeAllQuery("SELECT c9 , COUNT(*) total FROM disc_presencial GROUP  BY c9")
        for value in res:
            utils.addInTotals2(value, totals2) 
        totals.append(totals2) 

        totals3=dict()  
        utils.initAddInTotals2(totals3) 
        res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM doc_presencial GROUP  BY c8")
        for value in res:
            utils.addInTotals2(value, totals3) 
        totals.append(totals3) 

    except Exception as e:
        print(e)
    
    return totals


def g3EAD():
    totals=list()    
    try:
            
        totals1=dict()  
        utils.initAddInTotals2(totals1)  
        res = conn.executeAllQuery("SELECT c9 , COUNT(*) total FROM tae_ead GROUP  BY c9")
        for value in res:
            utils.addInTotals2(value, totals1) 
        totals.append(totals1)

        totals2=dict()   
        utils.initAddInTotals2(totals2) 
        res = conn.executeAllQuery("SELECT c10 , COUNT(*) total FROM disc_ead GROUP  BY c10")
        for value in res:
            utils.addInTotals2(value, totals2) 
        totals.append(totals2)

        totals3=dict()   
        utils.initAddInTotals2(totals3) 
        res = conn.executeAllQuery("SELECT c9 , COUNT(*) total FROM doc_ead GROUP  BY c9")
        for value in res:
            utils.addInTotals2(value, totals3) 
        totals.append(totals3)
        

    except Exception as e:
        print(e)
    
    return totals

def plotChartEixo2D1G3(g, title):
    res = g  
    novoRes = list()

    for i in range(len(res[0].values())):
        barList = list()
        for j in range(len(res)):
            l = list(res[j].values())
            barList.append(l[i])      
        novoRes.append(barList)

    barLabels = list(res[0].keys())

    chartsPanda.plotChartPd7(["TAE","Discentes","Docentes"],"",barLabels,
                            title, novoRes)


#plotChartEixo2D1G3(g3Pres(), 'Como voc?? avalia sua participa????o na elabora????o do PDI?')
#plotChartEixo2D1G3(g3EAD(), 'Como voc?? avalia sua participa????o na elabora????o do PDI?')



def g4PresSearch():
    totals=list()
    try:
        for i in range(12):
            to = dict()
            res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM tae_presencial GROUP  BY c"+str(i+10)+"")
            for value in res:
                utils.addInTotals3(value,to)              
            res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM disc_presencial GROUP  BY c"+str(i+10)+"")
            for value in res:
                utils.addInTotals3(value, to)            
            res = conn.executeAllQuery("SELECT c"+str(i+9)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+9)+"")
            for value in res:
                utils.addInTotals3(value, to)                 
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals


def g4EADSearch():
    totals=list()
    try:
        for i in range(12):
            to = dict()
            
            res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+10)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+11)+" , COUNT(*) total FROM disc_ead GROUP  BY c"+str(i+11)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+10)+"")
            for value in res:
                utils.addInTotals3(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g4Plot(totals):
    ts = totals
    novoTs = list()

    for i in range(len(ts[0].values())):
        barList = list()
        for j in range(len(ts)):
            l = list(ts[j].values())
            barList.append(l[i])      
        novoTs.append(barList)
 
    barLabels = list(ts[0].keys())
    chartsPanda.plotChartPd(['de ensino de gradua????o', 'de ensino de p??s-gradua????o', 'de pesquisa e inicia????o cient??fica', 
                            'de inova????o tecnol??gica', 'de desenvolvimento art??stico e cultural', 'de valoriza????o da diversidade', 
                            'de valoriza????o do meio ambiente','de valoriza????o da mem??ria cultural','de valoriza????o do patrim??nio cultural',
                            'de valoriza????o da produ????o art??stica', 'dos direitos humanos e da igualdade ??tnico-racial','de valoriza????o da educa????o a dist??ncia'],
                        'Total de Respostas',barLabels, 
                        'Avalia????o do alinhamento entre as pol??ticas institucionais expressas no PDI e as atividades.',
                        novoTs)



res = g4PresSearch()
print(res)
#res = g4EADSearch()
g4Plot(res)