import mysql.connector
cnx = mysql.connector.connect(host="localhost",
	user="root",
	password="1234",
	database="sakila")


def fetchFromDB(query,cursor):
	cursor.execute(query)	
	table = cursor.fetchall()
	for row in table:
		yield row

mycursor = cnx.cursor()
result = fetchFromDB("select * from payment",mycursor)
for i in result:
	print(i)
