import db.connectorMySql as conn
import utils
import charts
import chartsPanda


def g1EAD():
    totals=list()
    try:
        for i in range(6):
            to = dict()
            utils.initAddInTotals3(to)
            res = conn.executeAllQuery("SELECT c"+str(i+31)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+31)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+31)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+31)+"")
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
            
            res = conn.executeAllQuery("SELECT c"+str(i+30)+" , COUNT(*) total FROM tae_presencial GROUP  BY c"+str(i+30)+"")
            for value in res:
                utils.addInTotals3(value, to) 
                     
            res = conn.executeAllQuery("SELECT c"+str(i+29)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+29)+"")
            for value in res:
                utils.addInTotals3(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g1Plot(totals):
    ts = totals
    novoTs = list()

    for i in range(len(ts[0].values())):
        barList = list()
        for j in range(len(ts)):
            l = list(ts[j].values())
            barList.append(l[i])      
        novoTs.append(barList)
 
    barLabels = list(ts[0].keys())
    chartsPanda.plotChartPd(['o incentivo em suas iniciativas de formação',
                            'a garantia do acesso de ... internos',
                            'a garantia do acesso de ... externos',
                            'a implementação de um programa ... concursados/as',
                            'o incentivo e apoio às iniciativas ... do IFPE',
                            'o incentivo ao desenvolvimento ... parcerias'],
                        'Total de Respostas',barLabels, 
                        'Quanto a formação continuada de servidores do IFPE, como você avalia:',
                        novoTs)



#res = g1EAD()
#g1Plot(res)

def g2Pres():
    totals=list() 
    try:
        totals1=dict()  
        utils.initAddInTotals9(totals1)  
        res = conn.executeAllQuery("SELECT c36 , COUNT(*) total FROM tae_presencial GROUP  BY c36")
        for value in res:
            utils.addInTotals9(value, totals1)      
        totals.append(totals1)         

        totals3=dict()  
        utils.initAddInTotals9(totals3) 
        res = conn.executeAllQuery("SELECT c35 , COUNT(*) total FROM doc_presencial GROUP  BY c35")
        for value in res:
            utils.addInTotals9(value, totals3) 
        totals.append(totals3) 

    except Exception as e:
        print(e)
    
    return totals



def g2EAD():
    totals=list()    
    try:
            
        totals1=dict()  
        utils.initAddInTotals9(totals1)  
        res = conn.executeAllQuery("SELECT c37 , COUNT(*) total FROM tae_ead GROUP  BY c37")
        for value in res:
            utils.addInTotals9(value, totals1) 
        totals.append(totals1)

        totals3=dict()   
        utils.initAddInTotals9(totals3) 
        res = conn.executeAllQuery("SELECT c37 , COUNT(*) total FROM doc_ead GROUP  BY c37")
        for value in res:
            utils.addInTotals9(value, totals3) 
        totals.append(totals3)
        

    except Exception as e:
        print(e)
    
    return totals


def plotChartEixo4D5G2(g, title):
    res = g  
    novoRes = list()

    for i in range(len(res[0].values())):
        barList = list()
        for j in range(len(res)):
            l = list(res[j].values())
            barList.append(l[i])      
        novoRes.append(barList)

    barLabels = list(res[0].keys())

    chartsPanda.plotChartPd8(["TAE","Docentes"],"",barLabels,
                            title, novoRes)



#plotChartEixo4D5G2(g2Pres(), "O Programa de Integração Institucional ... Se já participou de ações dessa natureza, como você avalia:")
#plotChartEixo4D5G2(g2EAD(), "O Programa de Integração Institucional ... Se já participou de ações dessa natureza, como você avalia:")

def g3EAD():
    totals=list()
    try:
        for i in range(17):
            to = dict()
            utils.initAddInTotals5(to)
            res = conn.executeAllQuery("SELECT c"+str(i+38)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+38)+"")
            for value in res:
                utils.addInTotals5(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+38)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+38)+"")
            for value in res:
                utils.addInTotals5(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g3Pres():
    totals=list()
    try:
        for i in range(17):
            to = dict()
            utils.initAddInTotals5(to) 
            res = conn.executeAllQuery("SELECT c"+str(i+37)+" , COUNT(*) total FROM tae_presencial GROUP  BY c"+str(i+37)+"")
            for value in res:
                utils.addInTotals5(value, to) 
                     
            res = conn.executeAllQuery("SELECT c"+str(i+36)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+36)+"")
            for value in res:
                utils.addInTotals5(value, to)       
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
    chartsPanda.plotChartPd3(['cursos de curta duração presenciais',
                             'cursos de curta duração à distância',
                             'aprendizagem em serviço',
                             'grupos formais de estudos',
                             'intercâmbios',
                             'estágios',
                             'seminários',
                             'congressos',
                             'treinamentos em serviço',
                             'visitas técnicas ... à ocupação',
                             'fóruns',
                             'apresentações de trabalhos ... tecnológicos',
                             'apresentações de trabalhos ... culturais',
                             'acompanhamento de estudantes ... tecnológicas',
                             'feiras de inovação tecnológica',
                             'missões internacionais',
                             'trabalho voluntário'],
                        'Total de Respostas',barLabels, 
                        '... Avalie apenas as ações, promovidas por entes INTERNOS do IFPE, que você participou:',
                        novoTs)

