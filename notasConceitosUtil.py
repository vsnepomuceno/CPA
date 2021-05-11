
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
'Sede/Reitoria',
'Vitória de Santo Antão')

campiEad = (
    'Limoeiro',
    'Águas Belas',
    'Palmares',
    'Sertânia',
    'Santa Cruz do Capibaribe',
    'Carpina',
    'Gravatá',
    'Santana do Ipanema/AL',
    )

def calcularConceito(tot):
    conceitos = list()
    for cidade in tot:
        valorConceito = 0
        totalCasos = 0    
        for caso in cidade:
            if (caso == 'Desconheço' or caso == 'Inexistente/ Desconheço' 
                or caso == 'Nunca participei' or caso == 'Não participei' 
                or caso == 'Não ofertado' or caso == 'Inexistente/Desconheço'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 0*cidade.get(caso)
            if (caso == 'Péssimo'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 1*cidade.get(caso)
            if (caso == 'Ruim'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 2*cidade.get(caso)
            if (caso == 'Regular'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 3*cidade.get(caso)
            if (caso == 'Bom'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 4*cidade.get(caso)
            if (caso == 'Ótimo'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 5*cidade.get(caso)
        
        if (totalCasos != 0) :
            trunc = int((valorConceito/totalCasos)*100)
            conceitos.append(trunc/100)
        else :
            conceitos.append(0)
    return conceitos


def calcularConceito2(tot):
    conceitos = list()
    for cidade in tot:
        valorConceito = 0
        totalCasos = 0    
        for caso in cidade:
            if (caso == 'Pouco participativo'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 1*cidade.get(caso)
            if (caso == 'Não participei'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 2*cidade.get(caso)
            if (caso == 'Participação ocasional'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 3*cidade.get(caso)
            if (caso == 'Totalmente participativo'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 4*cidade.get(caso)
            if (caso == 'Muito participativo'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 5*cidade.get(caso)
        
        trunc = int((valorConceito/totalCasos)*100)
        conceitos.append(trunc/100)
    return conceitos


def calcularConceito3(tot):
    conceitos = list()
    for cidade in tot:
        valorConceito = 0
        totalCasos = 0    
        for caso in cidade:
            if (caso == 'Não tive acesso' or caso == 'Inexistente/Desconheço'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 0*cidade.get(caso)
            if (caso == 'Péssima'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 1*cidade.get(caso)
            if (caso == 'Ruim'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 2*cidade.get(caso)
            if (caso == 'Regular'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 3*cidade.get(caso)
            if (caso == 'Boa'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 4*cidade.get(caso)
            if (caso == 'Ótima'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 5*cidade.get(caso)
        
        trunc = int((valorConceito/totalCasos)*100)
        conceitos.append(trunc/100)
    return conceitos

def calcularConceito4(tot):
    conceitos = list()
    for cidade in tot:
        valorConceito = 0
        totalCasos = 0    
        for caso in cidade:
            if (caso == 'Desconheço' or caso == 'Não conheço/Não participo/Não acompanho'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 0*cidade.get(caso)
            if (caso == 'Discordo totalmente'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 1*cidade.get(caso)
            if (caso == 'Discordo'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 2*cidade.get(caso)
            if (caso == 'Não concordo, nem discordo'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 3*cidade.get(caso)
            if (caso == 'Concordo'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 4*cidade.get(caso)
            if (caso == 'Concordo totalmente'):
                totalCasos = totalCasos + cidade.get(caso)
                valorConceito = valorConceito + 5*cidade.get(caso)
        
        trunc = int((valorConceito/totalCasos)*100)
        conceitos.append(trunc/100)
    return conceitos


def printConceitosGerais(conceitos, filename):
    text = ''
    file_object  = open(filename, "a+")
    file_object.seek(0)
    data = file_object.readline()
    if len(data) == 0 :
        for campus in campi:
            text = text + campus + '$$'
        text = text + '\n'

    
    for quesito in conceitos:        
        for nota in quesito:
            text = text + str(nota) + '$'
            if (nota - int(nota)) >= 0.5:
                text = text + str(int(nota+1)) + '$'
            else:
                text = text + str(int(nota)) + '$'

        text = text + '\n'    
    
    file_object.write(text)
    file_object.close()


def calcularConceitoEeadDocTae(tot):
    conceito = 0    
    valorConceito = 0
    totalCasos = 0    
    for caso in tot:
        if (caso == 'Desconheço' or caso == 'Inexistente/ Desconheço' 
            or caso == 'Nunca participei' or caso == 'Não participei' 
            or caso == 'Não ofertado' or caso == 'Inexistente/Desconheço'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 0*tot.get(caso)
        if (caso == 'Péssimo'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 1*tot.get(caso)
        if (caso == 'Ruim'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 2*tot.get(caso)
        if (caso == 'Regular'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 3*tot.get(caso)
        if (caso == 'Bom'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 4*tot.get(caso)
        if (caso == 'Ótimo'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 5*tot.get(caso)
    
    if (totalCasos != 0) :
        trunc = int((valorConceito/totalCasos)*100)
        conceito = (trunc/100)
    else :
        conceito = 0
    return conceito


def calcularConceito2EAD(tot):
    conceito = 0
    valorConceito = 0
    totalCasos = 0    
    for caso in tot:
        if (caso == 'Pouco participativo'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 1*tot.get(caso)
        if (caso == 'Não participei'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 2*tot.get(caso)
        if (caso == 'Participação ocasional'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 3*tot.get(caso)
        if (caso == 'Totalmente participativo'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 4*tot.get(caso)
        if (caso == 'Muito participativo'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 5*tot.get(caso)
    
    trunc = int((valorConceito/totalCasos)*100)
    conceito = (trunc/100)
    return conceito


def calcularConceito3EAD(tot):
    conceito = 0
    valorConceito = 0
    totalCasos = 0    
    for caso in tot:
        if (caso == 'Desconheço' or caso == 'Não conheço/Não participo/Não acompanho'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 0*tot.get(caso)
        if (caso == 'Discordo totalmente'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 1*tot.get(caso)
        if (caso == 'Discordo'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 2*tot.get(caso)
        if (caso == 'Não concordo, nem discordo'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 3*tot.get(caso)
        if (caso == 'Concordo'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 4*tot.get(caso)
        if (caso == 'Concordo totalmente'):
            totalCasos = totalCasos + tot.get(caso)
            valorConceito = valorConceito + 5*tot.get(caso)
    
    if (totalCasos != 0) :
        trunc = int((valorConceito/totalCasos)*100)
        conceito = (trunc/100)
        
    return conceito

def printConceitosGeraisEAD(conceitos, filename):
    text = ''
    file_object  = open(filename, "a+")
    file_object.seek(0)
    data = file_object.readline()
    tam = 0

    if len(data) == 0 :
        text = text + 'TAE' + '$$'
        text = text + "Docente" + '$$'
        for campus in campiEad:
            text = text + campus + '$$'
        text = text + '\n'
    else :
        text = text + '\n'

    
    for nota in conceitos:
        #print(nota)
        text = text + str(nota) + '$'
        if (nota - int(nota)) >= 0.5:
            text = text + str(int(nota+1)) + '$'
        else:
            text = text + str(int(nota)) + '$'
        tam = tam + 1

        if ((tam%(len(campiEad)+2)) == 0) :
            text = text + '\n'  

    
    file_object.write(text)
    file_object.close()


def printConceitosGeraisEixo4D5EAD(conceitos, filename):
    text = ''
    file_object  = open(filename, "a+")
    file_object.seek(0)
    tam = 0

    text = text + 'TAE' + '$$'
    text = text + "Docente" + '$$' + '\n'

    
    for nota in conceitos:
        print(nota)
        text = text + str(nota) + '$'
        if (nota - int(nota)) >= 0.5:
            text = text + str(int(nota+1)) + '$'
        else:
            text = text + str(int(nota)) + '$'
        tam = tam + 1

        if ((tam%2) == 0) :
            text = text + '\n'  

    
    file_object.write(text)
    file_object.close()


def printConceitosGeraisEAD2(conceitos, filename):
    text = ''
    file_object  = open(filename, "a+")
    file_object.seek(0)
    data = file_object.readline()
    tam = 0

    if len(data) == 0 :
        text = text + 'TAE' + '$$'
        text = text + "Docente" + '$$'
        for campus in campiEad:
            text = text + campus + '$$'
        text = text + '\n'
    else :
        text = text + '\n'

    
    for nota in conceitos:
        #print(nota)
        text = text + str(nota) + '$'
        if (nota - int(nota)) >= 0.5:
            text = text + str(int(nota+1)) + '$'
        else:
            text = text + str(int(nota)) + '$'
        tam = tam + 1

        if ((tam%2) == 0) :
            text = text + '\n'  

    
    file_object.write(text)
    file_object.close()