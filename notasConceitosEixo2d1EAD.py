import db.connectorMySql as conn
import utils
import notasConceitosUtil as nUtils

conceitosgerais = list()

def n1EAD():
    try:        
        totals1=dict()  
        utils.initAddInTotals(totals1)          
        res = conn.executeAllQuery("SELECT c7 , COUNT(*) total FROM tae_ead GROUP  BY c7")
        for value in res:
            utils.addInTotals(value, totals1)   

        res = nUtils.calcularConceitoEeadDocTae(totals1)
        conceitosgerais.append(res)

        totals1=dict()  
        utils.initAddInTotals(totals1)
        res = conn.executeAllQuery("SELECT c7 , COUNT(*) total FROM doc_ead GROUP  BY c7")
        for value in res:
            utils.addInTotals(value, totals1) 

        res = nUtils.calcularConceitoEeadDocTae(totals1)
        conceitosgerais.append(res)

        for campus in nUtils.campiEad:
            totals1=dict()  
            utils.initAddInTotals(totals1)
            res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM disc_ead where c7=\'"+ campus +"\' GROUP  BY c8")
            
            for value in res:
                utils.addInTotals(value, totals1) 
            res = nUtils.calcularConceitoEeadDocTae(totals1)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)


n1EAD()



def n2EAD():
    try:        
        totals1=dict()  
        utils.initAddInTotals(totals1)          
        res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM tae_ead GROUP  BY c8")
        for value in res:
            utils.addInTotals(value, totals1)   

        res = nUtils.calcularConceitoEeadDocTae(totals1)
        conceitosgerais.append(res)

        totals1=dict()  
        utils.initAddInTotals(totals1)
        res = conn.executeAllQuery("SELECT c8 , COUNT(*) total FROM doc_ead GROUP  BY c8")
        for value in res:
            utils.addInTotals(value, totals1) 

        res = nUtils.calcularConceitoEeadDocTae(totals1)
        conceitosgerais.append(res)

        for campus in nUtils.campiEad:
            totals1=dict()  
            utils.initAddInTotals(totals1)
            res = conn.executeAllQuery("SELECT c9 , COUNT(*) total FROM disc_ead where c7=\'"+ campus +"\' GROUP  BY c9")
            
            for value in res:
                utils.addInTotals(value, totals1) 
            res = nUtils.calcularConceitoEeadDocTae(totals1)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)

n2EAD()

def n3EAD():
    try:        
        totals1=dict()  
        utils.initAddInTotals2(totals1)          
        res = conn.executeAllQuery("SELECT c9, COUNT(*) total FROM tae_ead GROUP  BY c9")
        for value in res:
            utils.addInTotals2(value, totals1)   

        res = nUtils.calcularConceito2EAD(totals1)
        conceitosgerais.append(res)

        totals1=dict()  
        utils.initAddInTotals2(totals1)
        res = conn.executeAllQuery("SELECT c9 , COUNT(*) total FROM doc_ead GROUP  BY c9")
        for value in res:
            utils.addInTotals2(value, totals1) 

        res = nUtils.calcularConceito2EAD(totals1)
        conceitosgerais.append(res)

        for campus in nUtils.campiEad:
            totals1=dict()  
            utils.initAddInTotals2(totals1)
            res = conn.executeAllQuery("SELECT c10 , COUNT(*) total FROM disc_ead where c7=\'"+ campus +"\' GROUP  BY c10")
            
            for value in res:
                utils.addInTotals2(value, totals1) 
            res = nUtils.calcularConceito2EAD(totals1)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)


n3EAD()

def n4EAD():
    
    try:    
        for i in range(12):
            totals1=dict()  
            utils.initAddInTotals3(totals1)          
            res = conn.executeAllQuery("SELECT c"+str(i+10)+", COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+10)+"")
            for value in res:
                utils.addInTotals3(value, totals1)   

            res = nUtils.calcularConceitoEeadDocTae(totals1)
            conceitosgerais.append(res)

            totals1=dict()  
            utils.initAddInTotals3(totals1)
            res = conn.executeAllQuery("SELECT c"+str(i+10)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+10)+"")
            for value in res:
                utils.addInTotals3(value, totals1) 

            res = nUtils.calcularConceitoEeadDocTae(totals1)
            conceitosgerais.append(res)

            for campus in nUtils.campiEad:
                totals1=dict()  
                utils.initAddInTotals3(totals1)
                res = conn.executeAllQuery("SELECT c"+str(i+11)+" , COUNT(*) total FROM disc_ead where c7=\'"+ campus +"\' GROUP  BY c"+str(i+11)+"")
                
                for value in res:
                    utils.addInTotals3(value, totals1) 
                res = nUtils.calcularConceitoEeadDocTae(totals1)
                conceitosgerais.append(res)  

    except Exception as e:
        print(e)

n4EAD()

nUtils.printConceitosGeraisEAD(conceitosgerais, 'conceitosEixo2d1EAD.txt')
