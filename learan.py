import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12652",
  database="mydatabase"

)

mycursor = mydb.cursor()

sql = "SELECT \
  user.name AS user, \
  products.name AS favorite \
  FROM user \
  INNER JOIN products ON user.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)