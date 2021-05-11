import db.connectorMySql as conn
import utils
import notasConceitosUtil as nUtils

conceitosgerais = list()

### g1 não faz sentido ###

def n2EAD():
    try:
        for i in range(4):
            
            to = dict()
            utils.initAddInTotals15(to)
            res = conn.executeAllQuery("SELECT c"+str(i+106)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+106)+"")
            for value in res:
                utils.addInTotals15(value, to) 

            #print(to)
            res = nUtils.calcularConceito3EAD(to)
            #print(res)
            conceitosgerais.append(res)

            to = dict()
            utils.initAddInTotals15(to)      
            res = conn.executeAllQuery("SELECT c"+str(i+106)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+106)+"")
            for value in res:
                utils.addInTotals15(value, to)   

            res = nUtils.calcularConceito3EAD(to)
            conceitosgerais.append(res)

            for campus in nUtils.campiEad:
                to = dict()
                utils.initAddInTotals15(to)
                #print("SELECT c"+str(i+48)+" , COUNT(*) total FROM disc_ead where c6=\'"+ campus + "\' GROUP  BY c"+str(i+48)+"")
                res = conn.executeAllQuery("SELECT c"+str(i+48)+" , COUNT(*) total FROM disc_ead where c7=\'"+ campus + "\' GROUP  BY c"+str(i+48)+"")
                for value in res:
                    utils.addInTotals15(value, to) 
                res = nUtils.calcularConceito3EAD(to)
                conceitosgerais.append(res)

                
    except Exception as e:
        print(e)
    

n2EAD()


def n3Pres():
    try:
        for i in range(3):            
            to = dict()
            utils.initAddInTotals16(to) 

            res = conn.executeAllQuery("SELECT c"+str(i+110)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+110)+"")
            for value in res:
                utils.addInTotals16(value, to) 

            res = nUtils.calcularConceito3EAD(to)
            conceitosgerais.append(res)

            to = dict()
            utils.initAddInTotals16(to) 
            res = conn.executeAllQuery("SELECT c"+str(i+110)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+110)+"")
            for value in res:
                utils.addInTotals16(value, to)       

            res = nUtils.calcularConceito3EAD(to)
            conceitosgerais.append(res)

            for campus in nUtils.campiEad:
                to = dict()
                utils.initAddInTotals16(to)
                res = conn.executeAllQuery("SELECT c"+str(i+52)+" , COUNT(*) total FROM disc_ead where c7=\'"+ campus + "\' GROUP  BY c"+str(i+52)+"")
                for value in res:
                    utils.addInTotals16(value, to) 
                res = nUtils.calcularConceito3EAD(to)
                conceitosgerais.append(res)
               
    except Exception as e:
        print(e)

n3Pres()

nUtils.printConceitosGeraisEAD(conceitosgerais, 'conceitosEixo4d10EAD.txt')