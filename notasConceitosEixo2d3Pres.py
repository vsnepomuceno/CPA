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
                res = conn.executeAllQuery("SELECT c"+str(i+23)+" , COUNT(*) total FROM tae_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+23)+"")
                for value in res:
                    utils.addInTotals3(value, to) 
                
                res = conn.executeAllQuery("SELECT c"+str(i+23)+" , COUNT(*) total FROM disc_presencial where c6=\'"+ campus + "\' GROUP  BY c"+str(i+23)+"")
                for value in res:
                    utils.addInTotals3(value, to) 
                
                res = conn.executeAllQuery("SELECT c"+str(i+22)+" , COUNT(*) total FROM doc_presencial where c5=\'"+ campus + "\' GROUP  BY c"+str(i+22)+"")
                for value in res:
                    utils.addInTotals3(value, to)       
                totals.append(to)      

            res = nUtils.calcularConceito(totals)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)


n1Pres()

nUtils.printConceitosGerais(conceitosgerais, 'conceitosEixo2d3Pres.txt')