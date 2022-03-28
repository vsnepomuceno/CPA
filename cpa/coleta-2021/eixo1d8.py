from asyncio.windows_events import NULL
import utils
import charts
import chartsPanda
import connectorMySql as conn

class Registro:
    campus = ''
    titulo = ''
    subtitulo = ''
    conceito = 0.0



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


def printConceitosGerais(all, filename):
    text = ''
    file_object  = open(filename, "w")
    file_object.seek(0)

    
    for key in all.keys(): 
        print(key)
        subtitulo = ""
        titulo = ""
        for reg in all.get(key):            
                
            if (subtitulo != "" and reg.subtitulo and reg.subtitulo != subtitulo):
                text = text + "\n" + reg.subtitulo
            elif (titulo != "" and not reg.subtitulo and reg.titulo != titulo):
                text = text + "\n" + reg.titulo
            elif (subtitulo == "" and reg.subtitulo):
                text = text + reg.subtitulo
            elif (subtitulo == "" and not reg.subtitulo):
                text = text + reg.titulo

            subtitulo = reg.subtitulo
            titulo = reg.titulo
            conceitoGeral = 0
            if (reg.conceito - int(reg.conceito)) >= 0.5:
                conceitoGeral = int(reg.conceito+1)
            else:
                conceitoGeral = int(reg.conceito)

            if (reg.subtitulo):
                #print(reg.campus + " " + reg.titulo + " " +reg.subtitulo + " " + str(reg.conceito)) 
                text = text + "$" + str(reg.conceito) + "$" + str(conceitoGeral)
            else:
                #print(reg.campus + " " + reg.titulo + " SEM subtilte " + str(reg.conceito))
                text = text  + "$" + str(reg.conceito) + "$" + str(conceitoGeral)

        text = text + "\n"

    
    #for nota in conceitos:
        #print(nota)
        #text = text + str(nota) + '$'
        #if (nota - int(nota)) >= 0.5:
            #text = text + str(int(nota+1)) + '$'
        #else:
            #text = text + str(int(nota)) + '$'
        #tam = tam + 1

        #if ((tam%(len(campiEad)+2)) == 0) :
            #text = text + '\n'  

    
    file_object.write(text)
    file_object.close()

def generateGraphics() :

    hLabels = []
    ylabel = ""
    barLabels= [] 
    title = ""

    for i in range(41):
        i = i+2
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
                if (len(subtitle) > 60):
                    if (i == 37 or i == 39 or i == 41) :
                        try:                        
                            index = subtitle[120:len(subtitle)].index(" ")
                            hLabels.append(subtitle[0:5] + subtitle[60:120+index] + "\n" + subtitle[120+index:180])
                        except ValueError:
                            hLabels.append(subtitle[0:5] + subtitle[60:len(subtitle)])
                    else:     
                        try:  
                            index = subtitle[60:len(subtitle)].index(" ")
                            hLabels.append(subtitle[0:60+index] + "\n" + subtitle[60+index:120])
                        except ValueError:
                            hLabels.append(subtitle)
                    
                    
                else: 
                    hLabels.append(subtitle)
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
                    if (len(value[1]) > 60):
                        
                            if (i == 37 or i == 39 or i == 41) :
                                try:
                                    index = value[1][120:len(value[1])].index(" ")
                                    hLabels.append(subtitle[0:5] + value[1][60:120+index] + "\n" + value[1][120+index:180])
                                except ValueError:
                                    hLabels.append(subtitle[0:5] + value[1][60:len(value[1])])
                            else:  
                                try:   
                                    index = value[1][60:len(value[1])].index(" ")
                                    hLabels.append(value[1][0:60+index] + "\n" + value[1][60+index:120])
                                except ValueError:
                                    hLabels.append(value[1])
                        
                    else: 
                        hLabels.append(value[1])
                    
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
            
            if (len(title) > 100):
                try:
                    index = title[100:len(title)].index(" ")
                    title = title[0:100+index]+"\n"+title[100+index:len(title)]
                except ValueError:
                    print("ValueError")
           
            if (len(dataEAD) > 0):
                Plot(hLabels, ylabel, barLabels, title, dataEAD, "EAD")
            if (len(dataPresencial) > 0):
                Plot(hLabels, ylabel, barLabels, title, dataPresencial, "Presencial")

            hLabels = []
            ylabel = ""
            barLabels= [] 
            title = ""
            break
            
  
#generateGraphics()

