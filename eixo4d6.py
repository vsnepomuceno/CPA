import db.connectorMySql as conn
import utils
import charts
import chartsPanda

def g1EAD():
    totals=list()
    try:
        for i in range(12):
            if (i != 6) :
                to = dict()
                utils.initAddInTotals7(to)
                res = conn.executeAllQuery("SELECT c"+str(i+85)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+85)+"")
                for value in res:
                    utils.addInTotals7(value, to) 
                
                res = conn.executeAllQuery("SELECT c"+str(i+85)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+85)+"")
                for value in res:
                    utils.addInTotals7(value, to)  

                if (i < 6):    
                    res = conn.executeAllQuery("SELECT c"+str(i+31)+" , COUNT(*) total FROM disc_ead GROUP  BY c"+str(i+31)+"")
                    for value in res:
                        utils.addInTotals7(value, to)   
                else :
                    res = conn.executeAllQuery("SELECT c"+str((i-1)+31)+" , COUNT(*) total FROM disc_ead GROUP  BY c"+str((i-1)+31)+"")
                    for value in res:
                        utils.addInTotals7(value, to)            
                totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g1EADQ7(totals):
    try:
                    
        to1 = dict()
        utils.initAddInTotals7(to1)
        res = conn.executeAllQuery("SELECT c91 , COUNT(*) total FROM tae_ead GROUP  BY c91")
        for value in res:
            utils.addInTotals7(value, to1) 
        totals.append(to1)

        to2 = dict()
        utils.initAddInTotals7(to2)
        res = conn.executeAllQuery("SELECT c91 , COUNT(*) total FROM doc_ead GROUP  BY c91")
        for value in res:
            utils.addInTotals7(value, to2)                      
        totals.append(to2)      

    except Exception as e:
        print(e)
    
    return totals

def g1Pres():
    totals=list()
    try:
        for i in range(12):
            if (i != 6) :
                to = dict()
                utils.initAddInTotals7(to)
                res = conn.executeAllQuery("SELECT c"+str(i+84)+" , COUNT(*) total FROM tae_presencial GROUP  BY c"+str(i+84)+"")
                for value in res:
                    utils.addInTotals7(value, to) 
                        
                res = conn.executeAllQuery("SELECT c"+str(i+83)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+83)+"")
                for value in res:
                    utils.addInTotals7(value, to)     

                if (i < 6):
                    res = conn.executeAllQuery("SELECT c"+str(i+30)+" , COUNT(*) total FROM disc_presencial GROUP  BY c"+str(i+30)+"")
                    for value in res:
                        utils.addInTotals7(value, to)   
                else:          
                    res = conn.executeAllQuery("SELECT c"+str((i-1)+30)+" , COUNT(*) total FROM disc_presencial GROUP  BY c"+str(i+30)+"")
                    for value in res:
                        utils.addInTotals7(value, to) 

                totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g1PresQ7(totals):
    try:
                    
        to1 = dict()
        utils.initAddInTotals7(to1)
        res = conn.executeAllQuery("SELECT c90 , COUNT(*) total FROM tae_presencial GROUP  BY c90")
        for value in res:
            utils.addInTotals7(value, to1) 
        totals.append(to1)

        to2 = dict()
        utils.initAddInTotals7(to2)
        res = conn.executeAllQuery("SELECT c89 , COUNT(*) total FROM doc_presencial GROUP  BY c89")
        for value in res:
            utils.addInTotals7(value, to2)                      
        totals.append(to2)      

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
    chartsPanda.plotChartPd5(['atuação dos órgãos de gestão (Pró-Reitorias)',
                             'atuação dos órgãos de gestão (Diretorias Sistêmicas)',
                             'atuação dos órgãos de gestão ao nível da EaD',
                             'atuação do Conselho Superior',
                             'atuação do Conselho de Dirigentes',
                             'atuação do Conselho de Ensino, Pesquisa e Extensão do IFPE',
                             'atuação do Comitê de Ética ',
                             'atuação do colegiado do curso',
                             'atuação do diretório acadêmico do curso',
                             'incentivo, à autonomia e à representatividade dos órgãos',
                             'participação da comunidade ... decisões institucionais',
                             'atuação da Comissão Interna de Supervisão dos TAE*',
                             'atuação da Comissão Permanente de Pessoal Docente*'],
                        'Total de Respostas',barLabels, 
                        'Avalie a política de gestão institucional quanto à/ao:',
                        novoTs)



#res = g1Pres()
#res = g1PresQ7(res)
#g1Plot(res)


def g2EAD():
    totals=list()
    try:
        for i in range(7):
            if (i != 1):
                to = dict()
                utils.initAddInTotals8(to)
                res = conn.executeAllQuery("SELECT c"+str(i+97)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+97)+"")
                for value in res:
                    utils.addInTotals8(value, to) 
                
                res = conn.executeAllQuery("SELECT c"+str(i+97)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+97)+"")
                for value in res:
                    utils.addInTotals8(value, to)  
                if ((i < 5)) :
                    res = conn.executeAllQuery("SELECT c"+str(i+42)+" , COUNT(*) total FROM disc_ead GROUP  BY c"+str(i+42)+"")
                    for value in res:
                        utils.addInTotals8(value, to)   
                            
                totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals

def g2EADQ1(totals):
    try:                    
        to = dict()
        utils.initAddInTotals8(to)
        res = conn.executeAllQuery("SELECT c98 , COUNT(*) total FROM tae_ead GROUP  BY c98")
        for value in res:
            utils.addInTotals8(value, to) 

        res = conn.executeAllQuery("SELECT c98 , COUNT(*) total FROM doc_ead GROUP  BY c98")
        for value in res:
            utils.addInTotals8(value, to)                      
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
    chartsPanda.plotChartPd6(['atende a demanda',
                              'faz uso de estratégias ... por diferentes mídias',
                              'faz uso de estratégias ... por diferentes suportes',
                              'faz uso de estratégias ... por diferentes  linguagens',
                              'possui plano de atualização ou é atualizado com frequência*',
                              'tem o apoio à produção de material autoral pelo corpo docente*',
                              'possui equipe técnica multidisciplinar responsável*'],
                        'Total de Respostas',barLabels, 
                        'Quanto à produção e distribuição de material didático:',
                        novoTs)

res = g2EAD()
res = g2EADQ1(res)
g2Plot(res)