#res = g3EAD()
#g3Plot(res)

def g4EAD():
    totals=list()
    try:
        for i in range(17):
            to = dict()
            utils.initAddInTotals5(to)
            res = conn.executeAllQuery("SELECT c"+str(i+55)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+55)+"")
            for value in res:
                utils.addInTotals5(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+55)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+55)+"")
            for value in res:
                utils.addInTotals5(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g4Pres():
    totals=list()
    try:
        for i in range(17):
            to = dict()
            utils.initAddInTotals5(to) 
            res = conn.executeAllQuery("SELECT c"+str(i+54)+" , COUNT(*) total FROM tae_presencial GROUP  BY c"+str(i+54)+"")
            for value in res:
                utils.addInTotals5(value, to) 
                     
            res = conn.executeAllQuery("SELECT c"+str(i+53)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+53)+"")
            for value in res:
                utils.addInTotals5(value, to)       
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
    chartsPanda.plotChartPd3(['cursos de curta duração presenciais',
                             'cursos de curta duração à distância',
                             'aprendizagem em serviço',
                             'grupos formais de estudos',
                             'intercâmbios',
                             'estágios',
                             'seminários',
                             'congressos',
                             'treinamentos em serviço',
                             'visitas técnicas ... à ocupação',
                             'fóruns',
                             'apresentações de trabalhos ... tecnológicos',
                             'apresentações de trabalhos ... culturais',
                             'acompanhamento de estudantes ... tecnológicas',
                             'feiras de inovação tecnológica',
                             'missões internacionais',
                             'trabalho voluntário'],
                        'Total de Respostas',barLabels, 
                        '... Avalie apenas as ações, promovidas por entes EXTERNOS do IFPE, que você participou:',
                        novoTs)

#res = g4Pres()
#g4Plot(res)

