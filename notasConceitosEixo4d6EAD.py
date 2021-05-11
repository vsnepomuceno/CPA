import db.connectorMySql as conn
import utils
import notasConceitosUtil as nUtils

conceitosgerais = list()


def n1EAD():    
    try:
        for i in range(12):
            if (i != 6) :    
                #print("SELECT c"+str(i+85)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+85)+"")                           
                to = dict()
                utils.initAddInTotals7(to)
                res = conn.executeAllQuery("SELECT c"+str(i+85)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+85)+"")
                for value in res:
                    utils.addInTotals7(value, to) 
                
                res = nUtils.calcularConceitoEeadDocTae(to)
                conceitosgerais.append(res)

                to = dict()
                utils.initAddInTotals7(to)
                res = conn.executeAllQuery("SELECT c"+str(i+85)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+85)+"")
                for value in res:
                    utils.addInTotals7(value, to)     

                res = nUtils.calcularConceitoEeadDocTae(to)
                conceitosgerais.append(res)

                for campus in nUtils.campiEad:
                    to = dict()
                    utils.initAddInTotals7(to)
                    if (i < 6):
                        #print("SELECT c"+str(i+31)+" , COUNT(*) total FROM disc_ead where c7=\'"+ campus + "\' GROUP  BY c"+str(i+31)+"")
                        res = conn.executeAllQuery("SELECT c"+str(i+31)+" , COUNT(*) total FROM disc_ead where c7=\'"+ campus + "\' GROUP  BY c"+str(i+31)+"")
                        for value in res:
                            utils.addInTotals7(value, to)   
                    else:          
                        res = conn.executeAllQuery("SELECT c"+str((i-1)+31)+" , COUNT(*) total FROM disc_ead where c7=\'"+ campus + "\' GROUP  BY c"+str((i-1)+31)+"")
                        for value in res:
                            utils.addInTotals7(value, to) 
                    res = nUtils.calcularConceitoEeadDocTae(to)
                    conceitosgerais.append(res)

    except Exception as e:
        print(e)
    

def n1EADQ7():
    try:
        to1 = dict()
        utils.initAddInTotals7(to1)
        res = conn.executeAllQuery("SELECT c91 , COUNT(*) total FROM tae_ead GROUP  BY c91")
        for value in res:
            utils.addInTotals7(value, to1) 
        res = nUtils.calcularConceitoEeadDocTae(to1)
        conceitosgerais.append(res)

        to2 = dict()
        utils.initAddInTotals7(to2)
        res = conn.executeAllQuery("SELECT c91 , COUNT(*) total FROM doc_ead GROUP  BY c91")
        for value in res:
            utils.addInTotals7(value, to2) 

        res = nUtils.calcularConceitoEeadDocTae(to2)
        conceitosgerais.append(res)

    except Exception as e:
        print(e)
    


n1EAD()
n1EADQ7()

nUtils.printConceitosGeraisEAD(conceitosgerais, 'conceitosEixo4d6EAD.txt')

conceitosgerais = list()
conceitosgerais2 = list()

def n2EAD():
    try:
        for i in range(7):
            if (i != 1):
                to = dict()
                utils.initAddInTotals8(to)
                #print("SELECT c"+str(i+97)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+97)+"")
                res = conn.executeAllQuery("SELECT c"+str(i+97)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+97)+"")
                for value in res:
                    utils.addInTotals8(value, to) 

                res = nUtils.calcularConceito3EAD(to)
                #print(res)
                if ((i < 4)):
                    conceitosgerais.append(res)
                else:
                    conceitosgerais2.append(res)


                to = dict()
                utils.initAddInTotals8(to)
                #print("SELECT c"+str(i+97)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+97)+"")
                res = conn.executeAllQuery("SELECT c"+str(i+97)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+97)+"")
                for value in res:
                    utils.addInTotals8(value, to) 
                res = nUtils.calcularConceito3EAD(to)
                #print(res)
                if ((i < 4)):
                    conceitosgerais.append(res)
                else:
                    conceitosgerais2.append(res) 

                for campus in nUtils.campiEad:
                    if ((i < 4)):    
                        to = dict()
                        utils.initAddInTotals8(to)                        
                        #print("SELECT c"+str(i+42)+" , COUNT(*) total FROM disc_ead  where c7=\'"+ campus + "\' GROUP  BY c"+str(i+42)+"")           
                        res = conn.executeAllQuery("SELECT c"+str(i+42)+" , COUNT(*) total FROM disc_ead  where c7=\'"+ campus + "\' GROUP  BY c"+str(i+42)+"")
                        for value in res:
                            utils.addInTotals8(value, to) 
                        res = nUtils.calcularConceito3EAD(to)
                        #print(res)
                        conceitosgerais.append(res)  
                             

    except Exception as e:
        print(e)
    

def n2EADQ1():
    try:                    
        to = dict()
        utils.initAddInTotals8(to)
        res = conn.executeAllQuery("SELECT c98 , COUNT(*) total FROM tae_ead GROUP  BY c98")
        for value in res:
            utils.addInTotals8(value, to) 
        res = nUtils.calcularConceito3EAD(to)
        #print(res)
        conceitosgerais2.append(res)

        to = dict()
        utils.initAddInTotals8(to)
        res = conn.executeAllQuery("SELECT c98 , COUNT(*) total FROM doc_ead GROUP  BY c98")
        for value in res:
            utils.addInTotals8(value, to)  
        res = nUtils.calcularConceito3EAD(to)
        #print(res)
        conceitosgerais2.append(res) 

    except Exception as e:
        print(e)

n2EAD()
n2EADQ1()  

nUtils.printConceitosGeraisEAD(conceitosgerais, 'conceitosEixo4d6EAD.txt')

nUtils.printConceitosGeraisEAD2(conceitosgerais2, 'conceitosEixo4d6EAD.txt')

