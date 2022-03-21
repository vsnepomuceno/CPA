import mysql.connector


mydb = mysql.connector.connect(
  host="cpa.ifpe.edu.br",
  user="cpa",
  password="cp@2021",
  database="cpa_coleta"
)

mycursor = mydb.cursor()

def executeAllQuery(query):
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  return myresult

def executeOneQuery(query):
  mycursor.execute(query)
  myresult = mycursor.fetchone()
  return myresult

def executeManyQuery(query, many):
  mycursor.execute(query)
  myresult = mycursor.fetchmany(many)
  return myresult


#query = "select `resposta`, count( resp.resposta ), u.modalidade from resposta resp inner join pergunta perg on resp.pergunta_id=perg.id inner join usuario u on resp.respondente_id=u.id where perg.titulo LIKE '2)%' AND perg.sub_titulo LIKE '2.1)%' AND (`resposta`= 0 OR `resposta`= 1 OR `resposta`= 2 OR `resposta`= 3 OR `resposta`= 4 OR `resposta`= 5) group BY u.modalidade, resp.`resposta` order BY u.modalidade, resp.`resposta`"

#res = executeAllQuery(query)
#print(res)