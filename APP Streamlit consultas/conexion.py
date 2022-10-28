import mysql.connector


database_username = 'admin'
database_password = '123456789'
database_ip       = 'database-2.cmmt68xsoykx.us-east-1.rds.amazonaws.com'
database_name     = 'sys'

miConexion = mysql.connector.connect(host=database_ip, user= database_username, passwd=database_password, db=database_name)
