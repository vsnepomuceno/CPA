import db.connectorMySql as conn
import utils
import notasConceitosUtil as nUtils

conceitosgerais = list()

def n1Pres():    
    try:
        for i in range(12):
            if (i != 6) :
                totals=list()
                for campus in nUtils.campi:                
                    to = dict()
                    utils.initAddInTotals7(to)
                    res = conn.executeAllQuery("SELECT c"+str(i+84)+" , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+84)+"")
                    for value in res:
                        utils.addInTotals7(value, to) 
                            
                    res = conn.executeAllQuery("SELECT c"+str(i+83)+" , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c"+str(i+83)+"")
                    for value in res:
                        utils.addInTotals7(value, to)     

                    if (i < 6):
                        res = conn.executeAllQuery("SELECT c"+str(i+30)+" , COUNT(*) total FROM disc_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+30)+"")
                        for value in res:
                            utils.addInTotals7(value, to)   
                    else:          
                        res = conn.executeAllQuery("SELECT c"+str((i-1)+30)+" , COUNT(*) total FROM disc_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+30)+"")
                        for value in res:
                            utils.addInTotals7(value, to) 

                    totals.append(to)      
                res = nUtils.calcularConceito(totals)
                conceitosgerais.append(res)
    except Exception as e:
        print(e)
    
    return totals

def n1PresQ7():
    totalsTAE=list()
    totalsDoc=list()
    try:
        for campus in nUtils.campi:            
            to1 = dict()
            utils.initAddInTotals7(to1)
            res = conn.executeAllQuery("SELECT c90 , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c90")
            for value in res:
                utils.addInTotals7(value, to1) 
            totalsTAE.append(to1) 

            to2 = dict()
            utils.initAddInTotals7(to2)
            res = conn.executeAllQuery("SELECT c89 , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c89")
            for value in res:
                utils.addInTotals7(value, to2) 

            totalsDoc.append(to2)  
        print(totalsTAE)    
        print(totalsDoc)
        resCal = nUtils.calcularConceito(totalsTAE)
        conceitosgerais.append(resCal)  
        resCal = nUtils.calcularConceito(totalsDoc)
        conceitosgerais.append(resCal)      
    except Exception as e:
        print(e)
    


n1Pres()
n1PresQ7()

nUtils.printConceitosGerais(conceitosgerais, 'conceitosEixo4d6Pres.txt')