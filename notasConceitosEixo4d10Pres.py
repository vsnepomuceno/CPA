import db.connectorMySql as conn
import utils
import notasConceitosUtil as nUtils

conceitosgerais = list()

### g1 não faz sentido ###


def n2Pres():
    try:
        for i in range(4):
            totals=list()
            for campus in nUtils.campi:
                to = dict()
                utils.initAddInTotals15(to) 

                res = conn.executeAllQuery("SELECT c"+str(i+98)+" , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+98)+"")
                for value in res:
                    utils.addInTotals15(value, to) 
                        
                res = conn.executeAllQuery("SELECT c"+str(i+97)+" , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c"+str(i+97)+"")
                for value in res:
                    utils.addInTotals15(value, to)       
                
                res = conn.executeAllQuery("SELECT c"+str(i+43)+" , COUNT(*) total FROM disc_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+43)+"")
                for value in res:
                    utils.addInTotals15(value, to) 

                totals.append(to)      
            res = nUtils.calcularConceito4(totals)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)
    
    return totals

n2Pres()


def n3Pres():
    try:
        for i in range(3):
            totals=list()
            for campus in nUtils.campi:
                to = dict()
                utils.initAddInTotals16(to) 

                res = conn.executeAllQuery("SELECT c"+str(i+102)+" , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+102)+"")
                for value in res:
                    utils.addInTotals16(value, to) 
                        
                res = conn.executeAllQuery("SELECT c"+str(i+101)+" , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c"+str(i+101)+"")
                for value in res:
                    utils.addInTotals16(value, to)       
                
                res = conn.executeAllQuery("SELECT c"+str(i+47)+" , COUNT(*) total FROM disc_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+47)+"")
                for value in res:
                    utils.addInTotals16(value, to) 

                totals.append(to)      
            res = nUtils.calcularConceito4(totals)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)
    
    return totals

n3Pres()

nUtils.printConceitosGerais(conceitosgerais, 'conceitosEixo4d10Pres.txt')