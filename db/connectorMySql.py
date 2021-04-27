import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ifpe",
  database="cpa"
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