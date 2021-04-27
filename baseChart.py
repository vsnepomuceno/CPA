import db.connectorMySql as conn
import utils
import charts
import chartsPanda

def baseSearch():
    totals=list()
    try:
        for i in range(12):
            to = dict()
            res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM tae_presencial GROUP  BY c10")
            for value in res:
                utils.addInTotals3(value,to)        
            res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+10)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM disc_presencial GROUP  BY c"+str(i+10)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            res = conn.executeAllQuery("SELECT c"+str(i+11)+" , COUNT(*) total FROM disc_ead GROUP  BY c"+str(i+11)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            res = conn.executeAllQuery("SELECT c"+str(i+9)+" , COUNT(*) total FROM doc_presencial GROUP  BY c"+str(i+9)+"")
            for value in res:
                utils.addInTotals3(value, to) 
            res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+10)+"")
            for value in res:
                utils.addInTotals3(value, to)       
            totals.append(to)      

    except Exception as e:
        print(e)
    
    return totals


def baseChart():
    ts = baseSearch()
    print(ts)
    novoTs = list()

    for i in range(len(ts[0].values())):
        barList = list()
        for j in range(len(ts)):
            l = list(ts[j].values())
            barList.append(l[i])      
        novoTs.append(barList)
 
    print("NOVO TS")
    print(novoTs)
    barLabels = list(ts[0].keys())
    chartsPanda.plotChartPd(['de ensino de graduação', 'de ensino de pós-graduação', 'de pesquisa e iniciação científica', 
                            'de inovação tecnológica', 'de desenvolvimento artístico e cultural', 'de valorização da diversidade', 
                            'de valorização do meio ambiente','de valorização da memória cultural','de valorização do patrimônio cultural',
                            'de valorização da produção artística', 'dos direitos humanos e da igualdade étnico-racial','de valorização da educação a distância'],
                        'Total de Respostas',barLabels, 
                        'Avaliação do alinhamento entre as políticas institucionais expressas no PDI e as atividades.',
                        novoTs)


baseChart()