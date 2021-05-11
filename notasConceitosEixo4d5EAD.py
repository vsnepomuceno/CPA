import db.connectorMySql as conn
import utils
import notasConceitosUtil as nUtils

conceitosgerais = list()


def n1EAD():
    try:
        for i in range(6):
            to = dict()                
            utils.initAddInTotals3(to)
            res = conn.executeAllQuery("SELECT c"+str(i+31)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+31)+"")
            for value in res:
                utils.addInTotals3(value, to) 

            res = nUtils.calcularConceitoEeadDocTae(to)
            conceitosgerais.append(res)

            to = dict()      
            res = conn.executeAllQuery("SELECT c"+str(i+31)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+31)+"")
            for value in res:
                utils.addInTotals3(value, to)       
            
            res = nUtils.calcularConceitoEeadDocTae(to)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)


n1EAD()

def n2EAD():
    try:
        totals1=dict() 
        utils.initAddInTotals9(totals1)  
        res = conn.executeAllQuery("SELECT c37 , COUNT(*) total FROM tae_ead GROUP  BY c37")
        for value in res:
            utils.addInTotals9(value, totals1)    

        res = nUtils.calcularConceitoEeadDocTae(totals1)
        conceitosgerais.append(res)

        totals1=dict() 
        utils.initAddInTotals9(totals1)
        res = conn.executeAllQuery("SELECT c37 , COUNT(*) total FROM doc_ead GROUP  BY c37")
        for value in res:
            utils.addInTotals9(value, totals1) 

        res = nUtils.calcularConceitoEeadDocTae(totals1)
        conceitosgerais.append(res)
    except Exception as e:
        print(e)
    

n2EAD()

def n3EAD():
    try:
        for i in range(17):
            to = dict()
            utils.initAddInTotals5(to) 
            res = conn.executeAllQuery("SELECT c"+str(i+38)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+38)+"")
            for value in res:
                utils.addInTotals5(value, to) 

            res = nUtils.calcularConceitoEeadDocTae(to)
            conceitosgerais.append(res)

            to = dict()
            utils.initAddInTotals5(to)
            res = conn.executeAllQuery("SELECT c"+str(i+38)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+38)+"")
            for value in res:
                utils.addInTotals5(value, to)       
            res = nUtils.calcularConceitoEeadDocTae(to)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)

n3EAD()


def n4EAD():
    try:
        for i in range(17):
            to = dict()
            utils.initAddInTotals5(to) 
            res = conn.executeAllQuery("SELECT c"+str(i+55)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+55)+"")
            for value in res:
                utils.addInTotals5(value, to) 

            res = nUtils.calcularConceitoEeadDocTae(to)
            conceitosgerais.append(res)   
            
            to = dict()
            utils.initAddInTotals5(to)
            res = conn.executeAllQuery("SELECT c"+str(i+55)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+55)+"")
            for value in res:
                utils.addInTotals5(value, to)  
                
            res = nUtils.calcularConceitoEeadDocTae(to)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)

n4EAD()


### N5 Não faz sentido ####

### N6 Não faz sentido ####

### N7 Não faz sentido ####

### N8 Não faz sentido ####

def n9EAD():
    try:
        for i in range(3):
            to = dict()
            utils.initAddInTotals6(to) 
            res = conn.executeAllQuery("SELECT c"+str(i+76)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+76)+"")
            for value in res:
                utils.addInTotals6(value, to) 

            res = nUtils.calcularConceitoEeadDocTae(to)
            conceitosgerais.append(res)

            to = dict()
            utils.initAddInTotals6(to)  
            res = conn.executeAllQuery("SELECT c"+str(i+76)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+76)+"")
            for value in res:
                utils.addInTotals6(value, to)                  

            res = nUtils.calcularConceitoEeadDocTae(to)
            conceitosgerais.append(res)
    except Exception as e:
        print(e)
    

n9EAD()

def n10EAD():
    try:
        for i in range(4):
            to = dict()
            utils.initAddInTotals6(to) 
            res = conn.executeAllQuery("SELECT c"+str(i+79)+" , COUNT(*) total FROM tae_ead GROUP  BY c"+str(i+79)+"")
            for value in res:
                utils.addInTotals6(value, to) 

            res = nUtils.calcularConceitoEeadDocTae(to)
            conceitosgerais.append(res)

            to = dict()
            utils.initAddInTotals6(to) 
            res = conn.executeAllQuery("SELECT c"+str(i+79)+" , COUNT(*) total FROM doc_ead GROUP  BY c"+str(i+79)+"")
            for value in res:
                utils.addInTotals6(value, to)  

            res = nUtils.calcularConceitoEeadDocTae(to)
            conceitosgerais.append(res)

    except Exception as e:
        print(e)
    
n10EAD()

def n11EAD():
    try:
        totals1=dict()  
        utils.initAddInTotals14(totals1)  
        res = conn.executeAllQuery("SELECT c83 , COUNT(*) total FROM tae_ead GROUP  BY c83")
        for value in res:
            utils.addInTotals14(value, totals1) 

        res = nUtils.calcularConceitoEeadDocTae(totals1)
        conceitosgerais.append(res)

        totals1=dict()  
        utils.initAddInTotals14(totals1)
        res = conn.executeAllQuery("SELECT c83 , COUNT(*) total FROM doc_ead GROUP  BY c83")
        for value in res:
            utils.addInTotals14(value, totals1) 

        res = nUtils.calcularConceitoEeadDocTae(totals1)
        conceitosgerais.append(res)
    except Exception as e:
        print(e)
    
n11EAD()

nUtils.printConceitosGeraisEixo4D5EAD(conceitosgerais, 'conceitosEixo4d5EAD.txt')