from asyncio.windows_events import NULL
import utils
import charts
import chartsPanda
import connectorMySql as conn


def initDicts(dictInit):     
    dictInit[0] = 0
    dictInit[1] = 0
    dictInit[2] = 0
    dictInit[3] = 0
    dictInit[4] = 0        
    dictInit[5] = 0


def Plot(hLabels, ylabel, barLabels, title, totals, modalidade):
    ts = totals
    novoTs = list()
    for i in range(len(ts[0].values())):
        barList = list()
        for j in range(len(ts)):
            l = list(ts[j].values())
            barList.append(l[i])      
        novoTs.append(barList)
    chartsPanda.plotChartPd(hLabels, ylabel,barLabels, title, novoTs, modalidade)

def initBarLabels(barLabels, escala):    
    if (escala == "ESCALA_1"):
        barLabels.append("Não sei responder / Não se aplica")
        barLabels.append("Péssimo")
        barLabels.append("Ruim")
        barLabels.append("Regular")
        barLabels.append("Bom")
        barLabels.append("Ótimo")
    elif (escala == "ESCALA_3"):
        barLabels.append("Não sei responder/ Não se aplica")
        barLabels.append("Discordo totalmente")
        barLabels.append("Discordo")
        barLabels.append("Não concordo, nem discordo")
        barLabels.append("Concordo")
        barLabels.append("Concordo totalmente")

def generateGraphics() :

    hLabels = []
    ylabel = ""
    barLabels= [] 
    title = ""

    for i in range(41):
        i = i+1
        query = """SELECT
                        perg.titulo,    
                        perg.sub_titulo,
                        perg.`tipo_pergunta`,
                        u.modalidade,
                        u.segmento,
                        `resposta`,
                        COUNT(resp.resposta)
                    FROM
                        resposta resp
                    INNER JOIN pergunta perg ON
                        resp.pergunta_id = perg.id
                    INNER JOIN usuario u ON
                        resp.respondente_id = u.id
                    WHERE
                        perg.titulo LIKE '{number})%' AND(
                            `resposta` = 0 OR `resposta` = 1 OR `resposta` = 2 OR `resposta` = 3 OR `resposta` = 4 OR `resposta` = 5
                        )
                    GROUP BY
                        u.modalidade,
                        u.segmento,
                        resp.`resposta`,
                        perg.titulo,
                        perg.sub_titulo,
                        perg.`tipo_pergunta`
                    ORDER BY
                        perg.titulo,
                        perg.sub_titulo,
                        u.modalidade,
                        u.segmento,
                        resp.`resposta`"""

        query = query.format(number=i)
        #print(query)

        res = conn.executeAllQuery(query)
        #print(res)
        
        if (len(res) > 0) :
            
            title = res[0][0]          
            subtitle = res[0][1]
            escala = res[0][2]
            modalidade = NULL
            segmento = res[0][4]

            if (escala == 'SIM_OU_NAO') :
                continue

            initBarLabels(barLabels, escala)    
            if (subtitle) :    
                hLabels.append(subtitle[0:60])
                ylabel = "Total de Respostas"
            else:
                hLabels.append("Discente")
                hLabels.append("Docente")
                hLabels.append("TAE")
                ylabel = ""
            dataEAD = list()
            dataPresencial = list()
            
            dataDiscente = dict()
            dataDocente = dict()
            dataTAE = dict()
            dataAgreg = dict()
            initDicts(dataDiscente)
            initDicts(dataDocente)
            initDicts(dataTAE)
            initDicts(dataAgreg)
            

            for value in res:                

                if (modalidade and (modalidade != value[3])) :  # mudou modalidade
                    #print("MUDOU MODALIDADE")
                    if (modalidade == 'EAD') :
                        if (subtitle) :
                            dataEAD.append(dataAgreg)
                        else:
                            dataEAD.append(dataDiscente)
                            dataEAD.append(dataDocente)
                            dataEAD.append(dataTAE)
                    if (modalidade == 'PRESENCIAL') :
                        if (subtitle) :
                            dataPresencial.append(dataAgreg)
                        else:
                            dataPresencial.append(dataDiscente)
                            dataPresencial.append(dataDocente)
                            dataPresencial.append(dataTAE)

                    dataDiscente = dict()
                    dataDocente = dict()
                    dataTAE = dict()
                    dataAgreg = dict()
                    initDicts(dataDiscente)
                    initDicts(dataDocente)
                    initDicts(dataTAE)
                    initDicts(dataAgreg)

                if (subtitle and (subtitle != value[1])):
                    hLabels.append(value[1][0:60])
                subtitle = value[1]
                modalidade = value[3] 
                segmento = value[4]  
                
                
                
                if (segmento == 'DISCENTE'):
                    if (subtitle):
                        dataAgreg[value[5]] = dataAgreg[value[5]] + value[6]
                    else:                        
                        dataDiscente[value[5]] = value[6]
                elif (segmento == 'DOCENTE'):   
                    if (subtitle):
                        dataAgreg[value[5]] = dataAgreg[value[5]] + value[6]
                    else:                        
                        dataDocente[value[5]] = value[6]
                elif (segmento == 'TAE'):           
                    if (subtitle):
                        dataAgreg[value[5]] = dataAgreg[value[5]] + value[6] 
                    else:
                        dataTAE[value[5]] = value[6]
                            

            # após processar último registro da consulta    
            if (modalidade == 'EAD') :
                if (subtitle) :
                    dataEAD.append(dataAgreg)
                else:
                    dataEAD.append(dataDiscente)
                    dataEAD.append(dataDocente)
                    dataEAD.append(dataTAE)
            if (modalidade == 'PRESENCIAL') :
                if (subtitle) :
                    dataPresencial.append(dataAgreg)
                else:
                    dataPresencial.append(dataDiscente)
                    dataPresencial.append(dataDocente)
                    dataPresencial.append(dataTAE)

              
            print(title)
            if (len(title) > 110):
                if (len(dataEAD) > 0):
                    Plot(hLabels, ylabel, barLabels, title[0:110]+"\n"+title[110:len(title)], dataEAD, "EAD")
                if (len(dataPresencial) > 0):
                    Plot(hLabels, ylabel, barLabels, title[0:110]+"\n"+title[110:len(title)], dataPresencial, "Presencial")
            else:
                if (len(dataEAD) > 0):
                    Plot(hLabels, ylabel, barLabels, title, dataEAD, "EAD")
                if (len(dataPresencial) > 0):
                    Plot(hLabels, ylabel, barLabels, title, dataPresencial, "Presencial")
            hLabels = []
            ylabel = ""
            barLabels= [] 
            title = ""
            
  
generateGraphics()