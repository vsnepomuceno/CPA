import db.connectorMySql as conn
import utils
import notasConceitosUtil as nUtils

conceitosgerais = list()

def n1Pres():
    try:
        for i in range(6):
            totals=list()
            for campus in nUtils.campi:
                to = dict()                
                res = conn.executeAllQuery("SELECT c"+str(i+30)+" , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+30)+"")
                for value in res:
                    utils.addInTotals3(value, to) 
                        
                res = conn.executeAllQuery("SELECT c"+str(i+29)+" , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c"+str(i+29)+"")
                for value in res:
                    utils.addInTotals3(value, to)       
                totals.append(to)      
            res = nUtils.calcularConceito(totals)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)


n1Pres()

def n2Pres():
    totals=list() 
    try:
        for campus in nUtils.campi:
            totals1=dict() 
            utils.initAddInTotals9(totals1)  
            res = conn.executeAllQuery("SELECT c36 , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c36")
            for value in res:
                utils.addInTotals9(value, totals1)    

            res = conn.executeAllQuery("SELECT c35 , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c35")
            for value in res:
                utils.addInTotals9(value, totals1) 

            totals.append(totals1) 

    except Exception as e:
        print(e)
    
    return totals

res = nUtils.calcularConceito(n2Pres())
conceitosgerais.append(res)


def n3Pres():
    try:
        for i in range(17):
            totals=list()
            for campus in nUtils.campi:
                to = dict()
                utils.initAddInTotals5(to) 
                res = conn.executeAllQuery("SELECT c"+str(i+37)+" , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+37)+"")
                for value in res:
                    utils.addInTotals5(value, to) 
                        
                res = conn.executeAllQuery("SELECT c"+str(i+36)+" , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c"+str(i+36)+"")
                for value in res:
                    utils.addInTotals5(value, to)       
                totals.append(to)   
            res = nUtils.calcularConceito(totals)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)

n3Pres()


def n4Pres():
    try:
        for i in range(17):
            totals=list()
            for campus in nUtils.campi:
                to = dict()
                utils.initAddInTotals5(to) 
                res = conn.executeAllQuery("SELECT c"+str(i+54)+" , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+54)+"")
                for value in res:
                    utils.addInTotals5(value, to) 
                        
                res = conn.executeAllQuery("SELECT c"+str(i+53)+" , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c"+str(i+53)+"")
                for value in res:
                    utils.addInTotals5(value, to)       
                totals.append(to)      
            res = nUtils.calcularConceito(totals)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)

n4Pres()


### N5 Não faz sentido ####

### N6 Não faz sentido ####

### N7 Não faz sentido ####

### N8 Não faz sentido ####

def n9Pres():
    try:
        for i in range(3):
            totals=list()
            for campus in nUtils.campi:
                to = dict()
                utils.initAddInTotals6(to) 
                res = conn.executeAllQuery("SELECT c"+str(i+75)+" , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+75)+"")
                for value in res:
                    utils.addInTotals6(value, to) 
                        
                res = conn.executeAllQuery("SELECT c"+str(i+74)+" , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c"+str(i+74)+"")
                for value in res:
                    utils.addInTotals6(value, to)       
                totals.append(to)      
            res = nUtils.calcularConceito(totals)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)
    

n9Pres()

def n10Pres():
    try:
        for i in range(4):
            totals=list()
            for campus in nUtils.campi:
                to = dict()
                utils.initAddInTotals6(to) 
                res = conn.executeAllQuery("SELECT c"+str(i+78)+" , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+78)+"")
                for value in res:
                    utils.addInTotals6(value, to) 
                        
                res = conn.executeAllQuery("SELECT c"+str(i+77)+" , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c"+str(i+77)+"")
                for value in res:
                    utils.addInTotals6(value, to)       
                totals.append(to)      
            res = nUtils.calcularConceito(totals)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)
    
n10Pres()

def n11Pres():
    totals=list() 
    try:
        for campus in nUtils.campi:
            totals1=dict()  
            utils.initAddInTotals14(totals1)  
            res = conn.executeAllQuery("SELECT c82 , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c82")
            for value in res:
                utils.addInTotals14(value, totals1) 

            res = conn.executeAllQuery("SELECT c81 , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c81")
            for value in res:
                utils.addInTotals14(value, totals1) 
            totals.append(totals1) 

    except Exception as e:
        print(e)
    
    return totals

res = nUtils.calcularConceito3(n11Pres())
conceitosgerais.append(res)

nUtils.printConceitosGerais(conceitosgerais, 'conceitosEixo4d5Pres.txt')