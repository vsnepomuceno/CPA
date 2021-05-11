import db.connectorMySql as conn
import utils
import notasConceitosUtil as nUtils

conceitosgerais = list()


def n1EAD():
    try:
        for i in range(6):
        
            totals1=dict()  
            utils.initAddInTotals3(totals1)          
            res = conn.executeAllQuery("SELECT c"+str(i+23)+", COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+23)+"")
            for value in res:
                utils.addInTotals3(value, totals1)   

            res = nUtils.calcularConceitoEeadDocTae(totals1)
            conceitosgerais.append(res)

            totals1=dict()  
            utils.initAddInTotals3(totals1)
            res = conn.executeAllQuery("SELECT c"+str(i+23)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+23)+"")
            for value in res:
                utils.addInTotals3(value, totals1) 

            res = nUtils.calcularConceitoEeadDocTae(totals1)
            conceitosgerais.append(res)

            for campus in nUtils.campiEad:
                totals1=dict()  
                utils.initAddInTotals3(totals1)
                res = conn.executeAllQuery("SELECT c"+str(i+24)+" , COUNT(*) total FROM disc_ead where c7=\'"+ campus +"\' GROUP  BY c"+str(i+24)+"")
                
                for value in res:
                    utils.addInTotals3(value, totals1) 
                res = nUtils.calcularConceitoEeadDocTae(totals1)
                conceitosgerais.append(res)

    except Exception as e:
        print(e)


n1EAD()

nUtils.printConceitosGeraisEAD(conceitosgerais, 'conceitosEixo2d3EAD.txt')