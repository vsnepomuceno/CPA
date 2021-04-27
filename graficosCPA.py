import db.connectorMySql as conn
import charts
import utils

campi = ('Afogados da Ingazeira', 
'Barreiros',
'Belo Jardim',
'Cabo de Santo Agostinho',
'Caruaru',
'Garanhuns',
'Igarassu',
'Ipojuca',
'Paulista',
'Pesqueira',
'Recife',
'Vitória de Santo Antão')

def getTotals():
    totals=dict()
    tot = 0;
    try:
        res = conn.executeOneQuery("select count(*) from disc_ead")
        totals['disc_ead'] = res[0]
        tot = tot + res[0]
        res = conn.executeOneQuery("select count(*) from disc_presencial")
        totals['disc_presencial'] = res[0]
        tot = tot + res[0]
        res = conn.executeOneQuery("select count(*) from doc_ead")
        totals['doc_ead'] = res[0]
        tot = tot + res[0]
        res = conn.executeOneQuery("select count(*) from doc_presencial")
        totals['doc_presencial'] = res[0]
        tot = tot + res[0]
        res = conn.executeOneQuery("select count(*) from tae_ead")
        totals['tae_ead'] = res[0]
        tot = tot + res[0]
        res = conn.executeOneQuery("select count(*) from tae_presencial")
        totals['tae_presencial'] = res[0]
        tot = tot + res[0]
        totals['Total'] = tot
    except Exception as e:
        print(e)
    
    return totals


#ts = getTotals()

#tsTotal = 0
#print(ts)
#charts.plotChart(['discente EAD', 'discente presencial',
#                    'docente EAD','docente presencial',
#                    'TAE EAD', 'TAE presencial'], 'N°', 'Total de Respostas', ts)


def addInTotals(value, tot):
    if (value[0] == 'Bom'):
        if (tot.get('Bom') != None) :
            tot['Bom'] = tot.get('Bom') + value[1]
        else:
            tot['Bom'] = value[1]
    if (value[0] == 'Regular'):
        if (tot.get('Regular') != None) :
            tot['Regular'] = tot.get('Regular') + value[1]
        else:
            tot['Regular'] = value[1]
    if (value[0] == 'Ótimo'):
        if (tot.get('Ótimo') != None) :
            tot['Ótimo'] = tot.get('Ótimo') + value[1]
        else:
            tot['Ótimo'] = value[1]
    if (value[0] == 'Desconheço'):
        if (tot.get('Desconheço') != None) :
            tot['Desconheço'] = tot.get('Desconheço') + value[1]
        else:
            tot['Desconheço'] = value[1]
    if (value[0] == 'Ruim'):
        if (tot.get('Ruim') != None) :
            tot['Ruim'] = tot.get('Ruim') + value[1]
        else:
            tot['Ruim'] = value[1]
    if (value[0] == 'Péssimo'):
        if (tot.get('Péssimo') != None) :
            tot['Péssimo'] = tot.get('Péssimo') + value[1]
        else:
            tot['Péssimo'] = value[1]

def addInTotals2(value, tot):
    if (value[0] == 'Totalmente participativo'):
        if (tot.get('Totalmente participativo') != None) :
            tot['Totalmente participativo'] = tot.get('Totalmente participativo') + value[1]
        else:
            tot['Totalmente participativo'] = value[1]

    if (value[0] == 'Muito participativo'):
        if (tot.get('Muito participativo') != None) :
            tot['Muito participativo'] = tot.get('Muito participativo') + value[1]
        else:
            tot['Muito participativo'] = value[1]

    if (value[0] == 'Participação ocasional'):
        if (tot.get('Participação ocasional') != None) :
            tot['Participação ocasional'] = tot.get('Participação ocasional') + value[1]
        else:
            tot['Participação ocasional'] = value[1]

    if (value[0] == 'Pouco participativo'):
        if (tot.get('Pouco participativo') != None) :
            tot['Pouco participativo'] = tot.get('Pouco participativo') + value[1]
        else:
            tot['Pouco participativo'] = value[1]

    if (value[0] == 'Não participei'):
        if (tot.get('Não participei') != None) :
            tot['Não participei'] = tot.get('Não participei') + value[1]
        else:
            tot['Não participei'] = value[1]
    

def getTotalsbyCampiPres():
    totals=dict()
    try:
        res = conn.executeAllQuery("SELECT c97 , COUNT(*) total FROM tae_presencial GROUP  BY c97")
        utils.initAddInTotals4(totals)
        for value in res:
            utils.addInTotals4(value, totals)     
        res = conn.executeAllQuery("SELECT c42 , COUNT(*) total FROM disc_presencial GROUP  BY c42")
        for value in res:
            utils.addInTotals4(value, totals) 
        res = conn.executeAllQuery("SELECT c96 , COUNT(*) total FROM doc_presencial GROUP  BY c96")
        for value in res:
            utils.addInTotals4(value, totals)         

    except Exception as e:
        print(e)
    
    return totals


def getTotalsbyCampiEAD():
    totals=dict()
    utils.initAddInTotals4(totals)
    try:
        res = conn.executeAllQuery("SELECT c105 , COUNT(*) total FROM tae_ead GROUP  BY c105")
        for value in res:
            utils.addInTotals4(value, totals) 
        res = conn.executeAllQuery("SELECT c47 , COUNT(*) total FROM disc_ead GROUP  BY c47")
        for value in res:
            utils.addInTotals4(value, totals) 
        res = conn.executeAllQuery("SELECT c105 , COUNT(*) total FROM doc_ead GROUP  BY c105")
        for value in res:
            utils.addInTotals4(value, totals) 
        

    except Exception as e:
        print(e)
    
    return totals

ts = getTotalsbyCampiEAD()
#print(ts)
charts.plotChart(ts.keys(), '', 
    'Como você avalia seu nível de conhecimento a respeito do PDI?', ts.values())