def g5Pres():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals10(dict1)
        res = conn.executeAllQuery("SELECT c71 , COUNT(*) total FROM tae_presencial GROUP  BY c71")
        for value in res:
            utils.addInTotals10(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals10(dict2)
        res = conn.executeAllQuery("SELECT c70 , COUNT(*) total FROM doc_presencial GROUP  BY c70")
        for value in res:
            utils.addInTotals10(value, dict2) 
        totals.append(dict2)

    except Exception as e:
        print(e)
    
    return totals

def g5EAD():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals10(dict1)
        res = conn.executeAllQuery("SELECT c72 , COUNT(*) total FROM tae_ead GROUP  BY c72")
        for value in res:
            utils.addInTotals10(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals10(dict2)
        res = conn.executeAllQuery("SELECT c72 , COUNT(*) total FROM doc_ead GROUP  BY c72")
        for value in res:
            utils.addInTotals10(value, dict2) 
        totals.append(dict2)

    except Exception as e:
        print(e)
    
    return totals

#ts = g5Pres()
#charts.plotChartDuplo(ts[0].keys(), '', 
#    'O Programa de Complementação de Estudos ... Se já participou de ações dessa natureza, indique qual horário você fez uso:', 
#    ts[0].values(), ts[1].values())

#ts = g5EAD()
#charts.plotChartDuplo(ts[0].keys(), '', 
#    'O Programa de Complementação de Estudos ... Se já participou de ações dessa natureza, indique qual horário você fez uso:', 
#    ts[0].values(), ts[1].values())

def g6Pres():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals11(dict1)
        res = conn.executeAllQuery("SELECT c72 , COUNT(*) total FROM tae_presencial GROUP  BY c72")
        for value in res:
            utils.addInTotals11(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals11(dict2)
        res = conn.executeAllQuery("SELECT c71 , COUNT(*) total FROM doc_presencial GROUP  BY c71")
        for value in res:
            utils.addInTotals11(value, dict2) 
        totals.append(dict2)

    except Exception as e:
        print(e)
    
    return totals

def g6EAD():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals11(dict1)
        res = conn.executeAllQuery("SELECT c73 , COUNT(*) total FROM tae_ead GROUP  BY c73")
        for value in res:
            utils.addInTotals11(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals11(dict2)
        res = conn.executeAllQuery("SELECT c73 , COUNT(*) total FROM doc_ead GROUP  BY c73")
        for value in res:
            utils.addInTotals11(value, dict2) 
        totals.append(dict2)

    except Exception as e:
        print(e)
    
    return totals

#ts = g6Pres()
#charts.plotChartDuplo(ts[0].keys(), '', 
#    'Qual o nível do último curso que você participou ou está participando, enquanto servidor do IFPE?', 
#    ts[0].values(), ts[1].values())

#ts = g6EAD()
#charts.plotChartDuplo(ts[0].keys(), '', 
#    'Qual o nível do último curso que você participou ou está participando, enquanto servidor do IFPE?', 
#    ts[0].values(), ts[1].values())

def g7Pres():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals12(dict1)
        res = conn.executeAllQuery("SELECT c73 , COUNT(*) total FROM tae_presencial GROUP  BY c73")
        for value in res:
            utils.addInTotals12(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals12(dict2)
        res = conn.executeAllQuery("SELECT c72 , COUNT(*) total FROM doc_presencial GROUP  BY c72")
        for value in res:
            utils.addInTotals12(value, dict2) 
        totals.append(dict2)

    except Exception as e:
        print(e)
    
    return totals

def g7EAD():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals12(dict1)
        res = conn.executeAllQuery("SELECT c74 , COUNT(*) total FROM tae_ead GROUP  BY c74")
        for value in res:
            utils.addInTotals12(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals12(dict2)        
        res = conn.executeAllQuery("SELECT c74 , COUNT(*) total FROM doc_ead GROUP  BY c74")
        for value in res:
            utils.addInTotals12(value, dict2) 
        totals.append(dict2)        
    except Exception as e:
        print(e)
    
    return totals

#ts = g7Pres()
#charts.plotChartDuplo(ts[0].keys(), '', 
#    'Para o curso STRICTO SENSU indicado na questão anterior assinale se houve afastamento de acordo com as situações abaixo:', 
#    ts[0].values(), ts[1].values())

#ts = g7EAD()
#charts.plotChartDuplo(ts[0].keys(), '', 
#    'Para o curso STRICTO SENSU indicado na questão anterior assinale se houve afastamento de acordo com as situações abaixo:', 
#    ts[0].values(), ts[1].values())

def g8Pres():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals13(dict1)
        res = conn.executeAllQuery("SELECT c74 , COUNT(*) total FROM tae_presencial GROUP  BY c74")
        for value in res:
            utils.addInTotals13(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals13(dict2)
        res = conn.executeAllQuery("SELECT c73 , COUNT(*) total FROM doc_presencial GROUP  BY c73")
        for value in res:
            utils.addInTotals13(value, dict2) 
        totals.append(dict2)

    except Exception as e:
        print(e)
    
    return totals

def g8EAD():
    totals=list()
    try:
        dict1 = dict()
        utils.initAddInTotals13(dict1)
        res = conn.executeAllQuery("SELECT c75 , COUNT(*) total FROM tae_ead GROUP  BY c75")
        for value in res:
            utils.addInTotals13(value, dict1) 
        totals.append(dict1)

        dict2 = dict()
        utils.initAddInTotals13(dict2)        
        res = conn.executeAllQuery("SELECT c75 , COUNT(*) total FROM doc_ead GROUP  BY c75")
        for value in res:
            utils.addInTotals13(value, dict2) 
        totals.append(dict2)        
    except Exception as e:
        print(e)
    
    return totals

#ts = g8Pres()
#charts.plotChartDuplo(ts[0].keys(), '', 
#    'Se foi contemplado com licença capacitação, por quanto tempo?', 
#    ts[0].values(), ts[1].values())

#ts = g8EAD()
#charts.plotChartDuplo(ts[0].keys(), '', 
#    'Se foi contemplado com licença capacitação, por quanto tempo?', 
#    ts[0].values(), ts[1].values())


def g9EAD():
    totals=list()
    try:
        for i in range(3):
            to = dict()
            utils.initAddInTotals6(to)
            res = conn.executeAllQuery("SELECT c"+str(i+76)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+76)+"")
            for value in res:
                utils.addInTotals6(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+76)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+76)+"")
            for value in res:
                utils.addInTotals6(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g9Pres():
    totals=list()
    try:
        for i in range(3):
            to = dict()
            utils.initAddInTotals6(to) 
            res = conn.executeAllQuery("SELECT c"+str(i+75)+" , COUNT(*) total FROM tae_presencial GROUP  BY c"+str(i+75)+"")
            for value in res:
                utils.addInTotals6(value, to) 
                     
            res = conn.executeAllQuery("SELECT c"+str(i+74)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+74)+"")
            for value in res:
                utils.addInTotals6(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g9Plot(totals):
    ts = totals
    novoTs = list()

    for i in range(len(ts[0].values())):
        barList = list()
        for j in range(len(ts)):
            l = list(ts[j].values())
            barList.append(l[i])      
        novoTs.append(barList)
 
    barLabels = list(ts[0].keys())
    chartsPanda.plotChartPd4(['Práticas esportivas em equipe',
                             'Realização de jogos intercampi',
                             'Realização de eventos festivos nas datas comemorativas'],
                        'Total de Respostas',barLabels, 
                        'Referente à Política de Qualidade de Vida no Trabalho (PQVT), ... você participou?',
                        novoTs)

#res = g9EAD()
#g9Plot(res)


def g10EAD():
    totals=list()
    try:
        for i in range(4):
            to = dict()
            utils.initAddInTotals6(to)
            res = conn.executeAllQuery("SELECT c"+str(i+79)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+79)+"")
            for value in res:
                utils.addInTotals6(value, to) 
            
            res = conn.executeAllQuery("SELECT c"+str(i+79)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+79)+"")
            for value in res:
                utils.addInTotals6(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g10Pres():
    totals=list()
    try:
        for i in range(4):
            to = dict()
            utils.initAddInTotals6(to) 
            res = conn.executeAllQuery("SELECT c"+str(i+78)+" , COUNT(*) total FROM tae_presencial GROUP  BY c"+str(i+78)+"")
            for value in res:
                utils.addInTotals6(value, to) 
                     
            res = conn.executeAllQuery("SELECT c"+str(i+77)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+77)+"")
            for value in res:
                utils.addInTotals6(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g10Plot(totals):
    ts = totals
    novoTs = list()

    for i in range(len(ts[0].values())):
        barList = list()
        for j in range(len(ts)):
            l = list(ts[j].values())
            barList.append(l[i])      
        novoTs.append(barList)
 
    barLabels = list(ts[0].keys())
    chartsPanda.plotChartPd4(['Ginástica laboral',
                             'Exercícios físicos',
                             'Palestras',
                             'Atividades ... servidor x família dentro da instituição'],
                        'Total de Respostas',barLabels, 
                        'Quanto ao programa de prevenção ao estresse ocupacional, ... que você participou?',
                        novoTs)

#res = g10EAD()
#g10Plot(res)


def g11Pres():
    totals=list() 
    try:
        totals1=dict()  
        utils.initAddInTotals14(totals1)  
        res = conn.executeAllQuery("SELECT c82 , COUNT(*) total FROM tae_presencial GROUP  BY c82")
        for value in res:
            utils.addInTotals14(value, totals1)      
        totals.append(totals1)         

        totals3=dict()  
        utils.initAddInTotals14(totals3) 
        res = conn.executeAllQuery("SELECT c81 , COUNT(*) total FROM doc_presencial GROUP  BY c81")
        for value in res:
            utils.addInTotals14(value, totals3) 
        totals.append(totals3) 

    except Exception as e:
        print(e)
    
    return totals



def g11EAD():
    totals=list()    
    try:
            
        totals1=dict()  
        utils.initAddInTotals14(totals1)  
        res = conn.executeAllQuery("SELECT c83 , COUNT(*) total FROM tae_ead GROUP  BY c83")
        for value in res:
            utils.addInTotals14(value, totals1) 
        totals.append(totals1)

        totals3=dict()   
        utils.initAddInTotals14(totals3) 
        res = conn.executeAllQuery("SELECT c83 , COUNT(*) total FROM doc_ead GROUP  BY c83")
        for value in res:
            utils.addInTotals14(value, totals3) 
        totals.append(totals3)
        

    except Exception as e:
        print(e)
    
    return totals


def plotChartEixo4D5G11(g, title):
    res = g  
    novoRes = list()

    for i in range(len(res[0].values())):
        barList = list()
        for j in range(len(res)):
            l = list(res[j].values())
            barList.append(l[i])      
        novoRes.append(barList)

    barLabels = list(res[0].keys())

    chartsPanda.plotChartPd9(["TAE","Docentes"],"",barLabels,
                            title, novoRes)



#plotChartEixo4D5G11(g11Pres(), "Se, no período pandêmico, você teve acesso ... como você avalia essas ações?")
plotChartEixo4D5G11(g11EAD(), "Se, no período pandêmico, você teve acesso ... como você avalia essas ações?")