def generateEADConcepts() :
    allRegistros = dict()
    for i in range(41):
        i = i+1
        query = """SELECT
                        perg.titulo,
                        perg.sub_titulo,
                        curso1_.nome_curso,
                        `resposta`,
                        COUNT(resp.resposta)
                    FROM
                        resposta resp
                    INNER JOIN pergunta perg ON
                        resp.pergunta_id = perg.id
                    INNER JOIN usuario u ON
                        resp.respondente_id = u.id
                    INNER JOIN respondente_curso cursos0_ ON
                        cursos0_.respondente_id = u.id
                    INNER JOIN curso curso1_ ON
                        cursos0_.curso_id = curso1_.id
                    INNER JOIN campus campus2_ ON
                        curso1_.campus_id = campus2_.id
                    WHERE
                        perg.titulo LIKE '{number})%' AND (
                            `resposta` = 0 OR `resposta` = 1 OR `resposta` = 2 OR `resposta` = 3 OR `resposta` = 4 OR `resposta` = 5
                        ) AND  campus2_.nome_campus = 'EAD' AND (perg.tipo_pergunta = 'ESCALA_1' OR perg.tipo_pergunta = 'ESCALA_3')
                    GROUP BY
                        resp.`resposta`,
                        perg.titulo,
                        curso1_.nome_curso,
                        perg.sub_titulo
                    ORDER BY
                        perg.titulo,
                        perg.sub_titulo,
                        curso1_.nome_curso,
                        resp.`resposta`"""

        query = query.format(number=i)
        #print(query)

        res = conn.executeAllQuery(query)
        #print(res)
        
        if (len(res) > 0) :
            for value in res:
                print(value)
            break

    return allRegistros


all = generateEADConcepts()      
#printConceitosGerais(all, "conceitosEAD.txt")

def generatePresencialConcepts() :

    allRegistros = dict()
    for i in range(41):
        i = i+1
        query = """SELECT
                        perg.titulo,
                        perg.sub_titulo,
                        campus2_.nome_campus,
                        `resposta`,
                        COUNT(resp.resposta)
                    FROM
                        resposta resp
                    INNER JOIN pergunta perg ON
                        resp.pergunta_id = perg.id
                    INNER JOIN usuario u ON
                        resp.respondente_id = u.id
                    INNER JOIN respondente_curso cursos0_ ON
                        cursos0_.respondente_id = u.id
                    INNER JOIN curso curso1_ ON
                        cursos0_.curso_id = curso1_.id
                    INNER JOIN campus campus2_ ON
                        curso1_.campus_id = campus2_.id
                    WHERE
                        perg.titulo LIKE '{number})%' AND(
                            `resposta` = 0 OR `resposta` = 1 OR `resposta` = 2 OR `resposta` = 3 OR `resposta` = 4 OR `resposta` = 5
                        ) AND campus2_.nome_campus <> 'EAD' AND(
                            perg.tipo_pergunta = 'ESCALA_1' OR perg.tipo_pergunta = 'ESCALA_3'
                        )
                    GROUP BY
                        perg.titulo,
                        perg.sub_titulo,
                        campus2_.nome_campus,
                        resp.`resposta`
                    ORDER BY
                        perg.titulo,
                        perg.sub_titulo,
                        campus2_.nome_campus,
                        resp.`resposta`"""        

        query = query.format(number=i)
        #print(query)

        res = conn.executeAllQuery(query)
        #print(res)     
        registros = list()
        if (len(res) > 0) :                   
            reg =  Registro()  
            totalCasos = 0
            conceito = 0.0    
            for value in res:
                if (reg.campus == ''):
                    reg.campus = value[2] 
                    reg.titulo = value[0]           
                    reg.subtitulo = value[1]   

                if (reg.campus != value[2] or reg.subtitulo != value[1]): # mudou campus
                    trunc = int((conceito/totalCasos)*100)
                    reg.conceito = (trunc/100)
                    registros.append(reg)
                    reg = Registro()
                    reg.campus = value[2]
                    reg.titulo = value[0]           
                    reg.subtitulo = value[1]
                    totalCasos = 0
                    conceito = 0.0
                    
                # calcular conceito            
                conceito = conceito + value[3]*value[4]
                totalCasos = totalCasos + value[4]

            trunc = int((conceito/totalCasos)*100)
            reg.conceito = (trunc/100)
            registros.append(reg)

            allRegistros[i] = registros
            
    return allRegistros
            
 
#all = generatePresencialConcepts()
#printConceitosGerais(all, "conceitosPres.txt")

#campus = ''
#titulo = ''
#subtitulo = ''
#conceito = 0.0

#for key in all.keys(): 
    #print(key)
    #for reg in all.get(key):
        #if (reg.subtitulo):
            #print(reg.campus + " " + reg.titulo + " " +reg.subtitulo + " " + str(reg.conceito))       
        #else:
            #print(reg.campus + " " + reg.titulo + " SEM subtilte " + str(reg.conceito))      
        



