import db.connectorMySql as conn
import utils
import notasConceitosUtil as nUtils

conceitosgerais = list()

def n1Pres():
    totals=list() 
    try:
        for campus in nUtils.campi:
            totals1=dict()  
            utils.initAddInTotals(totals1)          
            res = conn.executeAllQuery("SELECT c7 , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c7")
            for value in res:
                utils.addInTotals(value, totals1)   

            res = conn.executeAllQuery("SELECT c7 , COUNT(*) total FROM disc_presencial where c6=\'"+ campus + "\' GROUP  BY c7")
            for value in res:
                utils.addInTotals(value, totals1) 

            res = conn.executeAllQuery("SELECT c6 , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c6")
            for value in res:
                utils.addInTotals(value, totals1) 
    
            totals.append(totals1)    
    except Exception as e:
        print(e)
    
    return totals



res = nUtils.calcularConceito(n1Pres())
conceitosgerais.append(res)


def n2Pres():
    totals=list() 
    try:
        for campus in nUtils.campi:
            totals1=dict()  
            utils.initAddInTotals(totals1)  
            res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c8")
            for value in res:
                utils.addInTotals(value, totals1)  

            res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM disc_presencial where c6=\'"+ campus + "\' GROUP  BY c8")
            for value in res:
                utils.addInTotals(value, totals1) 

            res = conn.executeAllQuery("SELECT c7 , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c7")
            for value in res:
                utils.addInTotals(value, totals1) 

            totals.append(totals1)
    except Exception as e:
        print(e)
    
    return totals


res = nUtils.calcularConceito(n2Pres())
conceitosgerais.append(res)


def n3Pres():
    totals=list() 
    try:
        for campus in nUtils.campi:
            totals1=dict()  
            utils.initAddInTotals2(totals1)  
            res = conn.executeAllQuery("SELECT c9 , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c9")
            for value in res:
                utils.addInTotals2(value, totals1)      

            totals2=dict()  
            utils.initAddInTotals2(totals2) 
            res = conn.executeAllQuery("SELECT c9 , COUNT(*) total FROM disc_presencial where c6=\'"+ campus + "\' GROUP  BY c9")
            for value in res:
                utils.addInTotals2(value, totals1) 

            totals3=dict()  
            utils.initAddInTotals2(totals3) 
            res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c8")
            for value in res:
                utils.addInTotals2(value, totals1) 

            totals.append(totals1)
    except Exception as e:
        print(e)
    
    return totals


res = nUtils.calcularConceito2(n3Pres())
conceitosgerais.append(res)

def n4Pres():
    
    try:    
        for i in range(12):
            totals=list()
            for campus in nUtils.campi:
                to = dict()
                utils.initAddInTotals3(to)
                res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c10")
                for value in res:
                    utils.addInTotals3(value,to)              
                res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM disc_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+10)+"")
                for value in res:
                    utils.addInTotals3(value, to)            
                res = conn.executeAllQuery("SELECT c"+str(i+9)+" , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c"+str(i+9)+"")
                for value in res:
                    utils.addInTotals3(value, to)                 
                totals.append(to)   
            res = nUtils.calcularConceito(totals)
            conceitosgerais.append(res)   

    except Exception as e:
        print(e)

n4Pres()

nUtils.printConceitosGerais(conceitosgerais, 'conceitosEixo2d1Pres.txt')