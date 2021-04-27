
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
